# Unified AI Agent Toolkit — OpenCode Instructions

This supplements the OpenCode configuration with orchestrator-first routing and unified agent capabilities.

**Merged from:** everything-claude-code, superpowers, antigravity-kit

## Core Principles

1. **Orchestrator-First** — Complex tasks route through the orchestrator for multi-agent coordination
2. **Plan Before Execute** — Plan complex features before writing code
3. **Test-Driven** — Write tests before implementation, 80%+ coverage required
4. **Security-First** — Never compromise on security; validate all inputs
5. **Immutability** — Always create new objects, never mutate existing ones

## Agent Orchestration Protocol

Use agents proactively:
- Complex feature requests → **planner** first, then specialists
- Code just written/modified → **code-reviewer**
- Bug fix or new feature → **tdd-guide**
- Architectural decision → **architect**
- Security-sensitive code → **security-reviewer**

## Available Agents

| Agent | Purpose | When to Use |
|-------|---------|-------------|
| planner | Implementation planning | Complex features, refactoring |
| architect | System design and scalability | Architectural decisions |
| tdd-guide | Test-driven development | New features, bug fixes |
| code-reviewer | Code quality and security | After writing/modifying code |
| security-reviewer | Vulnerability detection | Before commits, sensitive code |
| build-error-resolver | Fix build/type errors | When build fails |
| e2e-runner | End-to-end testing | Critical user flows |
| refactor-cleaner | Dead code cleanup | Code maintenance |
| doc-updater | Documentation updates | Updating docs |
| go-reviewer | Go code review | Go projects |
| python-reviewer | Python code review | Python projects |
| database-reviewer | Database specialist | Schema design, queries |

## Coding Standards

- Prefer immutable updates over in-place mutation
- Keep functions small (<50 lines), files focused (<800 lines)
- Validate user input at boundaries
- Never hardcode secrets
- Fail loudly with clear error messages

## Security Guidelines

Before ANY commit:
- No hardcoded secrets (API keys, passwords, tokens)
- All user inputs validated
- SQL injection prevention (parameterized queries)
- XSS prevention (sanitized HTML)
- CSRF protection enabled
- Authentication/authorization verified
- Error messages don't leak sensitive data

## Testing Requirements

- Minimum coverage: 80%
- TDD workflow: RED → GREEN → REFACTOR
- Unit, Integration, and E2E tests all required
- Troubleshoot failures: check isolation → verify mocks → fix implementation

## Git Workflow

- Conventional commits: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`, `perf:`, `ci:`
- Comprehensive PR summaries with test plans
- Push with `-u` flag

## Skills Discovery

Skills are loaded from `.opencode/instructions/`. Each provides domain-specific workflow guidance.
Core skills: coding-standards, security-review, tdd-workflow, verification-loop, api-design
