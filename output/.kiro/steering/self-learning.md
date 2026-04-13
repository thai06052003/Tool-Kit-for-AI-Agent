---
description: "Self-Learning Protocol — automatically create and improve skills from experience"
globs: ["**/*"]
alwaysApply: true
---

# 🧠 Self-Learning Protocol

## When to Activate
After completing any complex task (5+ tool calls or multi-file change):

1. **Assess skill-worthiness**: Is this approach reusable?
2. **Check existing skills**: Does a similar `SKILL.md` exist?
3. **Create or update**: Write/patch the skill with YAML frontmatter

## Skill Format
```yaml
---
name: <kebab-case-name>
description: <one-line description>
version: 1.0.0
metadata:
  hermes:
    tags: [<relevant-tags>]
    category: <category>
---
```

## Trigger Conditions
- Complex task completed successfully
- Error recovery path discovered
- User corrected AI approach
- Non-trivial workflow identified

## After Creating
Announce: `💡 Created skill: <name> | Category: <category>`
