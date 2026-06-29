---
inclusion: auto
description: Project-specific patterns, preferences, and lessons learned over time (user-editable)
---

# Lessons Learned

This file captures project-specific patterns, coding preferences, common pitfalls, and architectural decisions that emerge during development. It serves as a workaround for continuous learning by allowing you to document patterns manually.

**How to use this file:**
1. The `extract-patterns` hook will suggest patterns after agent sessions
2. Review suggestions and add genuinely useful patterns below
3. Edit this file directly to capture team conventions
4. Keep it focused on project-specific insights, not general best practices

---

## Antigravity ↔ Kiro Format Translation

### Agent `.md` frontmatter: 3 điểm cần normalize khi dịch từ Antigravity sang Kiro
```
# Antigravity (nguồn)        →  Kiro IDE (đích)
tools: Read, Grep, Bash       →  tools: ["Read", "Grep", "Bash"]   # CSV → JSON array
model: inherit                →  model: claude-sonnet-4-5           # map tường minh
skills: a, b, c               →  (xoá khỏi frontmatter)            # Kiro không dùng trường này
```
Body markdown giữ nguyên — Kiro đọc giống Claude.

### Workflows Antigravity → Steering Kiro
- Mặc định: `inclusion: manual` (dùng khi cần, không tự nạp), nhưng `orchestrate` sẽ có `inclusion: always` (tự động nạp dù bất kể trường hợp nào)
- Ngoại lệ: `/orchestrate` → `inclusion: auto` (luôn luôn nạp vì định nghĩa protocol đa-agent)
- Prefix an toàn: dùng `workflow-` cho workflows, `antigravity-` cho rules, tránh đụng tên ECC

### Non-destructive migration pattern
Khi bổ sung Antigravity vào ECC Kiro hiện có: skip tên trùng thay vì ghi đè, dùng prefix để namespace riêng. ECC là nền tảng, Antigravity là layer bổ sung.

### Migration tool task decomposition: PBT co-located with translators
When speccing a migration/translation tool, place property-based tests (`*` optional tasks) immediately after the corresponding translator task — not in a separate testing section. This keeps the correctness contract co-located with the implementation (e.g., task 3.1 implements AgentTranslator, task 3.2 is its PBT P3 test). Integration test and CLI go last after all components are stable. Recommended wave order: Setup → Scanner → [Translator + PBT]×N → Writer → Pipeline + Idempotence → CLI → Strategies → Integration.

### `NonDestructiveWriter` as single choke-point for skip/overwrite logic
In any additive/non-destructive file operation tool, centralise the `if dest.exists(): skip` check in one writer class rather than inside each individual translator. This makes idempotence and non-destructive guarantees impossible to bypass regardless of which translator calls the writer, and gives a single place to audit or test the behavior.

---

## Project-Specific Patterns

*Document patterns unique to this project that the team should follow.*

### Example: API Error Handling
```typescript
// Always use our custom ApiError class for consistent error responses
throw new ApiError(404, 'Resource not found', { resourceId });
```

---

## Code Style Preferences

*Document team preferences that go beyond standard linting rules.*

### Example: Import Organization
```typescript
// Group imports: external, internal, types
import { useState } from 'react';
import { Button } from '@/components/ui';
import type { User } from '@/types';
```

---

## Kiro Hooks

### `install.sh` is additive-only — it won't update existing installations
The installer skips any file that already exists in the target (`if [ ! -f ... ]`). Running it against a folder that already has `.kiro/` will not overwrite or update hooks, agents, or steering files. To push updates to an existing project, manually copy the changed files or remove the target files first before re-running the installer.

### README.md mirrors hook configurations — keep them in sync
The hooks table and Example 5 in README.md document the action type (`runCommand` vs `askAgent`) and behavior of each hook. When changing a hook's `then.type` or behavior, update both the hook file and the corresponding README entries to avoid misleading documentation.

### Prefer `askAgent` over `runCommand` for file-event hooks
`runCommand` hooks on `fileEdited` or `fileCreated` events spawn a new terminal session every time they fire, creating friction. Use `askAgent` instead so the agent handles the task inline. Reserve `runCommand` for `userTriggered` hooks where a manual, isolated terminal run is intentional (e.g., `quality-gate`).

---

## Common Pitfalls

*Document mistakes that have been made and how to avoid them.*

### Example: Database Transactions
- Always wrap multiple database operations in a transaction
- Remember to handle rollback on errors
- Don't forget to close connections in finally blocks

---

## Architecture Decisions

*Document key architectural decisions and their rationale.*

### Example: State Management
- **Decision**: Use Zustand for global state, React Context for component trees
- **Rationale**: Zustand provides better performance and simpler API than Redux
- **Trade-offs**: Less ecosystem tooling than Redux, but sufficient for our needs

---

## Notes

- Keep entries concise and actionable
- Remove patterns that are no longer relevant
- Update patterns as the project evolves
- Focus on what's unique to this project
