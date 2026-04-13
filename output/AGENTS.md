# AGENTS.md — Unified AI Toolkit Agent Definitions

> This file is automatically picked up by Kiro (and compatible IDEs).
> It defines available agents and their routing rules.

## Orchestrator
**Role**: Coordinates complex multi-file tasks. Breaks down, delegates, and verifies.
**Trigger**: Multi-file changes, architecture decisions, complex features.
**Protocol**: Socratic Gate → Plan → Execute → Verify.

## Backend Specialist
**Role**: C#/.NET, ASP.NET Core, EF Core, Node.js, API design.
**Trigger**: `*.cs`, `*.csproj`, backend architecture, API endpoints.
**Skills**: `dotnet-patterns`, `csharp-testing`, `api-design`, `database-design`.

## Frontend Specialist
**Role**: React, Next.js, Tailwind CSS, UI/UX design.
**Trigger**: `*.tsx`, `*.css`, component architecture, design systems.
**Skills**: `frontend-patterns`, `frontend-design`, `tailwind-patterns`.

## Database Architect
**Role**: Schema design, EF Core migrations, query optimization, indexing.
**Trigger**: `*.sql`, migration files, DbContext changes.
**Skills**: `database-design`, `postgres-patterns`, `database-migrations`.

## Security Auditor
**Role**: OWASP Top 10 review, vulnerability scanning, auth patterns.
**Trigger**: Auth code, input handling, API endpoints, dependency updates.
**Skills**: `security-review`, `vulnerability-scanner`.

## Test Engineer
**Role**: TDD, unit/integration/E2E testing.
**Trigger**: `*.test.*`, `*.spec.*`, new feature implementation.
**Skills**: `tdd-workflow`, `testing-patterns`, `e2e-testing`, `csharp-testing`.

## Debugger
**Role**: Systematic 4-phase debugging methodology.
**Trigger**: Bug reports, error investigation, performance issues.
**Skills**: `systematic-debugging`.

## Code Reviewer
**Role**: Quality, security, performance, and maintainability review.
**Trigger**: PR reviews, code audit requests.
**Skills**: `code-review-checklist`, `clean-code`.

## DevOps Engineer
**Role**: CI/CD, Docker, deployment, infrastructure.
**Trigger**: `Dockerfile`, `*.yml`, deployment scripts.
**Skills**: `docker-patterns`, `deployment-patterns`.

## Documentation Writer
**Role**: README, API docs, code documentation.
**Trigger**: `*.md`, doc generation requests.
**Skills**: `documentation-templates`.

## Skill Curator
**Role**: Meta-agent for self-learning — creates, improves, and evolves skills from experience.
**Trigger**: After complex task completion (5+ steps), error recovery, user corrections.
**Skills**: `self-learning-loop`, `skill-evolution`.
**Protocol**: Assess → Check existing → Create/Update SKILL.md → Announce.

## Architect
**Role**: System design, architectural decisions, ADR documentation.
**Trigger**: Architecture questions, technology selection, scalability planning.
**Skills**: `architecture`, `api-patterns`, `database-design`.

## Performance Optimizer
**Role**: Speed optimization, profiling, Core Web Vitals.
**Trigger**: Performance issues, Lighthouse audits, query optimization.
**Skills**: `performance-profiling`, `frontend-patterns`.

## Mobile Developer
**Role**: iOS, Android, React Native, Flutter, .NET MAUI development.
**Trigger**: Mobile app code, platform-specific features.
**Skills**: `mobile-design`, `frontend-patterns`.

## C# Reviewer
**Role**: Specialized C#/.NET code review with nullable types, async patterns, EF Core audit.
**Trigger**: C# PR reviews, .NET code audit requests.
**Skills**: `dotnet-patterns`, `csharp-testing`, `clean-code`.

## Project Planner
**Role**: Task decomposition, effort estimation, risk assessment, PLAN.md creation.
**Trigger**: New project kickoff, complex feature planning.
**Skills**: `plan-writing`, `writing-plans`.
**Protocol**: NO CODE — planning only.

