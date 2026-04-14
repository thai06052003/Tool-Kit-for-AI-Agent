---
inclusion: always
---

# Technology Stack

## Primary Languages
- **C# / .NET 8+**: Backend services, APIs, domain logic
- **TypeScript / React / Next.js**: Frontend applications
- **Python 3.11+**: Scripting, data processing, APIs
- **SQL (PostgreSQL, SQL Server)**: Data persistence

## Backend Frameworks
- ASP.NET Core (Minimal API + Controllers)
- Entity Framework Core (Code-First migrations)
- MediatR (CQRS when needed)
- FluentValidation (Request validation)

## Frontend Frameworks
- React 18+ with Server Components
- Next.js 14+ (App Router)
- Tailwind CSS v4
- Vite for non-Next.js apps

## Testing
- xUnit + FluentAssertions + Moq (C#)
- Vitest / Jest (TypeScript)
- Pytest (Python)
- Playwright (E2E)

## DevOps
- Docker & Docker Compose
- GitHub Actions / Azure DevOps
- Terraform (IaC when applicable)

## Conventions
- **Formatting**: dotnet format, Prettier, Black, gofmt
- **Commits**: Conventional Commits (feat/fix/refactor/test/docs)
- **Branching**: Trunk-based with short-lived feature branches
