---
description: Debugging command. Activates DEBUG mode for systematic problem investigation.
---

# /debug - Systematic Problem Investigation

$ARGUMENTS

---

## Purpose

This command activates DEBUG mode for systematic investigation of issues, errors, or unexpected behavior.

---

## Behavior (Superpowers Engine Enabled)

When `/debug` is triggered, you MUST follow this precise sequence:

1. **Phase 1: Systematic Investigation**
   - **REQUIRED SKILL:** Use `systematic-debugging`
   - Gather error message, filepath, and recent changes.
   - Form hypotheses and test systematically before touching code.
   - Identify the exact root cause.

2. **Phase 2: Reproduction via TDD (CRITICAL)**
   - **REQUIRED SKILL:** Use `test-driven-development`
   - **MANDATORY:** Before fixing the bug, write a failing test that reproduces the exact issue.
   - Run the test to prove it fails exactly as described.

3. **Phase 3: Fix and Verify**
   - Write the minimal code to pass the newly created failing test.
   - Run the test again to prove the fix works (GREEN).
   - Use `finishing-a-development-branch` or run `python .agent/scripts/checklist.py .` to ensure nothing else broke.

---

## Output Format

```markdown
## 🔍 Debug: [Issue]

### 1. Symptom
[What's happening]

### 2. Information Gathered
- Error: `[error message]`
- File: `[filepath]`
- Line: [line number]

### 3. Hypotheses
1. ❓ [Most likely cause]
2. ❓ [Second possibility]
3. ❓ [Less likely cause]

### 4. Investigation

**Testing hypothesis 1:**
[What I checked] → [Result]

**Testing hypothesis 2:**
[What I checked] → [Result]

### 5. Root Cause
🎯 **[Explanation of why this happened]**

### 6. Fix
```[language]
// Before
[broken code]

// After
[fixed code]
```

### 7. Prevention
🛡️ [How to prevent this in the future]
```

---

## Examples

```
/debug login not working
/debug API returns 500
/debug form doesn't submit
/debug data not saving
```

---

## Key Principles

- **Ask before assuming** - get full error context
- **Test hypotheses** - don't guess randomly
- **Explain why** - not just what to fix
- **Prevent recurrence** - add tests, validation
