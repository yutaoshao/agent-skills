# PowerShell: Initialize plan/ directory from plan-template/
# Usage: powershell -ExecutionPolicy Bypass -File scripts/init_plan.ps1 [-ProjectDir .]

param(
    [string]$ProjectDir = "."
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$SkillDir = Split-Path -Parent $ScriptDir
$TemplateDir = Join-Path $SkillDir "plan-template"

$PlanDir = Join-Path $ProjectDir "plan"

if (-not (Test-Path $TemplateDir)) {
    Write-Error "Error: plan-template/ not found at $TemplateDir"
    exit 1
}

if (-not (Test-Path $PlanDir)) {
    New-Item -ItemType Directory -Path $PlanDir -Force | Out-Null
}

Get-ChildItem -Path $TemplateDir -Filter "*.md" | ForEach-Object {
    $target = Join-Path $PlanDir $_.Name
    if (Test-Path $target) {
        Write-Host "Skip (exists): $target"
    } else {
        Copy-Item $_.FullName $target
        Write-Host "Created: $target"
    }
}

Write-Host "Done. plan/ initialized at $PlanDir"
