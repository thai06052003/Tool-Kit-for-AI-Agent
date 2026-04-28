---
name: source-manager
description: >
  Manages external AI toolkit source repositories. Handles pulling updates,
  cloning new repos, cleaning build artifacts, evaluating integration impact,
  and generating detailed reports. Use when updating sources or evaluating
  a new repo for integration into the Unified AI Toolkit.
triggers:
  - /update-sources
  - /clone-source
---

# Source Manager Skill

> **Purpose**: Automate the lifecycle of external AI toolkit sources — from fetching to evaluation to selective integration.

---

## 📁 Directory Structure

```
Tool-Kit-for-AI-Agent/
├── sources/
│   ├── link.md                    ← Registry of tracked repos (name: URL)
│   ├── <repo-name>/               ← Cloned repo directories
│   └── reports/                   ← Auto-generated integration reports
│       └── YYYY-MM-DD_<name>.md
└── shared/                        ← Integration target (SSoT)
    ├── skills/
    ├── agents/
    ├── workflows/
    ├── rules/
    └── templates/
```

---

## 🧹 Phase 1: Cleanup Protocol

After pulling or cloning, ALWAYS remove these before evaluation:

### Frontend Build Artifacts
```powershell
# Directories to delete
$FE_DIRS = @("dist", "build", ".next", ".nuxt", "out", ".output", ".vercel", "public/build", ".cache", "storybook-static")

# Files to delete
$FE_FILES = @("*.bundle.js", "*.chunk.js", "*.map")
```

### Backend Build Artifacts
```powershell
# Directories to delete
$BE_DIRS = @("bin", "obj", "target", "__pycache__", ".pytest_cache", "node_modules", ".venv", "venv", "env", "vendor", "*.egg-info", ".eggs", "htmlcov", ".coverage")
```

### General Clutter
```powershell
$CLUTTER = @(".DS_Store", "Thumbs.db", "*.log", "*.tmp", "*.bak")
```

**PowerShell cleanup command:**
```powershell
function Remove-BuildArtifacts {
    param([string]$RepoPath)
    
    $dirsToRemove = @("dist","build",".next",".nuxt","out",".output","bin","obj","target","__pycache__",".pytest_cache","node_modules",".venv","venv","env","htmlcov",".cache","storybook-static")
    
    foreach ($dir in $dirsToRemove) {
        Get-ChildItem -Path $RepoPath -Directory -Recurse -Filter $dir -ErrorAction SilentlyContinue |
            Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
    }
    
    # Remove loose files
    Get-ChildItem -Path $RepoPath -File -Recurse -Include "*.log","*.tmp","*.bak",".DS_Store" -ErrorAction SilentlyContinue |
        Remove-Item -Force -ErrorAction SilentlyContinue
}
```

---

## 🔍 Phase 2: Discovery & Diff Analysis

### For UPDATE workflow (existing repo):
```powershell
# View changes since last pull
git -C "sources/<name>" log --oneline -10
git -C "sources/<name>" diff HEAD~1 --name-only
git -C "sources/<name>" diff HEAD~1 --stat
```

### For CLONE workflow (new repo):
```powershell
# Inventory what the repo contains
Get-ChildItem -Path "sources/<name>" -Recurse -File | 
    Select-Object Extension | 
    Group-Object Extension | 
    Sort-Object Count -Descending
```

**Key discovery questions:**
1. Does it contain `skills/` or `SKILL.md` files? → Candidate skills
2. Does it contain `agents/` or agent `.md` files? → Candidate agents
3. Does it contain `workflows/` or workflow `.md` files? → Candidate workflows
4. Does it contain `rules/`, `templates/`, `prompts/`? → Candidate rules/templates
5. What is the main tech domain? (AI, DevOps, Frontend, Backend...)

---

## ⚖️ Phase 3: Evaluation Criteria

### Scoring Matrix

| Criterion | Score | Description |
|-----------|-------|-------------|
| **New Skills** | +3 each | Skills NOT in `shared/skills/` |
| **Enhanced Skills** | +2 each | Skills that significantly improve existing ones |
| **New Agents** | +3 each | Agents covering new domains |
| **New Workflows** | +2 each | Useful workflow additions |
| **New Rules/Templates** | +1 each | Quality rules or templates |
| **Duplicate content** | -2 each | Exact duplicates of existing content |
| **Conflicts** | -3 each | Content that conflicts with existing patterns |
| **Low quality** | -2 each | No docs, unclear purpose, broken structure |

### Verdict Thresholds

| Total Score | Verdict | Action |
|-------------|---------|--------|
| ≥ 5 | ✅ **POSITIVE** | Integrate into `shared/` |
| 1–4 | ⚠️ **MARGINAL** | Ask user for manual decision |
| ≤ 0 | ❌ **NEGATIVE** | Do NOT integrate, keep in `sources/` only |

---

## 🔗 Phase 4: Integration Protocol (POSITIVE only)

When verdict is POSITIVE:

### Step 1: Identify what to copy
```
sources/<name>/skills/   → shared/skills/      (each skill subfolder)
sources/<name>/agents/   → shared/agents/      (each agent .md file)
sources/<name>/workflows/→ shared/workflows/   (each workflow .md file)
sources/<name>/rules/    → shared/rules/       (rule files)
sources/<name>/templates/→ shared/templates/   (template files)
```

### Step 2: Conflict resolution
- If a file with the same name exists in `shared/`: **SKIP** (do not overwrite)
- Log skipped files in the report under "Skipped (conflict)"

### Step 3: Copy command
```powershell
function Integrate-RepoContent {
    param([string]$RepoPath, [string]$SharedPath)
    
    $mappings = @{
        "skills"    = "skills"
        "agents"    = "agents"
        "workflows" = "workflows"
        "rules"     = "rules"
        "templates" = "templates"
    }
    
    $integrated = @()
    $skipped = @()
    
    foreach ($src in $mappings.Keys) {
        $srcDir = Join-Path $RepoPath $src
        $dstDir = Join-Path $SharedPath $mappings[$src]
        
        if (Test-Path $srcDir) {
            Get-ChildItem $srcDir -Recurse | foreach {
                $dst = $_.FullName.Replace($srcDir, $dstDir)
                if (-not (Test-Path $dst)) {
                    Copy-Item $_.FullName $dst -Force
                    $integrated += $_.Name
                } else {
                    $skipped += $_.Name
                }
            }
        }
    }
    
    return @{ Integrated = $integrated; Skipped = $skipped }
}
```

### Step 4: For CLONE workflow — update link.md
```powershell
# Append to sources/link.md
Add-Content -Path "sources/link.md" -Value "`n<repo-name>: <url>"
```

---

## 📄 Phase 5: Report Template

Save report to: `sources/reports/YYYY-MM-DD_<repo-name>.md`

```markdown
# Source Report: <repo-name>
**Date**: YYYY-MM-DD HH:MM
**Mode**: UPDATE | CLONE
**URL**: <repo-url>

---

## 📊 Summary

| Field | Value |
|-------|-------|
| Verdict | ✅ POSITIVE / ⚠️ MARGINAL / ❌ NEGATIVE |
| Score | X points |
| Skills Found | N |
| Agents Found | N |
| Workflows Found | N |
| Files Integrated | N |
| Files Skipped | N |

---

## 🔍 Changes Detected

### Modified Files (UPDATE mode)
- `path/to/file.md` — description of change

### New Content Found
| Type | Name | Description |
|------|------|-------------|
| Skill | skill-name | What it does |
| Agent | agent-name | What domain |
| Workflow | /workflow-name | What it triggers |

---

## ⚖️ Evaluation

### Positive Factors
- [ ] +N: <reason>

### Negative Factors
- [ ] -N: <reason>

**Total Score: X** → Verdict: ✅/⚠️/❌

---

## 🔗 Integration Result

### Integrated
- `shared/skills/skill-name/SKILL.md`
- `shared/agents/agent-name.md`

### Skipped (conflict)
- `skill-name` — already exists in shared/skills/

### NOT Integrated (negative verdict)
> Repo kept in `sources/<name>/` for reference only.

---

## 💡 Recommendations

1. <Specific action item>
2. <Specific action item>
```

---

## ⚡ Quick Reference Commands

```powershell
# Pull all sources
Get-Content "sources/link.md" | foreach {
    if ($_ -match "^(\S+):\s+(.+)$") {
        $name = $matches[1]; $url = $matches[2]
        git -C "sources/$name" pull origin main 2>&1
    }
}

# Clone new repo
git clone <url> "sources/<name>"

# Run sync after integration
powershell -ExecutionPolicy Bypass -File scripts/sync_all.ps1
```
