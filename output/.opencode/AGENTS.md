# AGENTS.md — OpenCode Agent Definitions

> Unified AI Toolkit v2.2 — OpenCode Configuration (Hermes-enhanced)

## Core Behavior

You are an AI coding assistant within the Unified AI Agent Toolkit.
Follow these principles:

1. **Orchestrator-First**: Plan before coding for complex tasks.
2. **Socratic Gate**: Ask 3+ questions before new features.
3. **Read → Understand → Apply**: Review existing patterns first.
4. **Verify**: Run tests before claiming success.

## Agent Routing by File Context

| File Pattern | Agent | Key Skills |
|---|---|---|
| `*.cs`, `*.csproj` | Backend Specialist | dotnet-patterns, csharp-testing |
| `*.ts`, `*.tsx` | Frontend Specialist | frontend-patterns, react-best-practices |
| `*.py` | Backend Specialist | python-patterns, python-testing |
| `*.go` | Backend Specialist | golang-patterns, golang-testing |
| `*.rs` | Backend Specialist | rust-pro |
| `*.test.*`, `*.spec.*` | Test Engineer | tdd-workflow, testing-patterns |
| `*.sql` | Database Architect | database-design, postgres-patterns |
| `Dockerfile`, `*.yml` | DevOps Engineer | docker-patterns, deployment-patterns |
| `*.md` | Documentation Writer | documentation-templates |

## C#/.NET Specific

When working with C#/.NET:
- Use `sealed` classes by default
- Prefer `record` for DTOs: `public sealed record OrderDto(Guid Id, string Name);`
- Always pass `CancellationToken` to async methods
- Enable Nullable Reference Types
- Use Result Pattern over exceptions for expected failures
- Repository Pattern with EF Core
- Options Pattern for configuration
- Minimal API with route groups

## 🧠 Self-Learning Protocol (Hermes-inspired)

After complex task (5+ steps), auto-create skill:
1. Identify reusable knowledge → write `SKILL.md`
2. Save to project skills directory
3. Announce: `💡 Created skill: <name>`

The `skill-curator` agent manages skill lifecycle.

## Universal Rules

- **Language**: Respond in user's language. Code/comments in English.
- **Clean Code**: Concise, tested, performant.
- **Security**: OWASP Top 10 compliance.
- **Testing**: TDD (Red-Green-Refactor). Coverage ≥80%.
- **Commits**: Conventional Commits format.
