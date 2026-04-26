#!/usr/bin/env pwsh
$ErrorActionPreference = 'Stop'

# Config git
git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"

# Update xliff file
$xliffFile = "./$addonId.xliff"
$mdFile = "./readme.md"
if (Test-Path $mdFile) {
    if (Test-Path $xliffFile) {
        $tempXliff = [System.IO.Path]::GetTempFileName()
        Copy-Item "$addonId.xliff" $tempXliff -Force
        Write-Host "Copied $addonId.xliff to temporary file: $tempXliff"
        uv run .github/scripts/markdownTranslate.py updateXliff -m $mdFile -x $tempXliff -o $xliffFile
        Write-Host "Updated $xliffFile based on $mdFile"
    } else {
        Write-Host "XLIFF file not found, but readme.md exists. Creating an XLIFF template for translations."
        uv run .github/scripts/markdownTranslate.py generateXliff -m $mdFile -o $xliffFile
    }
} else {
    Write-Host "readme.md not found. Skipping XLIFF generation."
}

# Update pot file in Crowdin
uv run scons pot
$potFile = "$addonId.pot"
if (Test-Path $potFile) {
    Write-Host "Uploading updated POT to Crowdin..."
    ./l10nUtil.exe uploadSourceFile "$potFile" -c addon
} else {
    Write-Host "POT file not found, skipping POT update."
}

# Update xliff file in Crowdin
if (Test-Path $xliffFile) {
    Write-Host "Uploading XLIFF to Crowdin..."
    ./l10nUtil.exe uploadSourceFile "$xliffFile" -c addon
    git add "$xliffFile"
    git diff --staged --quiet
    if ($LASTEXITCODE -ne 0) {
        git commit -m "Update $xliffFile for $addonId"
        git push
      } else {
        Write-Host "No changes to $xliffFile, skipping commit."
    }
} else {
    Write-Host "XLIFF file not found, skipping XLIFF upload."
}

# Export translations
Write-Host "Exporting translations from Crowdin..."
./l10nUtil.exe exportTranslations -o _addonL10n -c addon

# Ensure base directories exist
New-Item -ItemType Directory -Force -Path addon/locale | Out-Null
New-Item -ItemType Directory -Force -Path addon/doc | Out-Null

$addonId = $env:ADDON_ID.Trim()
if (-not $addonId) {
    Write-Error "Failed to get addon ID."
    exit 1
}

foreach ($dir in Get-ChildItem -Path "_addonL10n/$addonId" -Directory) {
    $langCode = $dir.Name
    $langShort = $langCode.Split('_')[0]

    if ($langCode -eq "en") { continue }

    Write-Host "--- Processing: $addonId ($langCode) ---"

    # Temporary files from Crowdin
    $remoteMd = Join-Path $dir.FullName "$addonId.md"
    $remoteXliff = Join-Path $dir.FullName "$addonId.xliff"
    $remotePo = Join-Path $dir.FullName "$addonId.po"

    # Local paths
    $localMdDir = "addon/doc/$langCode"
    $localMd = "$localMdDir/readme.md"
    $localPoPath = "addon/locale/$langCode/LC_MESSAGES/nvda.po"

    # 1. PO PROCESSING
    if (Test-Path $remotePo) {
        uv run python .github/scripts/checkTranslation.py "$addonId.po" $langShort
        if ($LASTEXITCODE -eq 0) {
            New-Item -ItemType Directory -Force -Path (Split-Path $localPoPath) | Out-Null
            Move-Item $remotePo $localPoPath -Force
        }
    }

    # 2. EVALUATION VIA API
    $scoreMd = 0.0
    $scoreXliff = 0.0

    if (Test-Path $remoteMd) {
        $res = uv run python .github/scripts/checkTranslation.py "$addonId.md" $langShort
        $scoreMd = [double]($res | Select-String "mdScore=").ToString().Split("=")[1]
    }

    if (Test-Path $remoteXliff) {
        $res = uv run python .github/scripts/checkTranslation.py "$addonId.xliff" $langShort
        $scoreXliff = [double]($res | Select-String "translationRatio=").ToString().Split("=")[1]
    }

    Write-Host "Scores -> MD: $scoreMd | XLIFF: $scoreXliff"

    # 3. DECISION LOGIC
    $threshold = 0.5
    $imported = $false

    if ($scoreXliff -gt $threshold -or $scoreMd -gt $threshold) {
        # Create doc directory if needed
        if (!(Test-Path $localMdDir)) { New-Item -ItemType Directory -Force -Path $localMdDir | Out-Null }

        if ($scoreXliff -ge $scoreMd) {
            Write-Host "Action: Converting XLIFF to local MD"
            ./l10nUtil.exe xliff2md $remoteXliff $localMd
            $imported = $true
        } else {
            Write-Host "Action: Importing Remote MD to local"
            Move-Item $remoteMd $localMd -Force
            $imported = $true
        }
    }

    # 4. FALLBACK: Upload local if remote is poor
    if (-not $imported -and (Test-Path $localMd)) {
        Write-Host "Action: Remote quality too low. Uploading local MD to Crowdin..."
        ./l10nUtil.exe uploadTranslationFile $langCode "$addonId.md" $localMd -c addon
    }
}

git add addon/locale addon/doc
git diff --staged --quiet
if ($LASTEXITCODE -ne 0) {
    git commit -m "Update translations for $addonId from Crowdin"
    $branch = $env:downloadTranslationsBranch
    git push -f origin "HEAD:$branch"
}
