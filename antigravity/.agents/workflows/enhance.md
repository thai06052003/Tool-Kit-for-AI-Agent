---
description: Add or update features in existing application. Used for iterative development.
---

# /enhance - Update Application

$ARGUMENTS

---

## Task

This command adds features or makes updates to existing application.

### Steps (Superpowers Engine Enabled):

> ⚠️ **CRITICAL: You MUST follow this precise modification sequence.**

1. **Understand Current State**
   - Load project state with `python .agent/scripts/session_manager.py info`
   - Use `explorer-agent` to map affected areas.

2. **Phase 1: Planning the Enhancement**
   - **REQUIRED SKILL:** Use `writing-plans`
   - Detect affected files and check dependencies.
   - Present plan to User (for major changes). Example: "I'll create 3 new files, update 2 files. Should I start?"

3. **Phase 2: Execution (Subagent Driven TDD)**
   - **REQUIRED SKILL:** Use `subagent-driven-development` & `test-driven-development`
   - Coordinate specialist agents based on the domain of the enhancement.
   - **MANDATORY POLICY:** Agents MUST write failing tests first, then implementation code. Complete the RED-GREEN-REFACTOR cycle for each affected file.

4. **Phase 3: Verification**
   - Run `python .agent/scripts/checklist.py .` to ensure no regressions.
   - Hot reload or restart the preview.

---

## Usage Examples

```
/enhance add dark mode
/enhance build admin panel
/enhance integrate payment system
/enhance add search feature
/enhance edit profile page
/enhance make responsive
```

---

## Caution

- Get approval for major changes
- Warn on conflicting requests (e.g., "use Firebase" when project uses PostgreSQL)
- Commit each change with git
