write-host "Exporting translations from Crowdin..."
./l10nUtil.exe exportTranslations -o _addonL10n -c addon

New-Item -ItemType Directory -Force -Path addon/locale | Out-Null
New-Item -ItemType Directory -Force -Path addon/doc | Out-Null
Write-Host "Getting addon ID from environment..."
$addonId = $env:ADDON_ID.Trim()
if (-not $addonId) {
    Write-Error "Failed to get addon ID. Ensure buildVars.py and dependencies are present."
    exit 1
}

foreach ($dir in Get-ChildItem -Path "_addonL10n/$addonId" -Directory) {
    Write-Host "=============================="
    Write-Host "Processing language: $($dir.Name)"
    Write-Host "=============================="

    $langCode = $dir.Name

    # Paths
    $poFile = Join-Path $dir.FullName "$addonId.po"
    $localPoPath = "addon/locale/$langCode/LC_MESSAGES/nvda.po"

    $xliffFile = Join-Path $dir.FullName "$addonId.xliff"
    $targetDocDir = "addon/doc/$langCode"
    $mdFile = Join-Path $targetDocDir "readme.md"

    # ----------------------------
    # SKIP ENGLISH (source language)
    # ----------------------------
    if ($langCode -eq "en") {
        Write-Host "Skipping English (source language) → no XLIFF processing required"
        continue
    }

    # ----------------------------
    # PO PROCESSING
    # ----------------------------
    if (Test-Path $poFile) {
        Write-Host "Checking PO file..."
        uv run ./.github/scripts/checkTranslation.py "$poFile"
        $isPoTranslated = ($LASTEXITCODE -eq 0)
        Write-Host "PO translated: $isPoTranslated"
        if ($isPoTranslated) {
            Write-Host "Updating local PO"
            New-Item -ItemType Directory -Force -Path (Split-Path $localPoPath) | Out-Null
            Move-Item $poFile $localPoPath -Force
        } else {
            Write-Host "PO not translated"
            if (Test-Path $localPoPath) {
                Write-Host "Uploading local PO to Crowdin"
                ./l10nUtil.exe uploadTranslationFile $langCode "$addonId.po" $localPoPath -c addon
            } else {
                Write-Host "No local PO available"
            }
        }
    }

    # ----------------------------
    # XLIFF PROCESSING
    # ----------------------------
    if (Test-Path $xliffFile) {
        Write-Host "Checking XLIFF..."
        uv run ./.github/scripts/checkTranslation.py "$xliffFile"
        $isXliffTranslated = ($LASTEXITCODE -eq 0)
        Write-Host "XLIFF translated: $isXliffTranslated"
        if ($isXliffTranslated) {
            Write-Host "Converting XLIFF → MD"
            ./l10nUtil.exe xliff2md $xliffFile $mdFile
        } else {
            Write-Host "XLIFF not valid"
        }
    } else {
        Write-Host "No XLIFF file found"
    }
} # End foreach
