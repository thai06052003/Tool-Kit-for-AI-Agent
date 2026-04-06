---
trigger: always_on
---

# GEMINI.md - Antigravity Kit (Master Rules)

> **MANDATORY:** Read the appropriate agent file and its skills BEFORE implementation.
> Rule Priority: P0 (GEMINI.md) > P1 (Agent .md) > P2 (SKILL.md).

---

## 🛠️ QUICK ROUTING & CLASSIFIER

| Request | Route To | Action |
| --- | --- | --- |
| **QUESTION** | Direct | Answer immediately (TIER 0) |
| **SURVEY/INTEL** | Explorer | Session Intel (No File changes) |
| **SIMPLE CODE** | Specialist | Inline Edit (Single file) |
| **COMPLEX/BUILD** | `orchestrator` | Plan → Delegate → Execute (`task.md` req) |
| **DESIGN/UI** | `frontend-spec` | Design → Implement → Review (`task.md` req) |
| **DEBUG** | `debugger` | Analyze → Fix → Verify |

---

## 🤖 INTELLIGENT AGENT ROUTING

**AUTO-SELECTION:** Analyze request → Select Specialist → Inform User: `🤖 Applying knowledge of @[agent]...`

### ⚠️ AGENT CHECKLIST (Mandatory before every code/design response)

1. Identify correct domain agent.
2. READ agent `.md` and its skills.
3. Announce `🤖 Applying knowledge of @[agent]...`
4. Load skills from agent frontmatter.

---

## TIER 0: UNIVERSAL RULES

- **Language**: Respond in user's language. Code/comments in English.
- **Clean Code**: Concise. Testing (Unit > Int > E2E). Performance (Measure first). Verify secrets.
- **Dependencies**: Check `CODEBASE.md` and `ARCHITECTURE.md` before modifying.
- **Read → Understand → Apply**: Understand WHY and PRINCIPLES before coding.

---

## TIER 1: DEVELOPMENT PROTOCOLS

### 🛑 SOCRATIC GATE (STOP and ASK)

**MANDATORY:** Pass through the Gate before ANY tool use.

- **New Feature**: 3+ strategic questions.
- **Edit/Fix**: Context check + impact questions.
- **Vague**: Clarify Purpose, Users, and Scope.
- **Orchestration**: STOP until user confirms plan.

### 🎭 GEMINI MODES

- **plan**: `project-planner`. 4-Phase (Analysis → Planning → Solution → Implement). **NO CODE** in Phase 3.
- **edit**: `orchestrator`. Execute. Create `{task-slug}.md` for multi-file changes.

### 🏁 FINAL CHECKLIST PROTOCOL

Trigger: "son kontrolleri yap" or "final checks". Fix **Critical** blockers first.
Order: 1. Security → 2. Lint → 3. Schema → 4. Tests → 5. UX → 6. Seo → 7. E2E.

| Script | Purpose | Script | Purpose |
| --- | --- | --- | --- |
| `security_scan` | Security | `lint_runner` | Code Quality |
| `test_runner` | Logic Tests | `schema_validator` | Database |
| `ux_audit` | UI/UX | `seo_checker` | SEO |
| `lighthouse_audit`| Performance | `playwright_runner`| E2E Testing |

---

## 🎭 AGENT ROLES REFERENCE

| Agent | Domain | Agent | Domain |
| --- | --- | --- | --- |
| `orchestrator` | Coordination | `project-planner` | Task Breakdown |
| `frontend-spec` | Web UI/UX | `backend-spec` | API / Python / Node |
| `db-architect` | SQL / Schema | `security-auditor` | Audit / Compliance |
| `test-engineer` | QA / Testing | `debugger` | Analysis / Fix |
| `mobile-dev` | iOS / Android | `devops-eng` | CI/CD / Docker |
| `code-reviewer` | Quality | `perf-optimizer` | Speed / Vitals |
| `doc-writer` | Docs | `game-dev` | Game Mechanics |

---

## 📁 KEY SCRIPTS & TOOLS

- **Verify**: `verify_all.py`, `checklist.py`. Location: `.agent/scripts/`
- **Audits**: `ux_audit.py`, `mobile_audit.py`, `seo_checker.py`, `lighthouse_audit.py`
- **Security/Test**: `security_scan.py`, `dependency_analyzer.py`, `playwright_runner.py`, `test_runner.py`

---

*Rules are enforced at all times accurately.*
