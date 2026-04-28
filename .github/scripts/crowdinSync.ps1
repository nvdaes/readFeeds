#!/usr/bin/env pwsh
$ErrorActionPreference = 'Stop'

# Git configuration for automated commits
git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"

$addonId = $env:ADDON_ID.Trim()
if (-not $addonId) {
    Write-Error "Failed to get addon ID."
    exit 1
}

# --- STEP 1: PREPARATION AND SOURCE UPDATE ---

$xliffFile = "./$addonId.xliff"
$mdFile = "./readme.md"

if (Test-Path $mdFile) {
    if (Test-Path $xliffFile) {
        $tempXliff = [System.IO.Path]::GetTempFileName()
        Copy-Item "$addonId.xliff" $tempXliff -Force
        Write-Host "Updating XLIFF source based on readme.md..."
        uv run .github/scripts/markdownTranslate.py updateXliff -m $mdFile -x $tempXliff -o $xliffFile
    } else {
        Write-Host "Creating new XLIFF template from readme.md..."
        uv run .github/scripts/markdownTranslate.py generateXliff -m $mdFile -o $xliffFile
    }
}

# Update POT file (addon interface)
uv run scons pot
$potFile = "$addonId.pot"

# --- STEP 2: UPLOAD SOURCES TO CROWDIN ---

if (Test-Path $potFile) {
    Write-Host "Uploading updated POT to Crowdin..."
    ./l10nUtil.exe uploadSourceFile "$potFile" -c addon
}

if (Test-Path $xliffFile) {
    Write-Host "Uploading updated XLIFF source to Crowdin..."
    ./l10nUtil.exe uploadSourceFile "$xliffFile" -c addon
    git add "$xliffFile"
    git diff --staged --quiet
    if ($LASTEXITCODE -ne 0) {
        git commit -m "Update $xliffFile for $addonId"
        git push
    }
}

# --- STEP 3: EXPORT AND PROCESS TRANSLATIONS ---

Write-Host "Exporting translations from Crowdin..."
./l10nUtil.exe exportTranslations -o _addonL10n -c addon

# Ensure base directories exist
New-Item -ItemType Directory -Force -Path addon/locale | Out-Null
New-Item -ItemType Directory -Force -Path addon/doc | Out-Null

foreach ($dir in Get-ChildItem -Path "_addonL10n/$addonId" -Directory) {
    $langCode = $dir.Name # This is the Crowdin ID (e.g., ar-SA, fr, pt-BR)
    
    if ($langCode -eq "en") { continue }

    # GET LOCAL NVDA DIRECTORY NAME VIA PYTHON MAPPING
    # This ensures "ar-SA" maps to "ar_SA", "pt-BR" to "pt_BR", etc.
    $localLangDir = uv run python .github/scripts/langCodes.py $langCode
    
    Write-Host "--- Processing Language: $langCode (Mapped to local folder: $localLangDir) ---"

    # Remote paths (files exported from Crowdin)
    $remoteMd = Join-Path $dir.FullName "$addonId.md"
    $remoteXliff = Join-Path $dir.FullName "$addonId.xliff"
    $remotePo = Join-Path $dir.FullName "$addonId.po"

    # Local paths (mapped to the standard NVDA language directory structure)
    $localMdDir = "addon/doc/$localLangDir"
    $localMd = "$localMdDir/readme.md"
    $localPoPath = "addon/locale/$localLangDir/LC_MESSAGES/nvda.po"

    # --- 3.1 PO FILE PROCESSING (Interface) ---
    $poImported = $false
    if (Test-Path $remotePo) {
        # API check using the Crowdin language code ($langCode)
        uv run python .github/scripts/checkTranslation.py "$addonId.po" $langCode
        if ($LASTEXITCODE -eq 0) {
            Write-Host "Action: Remote PO is valid. Importing to local folder: $localLangDir"
            New-Item -ItemType Directory -Force -Path (Split-Path $localPoPath) | Out-Null
            Move-Item $remotePo $localPoPath -Force
            $poImported = $true
        }
    }

    # Fallback: If Crowdin export is missing or poor quality, upload local legacy file to Crowdin
    if (-not $poImported -and (Test-Path $localPoPath)) {
        Write-Host "Action: Remote PO poor/missing. Uploading local legacy PO ($localLangDir) to Crowdin ($langCode)..."
        ./l10nUtil.exe uploadTranslationFile $langCode "$addonId.po" $localPoPath -c addon
    }

    # --- 3.2 DOCUMENTATION PROCESSING (Markdown) ---
    $scoreMd = 0.0
    $scoreXliff = 0.0

    if (Test-Path $remoteMd) {
        $res = uv run python .github/scripts/checkTranslation.py "$addonId.md" $langCode
        $scoreMd = [double]($res | Select-String "mdScore=").ToString().Split("=")[1]
    }
    if (Test-Path $remoteXliff) {
        $res = uv run python .github/scripts/checkTranslation.py "$addonId.xliff" $langCode
        $scoreXliff = [double]($res | Select-String "translationRatio=").ToString().Split("=")[1]
    }

    $threshold = 0.5
    $docImported = $false

    if ($scoreXliff -gt $threshold -or $scoreMd -gt $threshold) {
        if (!(Test-Path $localMdDir)) { New-Item -ItemType Directory -Force -Path $localMdDir | Out-Null }

        if ($scoreXliff -ge $scoreMd) {
            Write-Host "Action: Converting Remote XLIFF to local MD ($localLangDir)"
            ./l10nUtil.exe xliff2md $remoteXliff $localMd
            $docImported = $true
        } else {
            Write-Host "Action: Importing Remote MD to local ($localLangDir)"
            Move-Item $remoteMd $localMd -Force
            $docImported = $true
        }
    }

    # Fallback: Upload local MD to Crowdin if remote documentation is poor
    if (-not $docImported -and (Test-Path $localMd)) {
        Write-Host "Action: Remote documentation poor. Uploading local MD ($localLangDir) to Crowdin ($langCode)..."
        ./l10nUtil.exe uploadTranslationFile $langCode "$addonId.md" $localMd -c addon
    }
}

# --- STEP 4: COMMIT UPDATED TRANSLATIONS ---

git add addon/locale addon/doc
git diff --staged --quiet
if ($LASTEXITCODE -ne 0) {
    git commit -m "Update translations for $addonId from Crowdin (Automatic Sync)"
    $branch = $env:downloadTranslationsBranch
    git push -f origin "HEAD:$branch"
} else {
    Write-Host "No changes in translations to commit."
}
