# /clone-source — Clone & Evaluate a New Source Repo

> **Trigger**: `/clone-source <github-url>`
> **Skill**: `source-manager`
> **Purpose**: Clone a new repo into `sources/`, evaluate its value, and integrate into `shared/` if positive — then register it in `sources/link.md`.

---

## When to Use

Use this workflow when you want to:
- Discover a new AI toolkit, skills library, or agent collection on GitHub
- Evaluate it against your current toolkit before committing to integrate
- Get a structured report before making integration decisions

**Example:**
```
/clone-source https://github.com/username/awesome-ai-skills
```

---

## Pre-flight Checks

- [ ] A valid GitHub URL is provided as argument
- [ ] The repo name extracted from URL does NOT already exist in `sources/<name>/`
- [ ] Git is available

If the repo already exists in `sources/`, suggest running `/update-sources` instead.

---

## Execution Steps

### Step 1: Parse Input

Extract from the URL:
- `repo-name`: last segment of URL (e.g., `awesome-ai-skills` from `https://github.com/user/awesome-ai-skills`)
- `clone-url`: the full URL provided

Validate:
- URL starts with `https://github.com/` or `git@github.com:`
- `repo-name` doesn't already exist in `sources/`

### Step 2: Clone

```powershell
git clone <url> "sources/<repo-name>"
```

**Handle errors:**
- If clone fails → Report error, STOP workflow.
- If repo is empty → Report "Empty repo", STOP workflow.

### Step 3: Clean Build Artifacts

Apply cleanup protocol from `source-manager` skill immediately after clone:
- Remove: `dist/`, `build/`, `.next/`, `node_modules/`, `bin/`, `obj/`, `target/`, `__pycache__/`, `.venv/`, `venv/`, etc.

Log: "Cleaned X MB of build artifacts"

### Step 4: Discover Content

Inventory what the repo contains. Scan for:

```powershell
# Find skill definitions
Get-ChildItem "sources/<name>" -Recurse -Filter "SKILL.md"

# Find agent definitions
Get-ChildItem "sources/<name>" -Recurse -Filter "*.md" | 
    Where-Object { $_.DirectoryName -match "agent" }

# Find workflow definitions
Get-ChildItem "sources/<name>" -Recurse -Filter "*.md" |
    Where-Object { $_.DirectoryName -match "workflow" }

# Find rules/templates
Get-ChildItem "sources/<name>" -Recurse -Include "RULES.md","*.rules","GEMINI.md","CLAUDE.md","AGENTS.md"
```

Build an inventory table:
```markdown
| Type | Name | Path |
|------|------|------|
| Skill | web-scraper | skills/web-scraper/SKILL.md |
| Agent | data-analyst | agents/data-analyst.md |
```

### Step 5: Evaluate

Using the **Evaluation Criteria** from `source-manager` skill:

For each discovered item, check against `shared/`:
- Already exists? → Mark as duplicate (score penalty)
- New & relevant? → Mark as candidate (score bonus)
- Conflicts with existing patterns? → Mark as conflict (score penalty)

Calculate total score → determine verdict.

**Additionally, for new repos, assess:**
- **Maintenance**: Last commit date (active = +1, abandoned >2 years = -1)
- **Stars/popularity**: Not mandatory but notable if known
- **Documentation quality**: Has README + SKILL.md structure = +1

### Step 6a: POSITIVE Verdict (score ≥ 5)

1. Integrate content into `shared/` (following integration protocol)
2. Register in `sources/link.md`:
   ```powershell
   Add-Content "sources/link.md" "<repo-name>: <url>"
   ```
3. Log all integrated items

### Step 6b: MARGINAL Verdict (score 1–4)

1. Do NOT auto-integrate
2. Keep in `sources/<name>/` for reference
3. Do NOT add to `link.md` (not tracked for auto-updates)
4. Report: "Manual review recommended — see details"

### Step 6c: NEGATIVE Verdict (score ≤ 0)

1. Do NOT integrate
2. Keep folder in `sources/<name>/` for reference (user may want to explore manually)
3. Do NOT add to `link.md`
4. Report: "Not integrated — reasons listed below"

### Step 7: Generate Report

Save to: `sources/reports/YYYY-MM-DD_clone-<repo-name>.md`

Follow the report template from `source-manager` skill.

Include:
- Clone result (success/fail)
- Artifact cleanup summary (size freed)
- Full inventory of discovered content
- Score breakdown with reasoning
- Verdict and action taken
- List of integrated files (if any)

### Step 8: Run Sync (if integrated)

If verdict = POSITIVE and items were integrated:
```powershell
powershell -ExecutionPolicy Bypass -File scripts/sync_all.ps1
```

### Step 9: Final Output

Present a concise summary:

```markdown
## /clone-source — Result

**Repo**: `<repo-name>`
**URL**: <url>
**Verdict**: ✅ POSITIVE / ⚠️ MARGINAL / ❌ NEGATIVE
**Score**: X points

**Action taken**:
- Integrated X skills, Y agents, Z workflows into `shared/`
- Registered in `sources/link.md` (will be included in future `/update-sources`)
- Report saved: `sources/reports/YYYY-MM-DD_clone-<name>.md`

**Top integrated items**:
- `shared/skills/new-skill/` — Description
- `shared/agents/new-agent.md` — Description
```

---

## Notes

- **Never force-overwrite** existing `shared/` content.
- The `sources/<name>/` folder is kept regardless of verdict — it's your local cache.
- If you later decide to remove a rejected source: `Remove-Item -Recurse "sources/<name>"`.
- Re-run evaluation anytime by manually triggering the evaluation steps with the skill.
