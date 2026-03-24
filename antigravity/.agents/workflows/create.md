---
description: Create new application command. Triggers App Builder skill and starts interactive dialogue with user.
---

# /create - Create Application

$ARGUMENTS

---

## Task

This command starts a new application creation process.

### Steps (Superpowers Engine Enabled):

> ⚠️ **CRITICAL: You MUST follow this exact Superpowers sequence.**

1. **Phase 1: Brainstorming & Spec Definition**
   - **REQUIRED SKILL:** Use `brainstorming`
   - Ask clarifying questions about features, users, and tech stack.
   - Output an approved spec document before writing any code.

2. **Phase 2: Worktree Isolation**
   - **REQUIRED SKILL:** Use `using-git-worktrees`
   - Create an isolated Git worktree for this new application to prevent affecting main branches.

3. **Phase 3: Detailed Planning**
   - **REQUIRED AGENT:** Invoke `@project-planner`
   - **REQUIRED SKILL:** Use `writing-plans`
   - Break down the spec into 2-5 minute bite-sized tasks. Determine the file structure and exact test files needed.
   - Save the plan to `docs/superpowers/plans/YYYY-MM-DD-app-creation.md`.

4. **Phase 4: Execution (Subagent Driven TDD)**
   - **REQUIRED SKILL:** Use `subagent-driven-development` and `test-driven-development`
   - Coordinate specialist agents (`@database-architect` → Schema, `@backend-specialist` → API, `@frontend-specialist` → UI).
   - Each agent MUST write failing tests first, then implementation code, following strict RED-GREEN-REFACTOR cycles.

5. **Phase 5: Verification & Completion**
   - Run `python .agent/scripts/verify_all.py .` to ensure code meets all standards.
   - Use `finishing-a-development-branch` to merge the worktree back or prepare a PR.

---

## Usage Examples

```
/create blog site
/create e-commerce app with product listing and cart
/create todo app
/create Instagram clone
/create crm system with customer management
```

---

## Before Starting

If request is unclear, ask these questions:
- What type of application?
- What are the basic features?
- Who will use it?

Use defaults, add details later.
