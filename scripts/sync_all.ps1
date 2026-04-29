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
$Destinations = @(".agent/skills", ".github/skills", ".cursor/skills", ".kiro/skills")
foreach ($Dest in $Destinations) {
    Mirror-Directory $Source $Dest
}

# Sync Agents
if (Test-Path "shared/agents") {
    Mirror-Directory "shared/agents" ".agent/agents"
    Mirror-Directory "shared/agents" ".kiro/agents"
}

# Sync Workflows
if (Test-Path "shared/workflows") {
    Mirror-Directory "shared/workflows" ".agent/workflows"
}

# Sync Design Templates
if (Test-Path "shared/templates/design") {
    $SourceTemplate = "shared/templates/design"
    $DestinationsTemplate = @(".agent/templates/design", ".github/templates/design", ".cursor/templates/design", ".kiro/templates/design")
    foreach ($Dest in $DestinationsTemplate) {
        Mirror-Directory $SourceTemplate $Dest
    }
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

# --- PHASE 3: Root Files Synchronization ---
Write-Host "PHASE 3: Root Files Synchronization"

$RootFiles = @(
    "README.md",
    "GEMINI.md",
    "AGENTS.md",
    "PLAN_UPDATE.md",
    ".cursorrules",
    "hermes-config.yaml.example",
    "user-manual-claud-mem.md"
)

foreach ($file in $RootFiles) {
    if (Test-Path $file) {
        Copy-Item -Path $file -Destination "output/" -Force
        Write-Host "Copied root file: $file"
    }
}

$RootFolders = @(
    "docs",
    "level-up",
    ".vscode"
)

foreach ($folder in $RootFolders) {
    if (Test-Path $folder) {
        Mirror-Directory $folder "output/$folder"
    }
}

Write-Host "Sync and Mirror complete!" -ForegroundColor Green
