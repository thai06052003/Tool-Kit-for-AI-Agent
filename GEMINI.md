---
trigger: always_on
---

# GEMINI.md - Unified AI Agent Toolkit

> This file defines AI behavior in this workspace for Antigravity IDE.
> Merged from: antigravity-kit, everything-claude-code, superpowers, awesome-copilot

---

## CRITICAL: ORCHESTRATOR-FIRST PROTOCOL

> **MANDATORY:** All complex requests go through the orchestrator agent first.
> The orchestrator analyzes requirements and delegates to specialist agents.

### Agent Activation Flow

```
User Request → Orchestrator Analysis → Agent Selection → Specialist Execution → Synthesis
```

### Quick Routing

| Request Type     | Route To              | Action                          |
| ---------------- | --------------------- | ------------------------------- |
| **QUESTION**     | Direct response       | Answer immediately              |
| **SIMPLE CODE**  | Relevant specialist   | Inline edit                     |
| **COMPLEX CODE** | `orchestrator`        | Plan → Delegate → Execute      |
| **DESIGN/UI**    | `frontend-specialist` | Design → Implement → Review    |
| **DEBUG**        | `debugger`            | Analyze → Fix → Verify         |
| **SECURITY**     | `security-auditor`    | Scan → Report → Fix            |

---

## TIER 0: UNIVERSAL RULES (Always Active)

### 🌐 Language Handling
- Respond in user's language
- Code comments/variables remain in English

### 🧹 Clean Code (Global)
- Concise, direct, no over-engineering
- Testing mandatory: Unit > Integration > E2E
- Performance: Measure first, optimize second
- Security: Validate all inputs, never hardcode secrets

### 🧠 Read → Understand → Apply
```
❌ WRONG: Read agent file → Start coding
✅ CORRECT: Read → Understand WHY → Apply PRINCIPLES → Code
```

---

## TIER 1: CODE RULES

### Socratic Gate
For complex requests, ASK strategic questions before implementing:
- Purpose & scope
- Tech preferences
- Constraints & edge cases

### Development Workflow
1. **Plan** → Use project-planner for complex features
2. **TDD** → Write tests first, implement, refactor
3. **Review** → Code review after implementation
4. **Security** → Security audit before shipping

### Coding Standards
- Prefer immutable updates over in-place mutation
- Keep functions small (<50 lines), files focused (<800 lines)
- Validate user input at boundaries
- Never hardcode secrets
- Fail loudly with clear error messages
- Use conventional commits: feat, fix, refactor, docs, test, chore

---

## AVAILABLE AGENTS

| Agent                  | Domain                    |
| ---------------------- | ------------------------- |
| `orchestrator`         | Multi-agent coordination  |
| `project-planner`      | Task planning & breakdown |
| `frontend-specialist`  | Web UI/UX, React, Next.js |
| `backend-specialist`   | API, Node.js, Python      |
| `database-architect`   | Schema, SQL, migrations   |
| `security-auditor`     | Security & compliance     |
| `test-engineer`        | Testing strategies        |
| `debugger`             | Root cause analysis       |
| `mobile-developer`     | iOS, Android, RN          |
| `devops-engineer`      | CI/CD, Docker, Deploy     |
| `code-reviewer`        | Code quality review       |
| `performance-optimizer`| Speed, Web Vitals         |
| `documentation-writer` | Docs & manuals            |
| `game-developer`       | Game logic & mechanics    |

---

## QUICK REFERENCE

| Need     | Agent                 | Skills                                |
| -------- | --------------------- | ------------------------------------- |
| Web App  | `frontend-specialist` | react-best-practices, frontend-design |
| API      | `backend-specialist`  | api-patterns, nodejs-best-practices   |
| Mobile   | `mobile-developer`    | mobile-design                         |
| Database | `database-architect`  | database-design                       |
| Security | `security-auditor`    | vulnerability-scanner                 |
| Testing  | `test-engineer`       | testing-patterns, tdd-workflow        |
| Debug    | `debugger`            | systematic-debugging                  |
| Plan     | `project-planner`     | brainstorming, plan-writing           |
