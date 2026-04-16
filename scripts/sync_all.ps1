# sync_all.ps1 - Unified AI Toolkit Sync Engine
# Version: 1.2.1 (Stability Fix)

$ErrorActionPreference = "Continue"

Write-Host "Starting Comprehensive Sync (v1.2.1)..." -ForegroundColor Cyan

# --- FUNCTION: Mirror-Directory ---
function Mirror-Directory($src, $dest) {
    if (!(Test-Path $src)) { return }
    if (!(Test-Path $dest)) { New-Item -ItemType Directory -Path $dest -Force | Out-Null }
    
    $exclude = @("*.db-wal", "*.db-shm", "*.sqlite", "*.vsidx", ".DS_Store", "Thumbs.db")
    
    Write-Host "Mirroring: $src -> $dest"
    
    # 1. Copy new/updated files
    Copy-Item -Path "$src\*" -Destination $dest -Recurse -Force -Exclude $exclude
    
    # 2. Cleanup orphan files in destination
    $srcFiles = Get-ChildItem -Path $src -Recurse | Select-Object -ExpandProperty Name
    $destFiles = Get-ChildItem -Path $dest -Recurse | Select-Object -ExpandProperty Name
    
    foreach ($file in $destFiles) {
        if ($srcFiles -notcontains $file) {
            $targetPath = Join-Path $dest $file
            if (Test-Path $targetPath) {
                Remove-Item -Path $targetPath -Recurse -Force | Out-Null
                Write-Host "Removed orphan: $file" -ForegroundColor Yellow
            }
        }
    }
}

# --- PHASE 1: SSoT Distribution ---
Write-Host "PHASE 1: SSoT Distribution"

# Sync Skills
$Source = "shared/skills"
$Destinations = @(".agent/skills", ".github/skills")
foreach ($Dest in $Destinations) {
    if (Test-Path $Source) {
        if (!(Test-Path $Dest)) { New-Item -ItemType Directory -Path $Dest -Force | Out-Null }
        Copy-Item -Path "$Source\*" -Destination $Dest -Recurse -Force
    }
}

# Sync Agents & Workflows
if (Test-Path "shared/agents") {
    Copy-Item -Path "shared/agents\*" -Destination ".agent/agents" -Recurse -Force
}
if (Test-Path "shared/workflows") {
    Copy-Item -Path "shared/workflows\*" -Destination ".agent/workflows" -Recurse -Force
    Copy-Item -Path "shared/workflows\*" -Destination ".github/workflows" -Recurse -Force
}

# --- PHASE 2: Staging Mirror ---
Write-Host "PHASE 2: Staging Mirror"

$MirrorList = @(
    @{ src = ".agent"; dest = "output/.agent" },
    @{ src = ".github"; dest = "output/.github" },
    @{ src = ".cursor"; dest = "output/.cursor" },
    @{ src = ".kiro"; dest = "output/.kiro" },
    @{ src = ".opencode"; dest = "output/.opencode" },
    @{ src = ".vs"; dest = "output/.vs" },
    @{ src = "shared"; dest = "output/shared" }
)

foreach ($entry in $MirrorList) {
    Mirror-Directory $entry.src $entry.dest
}

Write-Host "Sync and Mirror complete!" -ForegroundColor Green
