# /update-sources — Update All Tracked Sources

> **Trigger**: `/update-sources`
> **Skill**: `source-manager`
> **Purpose**: Pull latest changes from all repos in `sources/link.md`, evaluate each change, and integrate improvements into `shared/` if positive.

---

## When to Use

Use this workflow when you want to:
- Sync your toolkit with the latest upstream improvements
- Check if any tracked source repos have new skills, agents, or workflows worth integrating
- Get a comprehensive report of what changed and what was integrated

---

## Pre-flight Checks

Before starting, verify:
- [ ] `sources/link.md` exists and has at least 1 entry
- [ ] All repos in `sources/link.md` have been cloned to `sources/<name>/`
- [ ] Git is available (`git --version`)

If a repo folder doesn't exist yet, run `git clone <url> sources/<name>` for it first, then re-run this workflow.

---

## Execution Steps

### Step 1: Read Registry

Read `sources/link.md` line by line. Format:
```
<repo-name>: <github-url>
```

Skip empty lines and comments (`#`).

### Step 2: For Each Repo — Pull

```powershell
# For each repo in link.md:
git -C "sources/<name>" fetch origin
git -C "sources/<name>" pull origin HEAD
```

**Handle errors:**
- If `git pull` fails (merge conflict, network error) → Log as `PULL_FAILED`, skip to next repo, continue.
- If directory doesn't exist → Log as `NOT_CLONED`, skip.

### Step 3: Capture Diff

```powershell
# What changed since last pull?
$changes = git -C "sources/<name>" diff HEAD@{1} --name-only
$stats   = git -C "sources/<name>" diff HEAD@{1} --stat
$commits = git -C "sources/<name>" log HEAD@{1}..HEAD --oneline
```

If no changes (`$changes` is empty) → Log as `UP_TO_DATE`, skip evaluation, move to next repo.

### Step 4: Clean Build Artifacts

Apply cleanup protocol from `source-manager` skill:
- Remove: `dist/`, `build/`, `.next/`, `bin/`, `obj/`, `target/`, `node_modules/`, `__pycache__/`, etc.

### Step 5: Evaluate Changes

Using the **Evaluation Criteria** from `source-manager` skill:

Scan the changed files specifically:
- New `SKILL.md` files → +3 each (if not in `shared/skills/`)
- Modified `SKILL.md` files → +2 if significantly improved
- New agent `.md` files → +3 each
- New workflow `.md` files → +2 each
- New rule/template files → +1 each
- Duplicates/conflicts → -2 or -3

Calculate total score → determine verdict.

### Step 6: Integrate (POSITIVE only)

If verdict = ✅ **POSITIVE** (score ≥ 5):
- Copy new/improved content to `shared/` following the integration protocol
- Do NOT overwrite existing files (skip conflicts)
- Log all integrated and skipped files

If verdict = ⚠️ **MARGINAL** (score 1–4):
- Do NOT auto-integrate
- Flag in report: "Manual review recommended"

If verdict = ❌ **NEGATIVE** (score ≤ 0):
- Do NOT integrate
- Note in report why

### Step 7: Generate Report

For each repo, generate a report following the template in `source-manager` skill.

Save to: `sources/reports/YYYY-MM-DD_update-<name>.md`

### Step 8: Final Summary

After processing all repos, output a summary table:

```markdown
## /update-sources — Final Summary
Date: YYYY-MM-DD

| Repo | Status | Verdict | Score | Integrated |
|------|--------|---------|-------|-----------|
| antigravity-awesome-skills | ✅ Pulled | ✅ POSITIVE | 8 | 3 skills |
| superpowers | ✅ Pulled | ❌ NEGATIVE | -1 | 0 |
| hermes-agent | ⚠️ UP_TO_DATE | — | — | — |
| awesome-copilot | ❌ PULL_FAILED | — | — | — |

**Total integrated**: X items
**Reports saved**: sources/reports/
```

### Step 9: Run Sync (if anything was integrated)

If at least 1 item was integrated:
```powershell
powershell -ExecutionPolicy Bypass -File scripts/sync_all.ps1
```

---

## Notes

- This workflow is **read-only for remote repos** — only `git pull`, never `git push`.
- Never delete source repo folders. Keep them in `sources/` for reference.
- If `sync_all.ps1` is not available, manually copy from `shared/` to IDE folders.
