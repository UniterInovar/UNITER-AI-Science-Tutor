# Convenience script to run basic project checks from project root
# Usage: Open PowerShell at project root and run: .\scripts\run_checks.ps1

# Ensure we are in project root
$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $projectRoot

# Use local virtualenv python if available
$venvPython = Join-Path $projectRoot '.venv\Scripts\python.exe'
if (-Not (Test-Path $venvPython)) {
    Write-Output "Virtualenv python not found at $venvPython. Activate or create a .venv first."
    exit 1
}

# Set PYTHONPATH so imports work when running scripts directly
$env:PYTHONPATH = $projectRoot
$env:PYTHONIOENCODING = 'utf-8'

Write-Output "Running backend example/test scripts..."
& $venvPython '.\backend\tests\test_topic_matcher.py'
$lastExit = $?
& $venvPython '.\backend\tests\test_tutor.py'
if (-not $lastExit) { Write-Output 'One or more tests may have failed.' }
else { Write-Output 'Example scripts completed.' }
