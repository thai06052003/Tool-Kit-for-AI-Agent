# GitHub Copilot Instructions — Visual Studio

> These instructions configure GitHub Copilot Agent Mode behavior in Visual Studio.
> Merged from: awesome-copilot, everything-claude-code

## Core Principles

1. **Plan Before Execute** — Break down complex tasks before implementation
2. **Test-Driven Development** — Write tests first (80%+ coverage minimum)
3. **Security-First** — Validate all inputs, never hardcode secrets
4. **Clean Code** — Small functions, focused files, self-documenting names
5. **Immutability** — Prefer creating new objects over mutating existing ones

## Agent Mode Behavior

When operating in Copilot Agent Mode:

### Iterative Problem Solving
- Detect build errors and fix them iteratively
- Run tests after code changes and fix failures
- Review git diff before suggesting commits
- Use terminal output to verify changes work

### Planning Protocol
- For multi-file changes, create a plan first
- Break features into discrete, testable steps
- Identify dependencies between changes
- Consider rollback strategy

### Code Changes
- Make minimal, focused changes
- Keep changes self-contained and easy to revert
- Run existing tests after modifications
- Add new tests for new functionality

## Coding Standards

### C# / .NET
- Follow Microsoft coding conventions
- Use nullable reference types
- Prefer LINQ for collection operations
- Use async/await for I/O operations
- Apply SOLID principles
- Use dependency injection

### TypeScript / JavaScript
- Strict TypeScript mode
- Prefer `const` over `let`, never use `var`
- Use async/await over raw Promises
- Runtime validation with zod or similar

### Python
- PEP 8 with type hints
- Pydantic for data validation
- Pytest for testing

## Security Checklist

Before EVERY commit:
- [ ] No hardcoded API keys, passwords, or tokens
- [ ] All external input validated and sanitized
- [ ] Parameterized queries for database operations
- [ ] Sanitized HTML output (XSS prevention)
- [ ] Auth/authz verified on sensitive endpoints
- [ ] Error messages scrubbed of sensitive internals

## Testing Requirements

- Minimum 80% code coverage
- TDD: Write failing test → Minimal implementation → Refactor
- Unit tests for core logic
- Integration tests for API and database operations
- E2E tests for critical user flows

## Architecture Patterns

- **Clean Architecture** — Separate concerns into layers
- **Repository Pattern** — Abstract data access
- **CQRS** — Command Query Responsibility Segregation for complex domains
- **Feature Folders** — Organize by domain, not by layer
- **Consistent API Envelopes** — Standard response format

## Git Workflow

- Conventional commits: `feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`
- Keep commits focused and atomic
- Include test plans in PR descriptions
- Review diff before pushing
