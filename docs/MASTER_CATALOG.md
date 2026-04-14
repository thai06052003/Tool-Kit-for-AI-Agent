# MASTER CATALOG — Unified AI Agent Toolkit

> Tài liệu kiểm kê, phân loại và loại trùng toàn bộ nội dung từ 5 toolkits.
> Cập nhật: 2026-04-06

---

## 1. Tổng hợp Agents (59 unique, merged từ 241 thô)

### Danh mục 1: Orchestration & Planning (4 agents)

| Agent | Nguồn ưu tiên | Nguồn phụ | Ghi chú |
|-------|---------------|-----------|---------|
| `orchestrator` | antigravity-kit | — | Multi-agent coordination, Socratic Gate |
| `project-planner` | antigravity-kit | ECC `planner` | Merged: AK có Socratic Gate, ECC có read-only tools |
| `chief-of-staff` | ECC | — | Executive assistant, project management |
| `explorer-agent` | antigravity-kit | — | Codebase discovery, read-only |

### Danh mục 2: Code Quality & Review (4 agents)

| Agent | Nguồn ưu tiên | Nguồn phụ | Ghi chú |
|-------|---------------|-----------|---------|
| `code-reviewer` | ECC | superpowers | Merged: ECC security-focused + SP verification flow |
| `refactor-cleaner` | ECC | — | Dead code cleanup, consolidation |
| `code-archaeologist` | antigravity-kit | — | Legacy code, refactoring |
| `architect` | ECC | — | System design, scalability |

### Danh mục 3: Security (3 agents)

| Agent | Nguồn ưu tiên | Nguồn phụ | Ghi chú |
|-------|---------------|-----------|---------|
| `security-auditor` | antigravity-kit | ECC `security-reviewer` | AK wider scope, ECC OWASP-focused |
| `penetration-tester` | antigravity-kit | — | Offensive security testing |
| `healthcare-reviewer` | ECC | — | Healthcare compliance (PHI/HIPAA) |

### Danh mục 4: Testing & TDD (4 agents)

| Agent | Nguồn ưu tiên | Nguồn phụ | Ghi chú |
|-------|---------------|-----------|---------|
| `test-engineer` | antigravity-kit | — | Broad testing strategies |
| `tdd-guide` | ECC | — | Strict TDD methodology |
| `e2e-runner` | ECC | — | Playwright/Cypress E2E |
| `qa-automation-engineer` | antigravity-kit | — | CI pipeline testing |

### Danh mục 5: Frontend & UI/UX (2 agents)

| Agent | Nguồn ưu tiên | Nguồn phụ | Ghi chú |
|-------|---------------|-----------|---------|
| `frontend-specialist` | antigravity-kit | — | React, Next.js, Tailwind |
| `flutter-reviewer` | ECC | — | Flutter/Dart code review |

### Danh mục 6: Backend & API (3 agents)

| Agent | Nguồn ưu tiên | Nguồn phụ | Ghi chú |
|-------|---------------|-----------|---------|
| `backend-specialist` | antigravity-kit | — | Node.js, Express, FastAPI |
| `database-architect` | antigravity-kit | ECC `database-reviewer` | AK schema design, ECC query optimization |
| `docs-lookup` | ECC | — | Documentation lookup via Context7 |

### Danh mục 7: Language-Specific Reviewers (12 agents)

| Agent | Nguồn | Ngôn ngữ |
|-------|-------|----------|
| `typescript-reviewer` | ECC | TypeScript/JavaScript |
| `python-reviewer` | ECC | Python |
| `go-reviewer` | ECC | Go |
| `rust-reviewer` | ECC | Rust |
| `java-reviewer` | ECC | Java/Spring |
| `kotlin-reviewer` | ECC | Kotlin/Android |
| `cpp-reviewer` | ECC | C++ |
| `csharp-reviewer` | ECC | C# / .NET |
| `go-build-resolver` | ECC | Go build errors |
| `java-build-resolver` | ECC | Java/Maven/Gradle |
| `kotlin-build-resolver` | ECC | Kotlin/Gradle |
| `rust-build-resolver` | ECC | Rust build errors |

### Danh mục 8: DevOps & Deployment (2 agents)

| Agent | Nguồn ưu tiên | Nguồn phụ | Ghi chú |
|-------|---------------|-----------|---------|
| `devops-engineer` | antigravity-kit | — | CI/CD, Docker, monitoring |
| `build-error-resolver` | ECC | — | Build/TypeScript errors |

### Danh mục 9: Documentation (2 agents)

| Agent | Nguồn ưu tiên | Nguồn phụ | Ghi chú |
|-------|---------------|-----------|---------|
| `documentation-writer` | antigravity-kit | — | Manuals, README, API docs |
| `doc-updater` | ECC | — | Codemaps, auto-update docs |

### Danh mục 10: Specialized (8 agents)

| Agent | Nguồn | Chuyên môn |
|-------|-------|-----------|
| `game-developer` | antigravity-kit | Unity, Godot, Phaser |
| `mobile-developer` | antigravity-kit | React Native, Flutter |
| `performance-optimizer` | antigravity-kit + ECC | Profiling, Web Vitals |
| `seo-specialist` | antigravity-kit | SEO, E-E-A-T |
| `product-manager` | antigravity-kit | Requirements, user stories |
| `product-owner` | antigravity-kit | Strategy, backlog |
| `loop-operator` | ECC | Autonomous loop execution |
| `harness-optimizer` | ECC | Test harness tuning |

### Agents bị LOẠI (trùng hoặc quá chuyên biệt)

| Agent | Nguồn | Lý do loại |
|-------|-------|-----------|
| `planner` (ECC) | ECC | Trùng `project-planner` (AK) |
| `security-reviewer` (ECC) | ECC | Trùng `security-auditor` (AK) |
| `performance-optimizer` (ECC) | ECC | Trùng với AK version |
| `gan-*` (3 agents) | ECC | Quá chuyên biệt (GAN AI) |
| `opensource-*` (3 agents) | ECC | Quá chuyên biệt |
| `cpp-build-resolver` | ECC | Ít dùng |
| `dart-build-resolver` | ECC | Ít dùng |
| `pytorch-build-resolver` | ECC | Quá chuyên biệt |
| 182 awesome-copilot agents | awesome-copilot | Chuyển thành instructions/rules cho VS Code & VS |

---

## 2. Tổng hợp Skills (75 unique, chọn lọc từ 1753 thô)

### Core Skills (Luôn có trong mọi IDE)

| # | Skill | Nguồn ưu tiên | Danh mục |
|---|-------|---------------|---------|
| 1 | `clean-code` | antigravity-kit | Code Quality |
| 2 | `coding-standards` | ECC | Code Quality |
| 3 | `security-review` | ECC | Security |
| 4 | `tdd-workflow` | ECC + antigravity-kit | Testing |
| 5 | `verification-loop` | ECC | Testing |
| 6 | `plan-writing` | antigravity-kit + superpowers | Planning |
| 7 | `brainstorming` | antigravity-kit + superpowers | Planning |
| 8 | `architecture` | antigravity-kit | Planning |
| 9 | `systematic-debugging` | antigravity-kit + superpowers | Debug |
| 10 | `code-review-checklist` | antigravity-kit | Code Quality |

### Frontend Skills

| # | Skill | Nguồn | Ghi chú |
|---|-------|-------|---------|
| 11 | `frontend-design` | antigravity-kit | UI/UX patterns |
| 12 | `frontend-patterns` | ECC | React, Next.js patterns |
| 13 | `tailwind-patterns` | antigravity-kit | Tailwind CSS v4 |
| 14 | `web-design-guidelines` | antigravity-kit | 100+ UI rules |
| 15 | `nextjs-react-expert` | antigravity-kit | React best practices |

### Backend Skills

| # | Skill | Nguồn | Ghi chú |
|---|-------|-------|---------|
| 16 | `api-design` | ECC | REST API patterns |
| 17 | `api-patterns` | antigravity-kit | REST, GraphQL, tRPC |
| 18 | `backend-patterns` | ECC | Node.js, Express |
| 19 | `nodejs-best-practices` | antigravity-kit | Node.js async, modules |
| 20 | `database-design` | antigravity-kit | Schema, optimization |
| 21 | `database-migrations` | ECC | Schema changes |
| 22 | `postgres-patterns` | ECC | PostgreSQL optimization |

### Testing Skills

| # | Skill | Nguồn | Ghi chú |
|---|-------|-------|---------|
| 23 | `testing-patterns` | antigravity-kit | Jest, Vitest, strategies |
| 24 | `e2e-testing` | ECC | Playwright E2E |
| 25 | `webapp-testing` | antigravity-kit | E2E, deep audit |
| 26 | `test-driven-development` | superpowers | TDD before code |
| 27 | `verification-before-completion` | superpowers | Evidence before assertions |

### Language-Specific Skills

| # | Skill | Nguồn | Ngôn ngữ |
|---|-------|-------|---------|
| 28 | `python-patterns` | antigravity-kit + ECC | Python |
| 29 | `python-testing` | ECC | Pytest |
| 30 | `golang-patterns` | ECC | Go idioms |
| 31 | `golang-testing` | ECC | Go table-driven tests |
| 32 | `rust-pro` | antigravity-kit | Rust 1.75+ |
| 33 | `docker-patterns` | ECC | Docker best practices |
| 34 | `deployment-patterns` | ECC | CI/CD patterns |

### Workflow & Methodology Skills

| # | Skill | Nguồn | Ghi chú |
|---|-------|-------|---------|
| 35 | `agentic-engineering` | ECC | Eval-first execution |
| 36 | `parallel-agents` | antigravity-kit | Multi-agent patterns |
| 37 | `dispatching-parallel-agents` | superpowers | Independent task dispatch |
| 38 | `subagent-driven-development` | superpowers | Subagent execution |
| 39 | `executing-plans` | superpowers | Plan execution with review |
| 40 | `writing-plans` | superpowers | Multi-step task planning |
| 41 | `writing-skills` | superpowers | Creating new skills |
| 42 | `requesting-code-review` | superpowers | Pre-merge verification |
| 43 | `receiving-code-review` | superpowers | Code review feedback |
| 44 | `finishing-a-development-branch` | superpowers | Branch completion |
| 45 | `using-git-worktrees` | superpowers | Isolated git worktrees |
| 46 | `search-first` | ECC | Research-before-code |
| 47 | `git-workflow` | ECC | Git conventions |
| 48 | `deep-research` | ECC | Multi-source research |

### Specialized Skills

| # | Skill | Nguồn | Ghi chú |
|---|-------|-------|---------|
| 49 | `behavioral-modes` | antigravity-kit | Agent personas |
| 50 | `app-builder` | antigravity-kit | Full-stack scaffolding |
| 51 | `game-development` | antigravity-kit | Game mechanics |
| 52 | `mobile-design` | antigravity-kit | Mobile UI/UX |
| 53 | `mcp-builder` | antigravity-kit | MCP server building |
| 54 | `seo-fundamentals` | antigravity-kit | SEO, E-E-A-T |
| 55 | `geo-fundamentals` | antigravity-kit | GenAI optimization |
| 56 | `i18n-localization` | antigravity-kit | Internationalization |
| 57 | `performance-profiling` | antigravity-kit | Web Vitals |
| 58 | `vulnerability-scanner` | antigravity-kit | OWASP security scan |
| 59 | `red-team-tactics` | antigravity-kit | Offensive security |
| 60 | `documentation-templates` | antigravity-kit | Doc formats |
| 61 | `deployment-procedures` | antigravity-kit | CI/CD workflows |
| 62 | `server-management` | antigravity-kit | Infrastructure |
| 63 | `bash-linux` | antigravity-kit | Linux CLI |
| 64 | `powershell-windows` | antigravity-kit | Windows CLI |
| 65 | `intelligent-routing` | antigravity-kit | Auto agent selection |

---

## 3. Tổng hợp Rules (17 unique rule sets)

| # | Rule Set | Nguồn | Scope |
|---|---------|-------|-------|
| 1 | `common` | ECC | Universal coding rules |
| 2 | `security` | ECC + AK | Security checklist |
| 3 | `typescript` | ECC | TypeScript patterns |
| 4 | `python` | ECC | Python PEP 8 |
| 5 | `golang` | ECC | Go idioms |
| 6 | `rust` | ECC | Rust idioms |
| 7 | `java` | ECC | Java/Spring |
| 8 | `kotlin` | ECC | Kotlin/KMP |
| 9 | `csharp` | ECC | C# / .NET |
| 10 | `cpp` | ECC | C++ standards |
| 11 | `swift` | ECC | Swift patterns |
| 12 | `dart` | ECC | Dart/Flutter |
| 13 | `perl` | ECC | Perl patterns |
| 14 | `php` | ECC | PHP patterns |
| 15 | `web` | ECC | HTML/CSS/JS |
| 16 | `orchestration` | NEW (from AK orchestrator) | Orchestrator-first routing |
| 17 | `testing` | ECC + AK | TDD requirements |

---

## 4. Tổng hợp Workflows (11 unique)

| # | Workflow | Nguồn ưu tiên | Mục đích |
|---|---------|---------------|---------|
| 1 | `/orchestrate` | antigravity-kit | Multi-agent coordination |
| 2 | `/plan` | antigravity-kit | Task breakdown |
| 3 | `/create` | antigravity-kit | App builder |
| 4 | `/debug` | antigravity-kit | Debug workflow |
| 5 | `/test` | antigravity-kit | Test generation |
| 6 | `/deploy` | antigravity-kit | Deployment |
| 7 | `/enhance` | antigravity-kit | Feature improvement |
| 8 | `/preview` | antigravity-kit | Local preview |
| 9 | `/status` | antigravity-kit | Project status |
| 10 | `/brainstorm` | antigravity-kit + superpowers | Socratic discovery |
| 11 | `/ui-ux-pro-max` | antigravity-kit | Design with 50 styles |

---

## 5. Thống kê FINAL

| Loại | Thô (5 toolkits) | Sau loại trùng | Tỉ lệ giảm |
|------|------------------|----------------|-------------|
| **Agents** | 241 | 44 (shared) + 182 (copilot→instructions) | -82% |
| **Skills** | 1753 | 65 (shared) | -96% |
| **Rules** | 189 | 17 rule sets | -91% |
| **Workflows** | 86 | 11 | -87% |
| **Hooks** | 10 | 10 | 0% |

> Giảm mạnh nhưng giữ chất lượng: Mỗi item trong shared/ đều là bản merge tinh hoa nhất từ nhiều nguồn.
