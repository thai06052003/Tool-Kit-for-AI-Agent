---
name: self-learning-loop
description: Teaches the AI agent to create new skills from experience, building procedural memory that makes future tasks easier and smarter.
version: 1.0.0
metadata:
  hermes:
    tags: [self-improvement, learning, meta-cognition, procedural-memory]
    category: meta
---

# Self-Learning Loop

When you successfully complete a complex task, **create a new skill** to remember the approach for future reuse.

## When to Create a New Skill

Create a new skill when ANY of these conditions are met:

1. **Complex task completed**: Task required 5+ distinct steps or tool calls
2. **Error recovery**: You hit errors or dead ends and found the working path
3. **User correction**: The user corrected your approach — save the correct method
4. **Non-trivial workflow**: You discovered a workflow that isn't obvious
5. **Repeated pattern**: You recognize you've done similar work before

## How to Create a Skill

### Step 1: Assess if Skill-Worthy

Ask yourself:
- Would this approach be useful next time?
- Did I learn something non-obvious?
- Would another developer benefit from this?

If YES to any → create the skill.

### Step 2: Write the SKILL.md

```markdown
---
name: <descriptive-kebab-case-name>
description: <one-line description>
version: 1.0.0
metadata:
  hermes:
    tags: [<relevant>, <tags>]
    category: <category>
---

# <Skill Title>

## When to Use
<Clear trigger conditions>

## Procedure
1. <Step 1>
2. <Step 2>
...

## Pitfalls
- <Known failure modes and fixes>

## Verification
<How to confirm it worked>
```

3. **Draft & Save (Level-Up Protocol)**:
   - Write the `SKILL.md` file.
   - Save to: `output/shared/skills/<name>/SKILL.md`
   - **MANDATORY MIRROR**: Mirror the save to `level-up/output/shared/skills/<name>/SKILL.md`.
   - **Purpose**: This ensures `level-up/` preserves all AI-generated advancements with correct paths for easy root-merging.
- **Antigravity/Cursor/VS Code**: `shared/skills/<skill-name>/SKILL.md`
- **IDE-agnostic**: Save in the project's skill directory

### Step 4: Announce

Tell the user:
```
💡 Created new skill: <skill-name>
   Category: <category>
   Trigger: <when it activates>
```

## Skill Improvement Protocol

When using an existing skill and discovering a better approach:

1. Read the current skill content
2. Patch only the changed sections (don't rewrite entirely)
3. Increment the version (1.0.0 → 1.1.0)
4. Add the improvement to the "Pitfalls" or "Procedure" section
5. Announce: `🔄 Improved skill: <skill-name> → v<new-version>`

## Categories

| Category | For Skills About |
|----------|-----------------|
| `software-development` | Coding patterns, debugging, testing |
| `devops` | CI/CD, Docker, deployment |
| `data-science` | ML, data processing |
| `productivity` | Workflow automation |
| `research` | Investigation, analysis |
| `creative` | Design, writing |
| `security` | Security scanning, compliance |
| `domain` | Domain-specific knowledge |

## Anti-Patterns

- ❌ Don't create skills for trivial tasks (< 3 steps)
- ❌ Don't duplicate existing skills
- ❌ Don't include secrets or API keys in skills
- ❌ Don't create overly narrow skills (too specific to one project)
