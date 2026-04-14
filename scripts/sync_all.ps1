# sync_all.ps1 - Unified AI Toolkit Sync Engine
# Version: 1.1 (Unification Fix)

$ErrorActionPreference = "Continue"

Write-Host "Starting Sync..." -ForegroundColor Cyan

# 1. Sync Skills
$Source = "shared/skills"
$Destinations = @(".agent/skills", ".github/skills", "output/shared/skills")

if (Test-Path $Source) {
    foreach ($Dest in $Destinations) {
        Write-Host "Syncing Skills to: $Dest"
        if (!(Test-Path $Dest)) { New-Item -ItemType Directory -Path $Dest -Force | Out-Null }
        Copy-Item -Path "$Source\*" -Destination $Dest -Recurse -Force
    }
}

# 2. Sync Agents & Workflows
$SourceAgents = "shared/agents"
$DestAgents = @(".agent/agents", "output/shared/agents")

if (Test-Path $SourceAgents) {
    foreach ($Target in $DestAgents) {
        Write-Host "Syncing Agents to: $Target"
        if (!(Test-Path $Target)) { New-Item -ItemType Directory -Path $Target -Force | Out-Null }
        Copy-Item -Path "$SourceAgents\*" -Destination $Target -Recurse -Force
    }
}

$SourceWorkflows = "shared/workflows"
$DestWorkflows = @(".agent/workflows", ".github/workflows", "output/shared/workflows")

if (Test-Path $SourceWorkflows) {
    foreach ($Target in $DestWorkflows) {
        Write-Host "Syncing Workflows to: $Target"
        if (!(Test-Path $Target)) { New-Item -ItemType Directory -Path $Target -Force | Out-Null }
        Copy-Item -Path "$SourceWorkflows\*" -Destination $Target -Recurse -Force
    }
}

Write-Host "Sync complete!" -ForegroundColor Green
