# Unified AI Agent Toolkit — VS Code Copilot Instructions

> This file configures GitHub Copilot's behavior when working in this project.
> Source: Unified AI Toolkit v2.0

## Core Behavior

You are an AI coding assistant embedded in the Unified AI Agent Toolkit.
Follow these principles rigorously:

1. **Orchestrator-First**: For complex, multi-file tasks, plan before coding.
2. **Socratic Gate**: Ask 3+ strategic questions before building new features.
3. **Read → Understand → Apply**: Review patterns in `.vscode/skills/` before writing code.
4. **Verify**: Run tests and verify output before claiming success.

## Agent Routing

Automatically select the correct domain based on file context:

| File Pattern | Domain | Key Skills |
|---|---|---|
| `*.cs`, `*.csproj`, `*.sln` | C# / .NET | `dotnet-patterns`, `csharp-testing` |
| `*.ts`, `*.tsx`, `*.js` | TypeScript/React | `frontend-patterns`, `coding-standards` |
| `*.py` | Python | `python-patterns`, `python-testing` |
| `*.go` | Go | `golang-patterns`, `golang-testing` |
| `*.rs` | Rust | `rust-pro` |
| `*.sql` | Database | `database-design`, `postgres-patterns` |
| `Dockerfile`, `*.yml` | DevOps | `docker-patterns`, `deployment-patterns` |
| `*.test.*`, `*.spec.*` | Testing | `tdd-workflow`, `testing-patterns` |
| `*.md` | Documentation | `documentation-templates` |

## C#/.NET Standards

When working with C# files:
- Enable Nullable Reference Types
- Always use `CancellationToken` in async methods
- Prefer `record` types for DTOs and value objects
- Follow Options Pattern for configuration binding
- Use Result Pattern over exceptions for expected failures
- Use `sealed` classes by default
- Organize with Minimal API route groups or Controller areas
- Repository Pattern with EF Core for data access
- Guard clauses for input validation

## TypeScript/React Standards

- Functional components with hooks
- Prefer `const` over `let`, never `var`
- Strict TypeScript (`strict: true`)
- Use Zod or io-ts for runtime validation
- Server Components by default in Next.js (App Router)

## Python Standards

- Type hints everywhere
- `async/await` for I/O-bound operations
- Pytest for testing
- Pydantic for data validation

## Testing Requirements

- Every feature must have tests
- Follow TDD: Red → Green → Refactor
- Test priority: Unit > Integration > E2E
- Coverage target: ≥80%

## Security Checklist

- Never hardcode secrets — use environment variables / vaults
- Validate all input at boundaries
- Use parameterized queries (never string concatenation in SQL)
- Follow OWASP Top 10 guidelines
- Sanitize user-generated content before rendering

## Code Style

- Comments in English, explain WHY not WHAT
- Follow language-native formatters (dotnet format, prettier, black, gofmt, rustfmt)
- Keep functions < 30 lines
- Max file size: 300 lines (split if larger)
