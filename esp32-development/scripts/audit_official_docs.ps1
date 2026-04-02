param(
    [string]$Root = "."
)

$ErrorActionPreference = "Stop"

$rootPath = (Resolve-Path $Root).Path
$skillFile = Join-Path $rootPath "SKILL.md"
$referencesDir = Join-Path $rootPath "references"

$targets = @()
if (Test-Path $skillFile) {
    $targets += $skillFile
} else {
    Write-Error "Missing file: $skillFile"
}

if (Test-Path $referencesDir) {
    $targets += Get-ChildItem $referencesDir -Filter *.md | ForEach-Object { $_.FullName }
} else {
    Write-Error "Missing directory: $referencesDir"
}

$errors = New-Object System.Collections.Generic.List[string]
$urlPattern = 'https?://[^\s\)>"'']+'

foreach ($file in $targets) {
    $content = Get-Content -Encoding utf8 $file -Raw

    if ((Split-Path $file -Parent | Split-Path -Leaf) -eq "references" -and $content -notmatch 'Official docs:') {
        $errors.Add("${file}: missing 'Official docs:' section")
    }

    $matches = [regex]::Matches($content, $urlPattern)
    foreach ($match in $matches) {
        $url = $match.Value
        if ($url -match 'espressif' -and $url -notmatch '^https://docs\.espressif\.com/') {
            $errors.Add("${file}: non-official Espressif docs host -> $url")
        }
    }
}

if ($errors.Count -gt 0) {
    Write-Host "Audit failed:"
    foreach ($errorLine in $errors) {
        Write-Host "- $errorLine"
    }
    exit 1
}

Write-Host "Audit passed: official-doc sections and hosts look valid."
