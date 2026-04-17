# merge-levelup.ps1 - Unified AI Toolkit Knowledge Consolidation
# Version: 1.0.0

$ErrorActionPreference = "Stop"

Write-Host "Merging learned knowledge from level-up/ archive..." -ForegroundColor Cyan

$Source = "level-up/output/shared"
$Dest = "shared"

if (-Not (Test-Path $Source)) {
    Write-Warning "No new knowledge found in $Source. Skipping merge."
    exit 0
}

# 1. Merge Skills
if (Test-Path (Join-Path $Source "skills")) {
    Write-Host "Merging new Skills..."
    Copy-Item -Path (Join-Path $Source "skills\*") -Destination (Join-Path $Dest "skills") -Recurse -Force -ErrorAction Continue
}

# 2. Merge Agents
if (Test-Path (Join-Path $Source "agents")) {
    Write-Host "Merging new Agents..."
    Copy-Item -Path (Join-Path $Source "agents\*") -Destination (Join-Path $Dest "agents") -Recurse -Force -ErrorAction Continue
}

# 3. Merge rules
if (Test-Path (Join-Path $Source "rules")) {
    Write-Host "Merging new Rules..."
    Copy-Item -Path (Join-Path $Source "rules\*") -Destination (Join-Path $Dest "rules") -Recurse -Force -ErrorAction Continue
}

Write-Host "Merge complete. Triggering global synchronization..." -ForegroundColor Green

# 4. Global Sync
if (Test-Path "./scripts/sync_all.ps1") {
    powershell -ExecutionPolicy Bypass -File ./scripts/sync_all.ps1
}

Write-Host "Your Toolkit has successfully 'Leveled Up'!" -ForegroundColor Green
