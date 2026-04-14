---
name: skill-evolution
description: Protocol for reviewing, improving, and evolving existing skills based on real-world usage feedback and accumulated knowledge.
version: 1.0.0
metadata:
  hermes:
    tags: [meta-cognition, skill-improvement, continuous-learning]
    category: meta
---

# Skill Evolution Protocol

A systematic process for improving skills based on experience.

## When to Evolve a Skill

1. **After using a skill**: Did it work perfectly? Were there gaps?
2. **After user feedback**: User says "that's not how we do it here"
3. **After discovering better tools**: New library, pattern, or approach found
4. **Periodic review**: Skills older than 3 months should be reviewed

## Evolution Process

### Phase 1: Evaluate

Score the skill on:
- **Accuracy**: Does the procedure still work? (1-5)
- **Completeness**: Are all edge cases covered? (1-5)
- **Clarity**: Can an AI follow it without confusion? (1-5)
- **Relevance**: Is this skill still needed? (1-5)

If average score < 3 → needs evolution.

### Phase 2: Improve

Apply the minimum effective change:

| Issue | Fix |
|-------|-----|
| Outdated dependency | Update version numbers and commands |
| Missing edge case | Add to Pitfalls section |
| Better approach found | Update Procedure, keep old as "Alternative" |
| Overly verbose | Trim to essential steps |
| Too vague | Add concrete examples |

### Phase 3: Version

Follow semver for skills:
- **1.0.0 → 1.0.1**: Typo fix, minor clarification
- **1.0.0 → 1.1.0**: New section, new pitfall, improved procedure
- **1.0.0 → 2.0.0**: Complete rewrite, breaking changes in procedure

### Phase 4: Validate

After evolving:
1. Re-read the entire skill
2. Check for internal consistency
3. Verify examples still work
4. Ensure format compliance (YAML frontmatter + required sections)

## Deprecation

If a skill is no longer useful:
1. Add `deprecated: true` to frontmatter
2. Add reason: `deprecated_reason: "Replaced by <new-skill>"`
3. Keep for 1 version cycle, then delete

## Skill Health Dashboard

Mentally track:
```
Skill: <name>
Last used: <date>
Last updated: <date>
Health: 🟢 Good | 🟡 Needs review | 🔴 Outdated
Times used: <count>
Success rate: <percentage>
```
