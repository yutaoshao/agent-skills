# De-AI Style Checker for academic papers (PowerShell)
# Usage: powershell -ExecutionPolicy Bypass -File scripts/style_check.ps1 -FilePath <file>

param(
    [Parameter(Mandatory=$true)]
    [string]$FilePath
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $FilePath)) {
    Write-Error "File not found: $FilePath"
    exit 1
}

$content = Get-Content $FilePath -Raw
$lines = Get-Content $FilePath
$issues = 0

Write-Host "=== De-AI Style Check: $FilePath ===" -ForegroundColor Cyan

Write-Host "`n[1] Bold-label paragraph openers:" -ForegroundColor Yellow
$found = $false
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match '\\textbf\{[^}]+\}\.' -or $lines[$i] -match '^\*\*[^*]+\*\*[.:]') {
        Write-Host "  Line $($i+1): $($lines[$i])"
        $found = $true
    }
}
if ($found) { $issues++ } else { Write-Host "  OK" }

Write-Host "`n[2] High-frequency AI transition words (EN):" -ForegroundColor Yellow
$found = $false
$pattern = '^\s*(Furthermore|Moreover|Additionally|Notably|Importantly|Interestingly|Crucially|Specifically|Consequently|Nevertheless)[,.]'
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match $pattern) {
        Write-Host "  Line $($i+1): $($lines[$i])"
        $found = $true
    }
}
if ($found) { $issues++ } else { Write-Host "  OK" }

Write-Host "`n[3] Filler phrases (EN):" -ForegroundColor Yellow
$found = $false
$fillers = @('It is worth noting that', 'It should be noted that', 'plays a crucial role', 'state-of-the-art', 'a wide range of', 'in a comprehensive manner')
for ($i = 0; $i -lt $lines.Count; $i++) {
    foreach ($filler in $fillers) {
        if ($lines[$i] -match [regex]::Escape($filler)) {
            Write-Host "  Line $($i+1): $($lines[$i])"
            $found = $true
            break
        }
    }
}
if ($found) { $issues++ } else { Write-Host "  OK" }

Write-Host "`n[4] Overused AI vocabulary (EN):" -ForegroundColor Yellow
$found = $false
$aiWords = @('leverage', 'utilize', 'harness', 'delve', 'paradigm', 'seamless', 'landscape', 'plethora', 'synergy', 'holistic', 'elucidate', 'pivotal', 'myriad')
for ($i = 0; $i -lt $lines.Count; $i++) {
    foreach ($word in $aiWords) {
        if ($lines[$i] -match "\b$word") {
            Write-Host "  Line $($i+1): $($lines[$i])"
            $found = $true
            break
        }
    }
}
if ($found) { $issues++ } else { Write-Host "  OK" }

Write-Host "`n[5] Banned Chinese transitions:" -ForegroundColor Yellow
$found = $false
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match '首先|其次|最后|此外|另外|接下来|值得注意的是|需要指出的是') {
        Write-Host "  Line $($i+1): $($lines[$i])"
        $found = $true
    }
}
if ($found) { $issues++ } else { Write-Host "  OK" }

Write-Host "`n[6] Subjective first-person phrases:" -ForegroundColor Yellow
$found = $false
for ($i = 0; $i -lt $lines.Count; $i++) {
    if ($lines[$i] -match '我认为|我觉得|我个人|in my opinion|I believe') {
        Write-Host "  Line $($i+1): $($lines[$i])"
        $found = $true
    }
}
if ($found) { $issues++ } else { Write-Host "  OK" }

Write-Host "`n=== Summary: $issues category/categories flagged ===" -ForegroundColor Cyan
if ($issues -eq 0) {
    Write-Host "Paper passes de-AI style check." -ForegroundColor Green
} else {
    Write-Host "Review flagged items above." -ForegroundColor Red
}
