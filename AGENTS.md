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
**Skills**: `dotnet-backend`, `csharp-pro`, `ef-core`, `aspnet-minimal-api-openapi`, `api-design`, `backend-patterns`, `database-design`, `hexagonal-architecture`.

## Frontend Specialist
**Role**: React, Next.js, Tailwind CSS, UI/UX design.
**Trigger**: `*.tsx`, `*.css`, component architecture, design systems.
**Skills**: `nextjs-best-practices`, `react-best-practices`, `vuejs-patterns`, `angular-ui-patterns`, `tailwind-design-system`, `app-list`, `app-create`, `app-show`, `app-edit`, `app-button`, `refine-framework`, `ui-skills`, `frontend-design`, `taste-skill`, `brutalist-skill`, `minimalist-skill`, `soft-skill`, `redesign-skill`.

## Database Architect
**Role**: Schema design, EF Core migrations, query optimization, indexing.
**Trigger**: `*.sql`, migration files, DbContext changes.
**Skills**: `database-design`, `postgres-best-practices`, `database-migrations`, `sql-optimization`, `ef-core`.

## Security Auditor
**Role**: OWASP Top 10 review, vulnerability scanning, auth patterns.
**Trigger**: Auth code, input handling, API endpoints, dependency updates.
**Skills**: `security-review`, `vulnerability-scanner`, `auth-implementation-patterns`, `api-security-best-practices`.

## Test Engineer
**Role**: TDD, unit/integration/E2E testing.
**Trigger**: `*.test.*`, `*.spec.*`, new feature implementation.
**Skills**: `tdd-workflow`, `testing-patterns`, `e2e-testing`, `csharp-testing`, `playwright-skill`.

## Debugger
**Role**: Systematic 4-phase debugging methodology.
**Trigger**: Bug reports, error investigation, performance issues.
**Skills**: `systematic-debugging`, `debugger`, `debugging-strategies`, `error-handling-patterns`.

## Code Reviewer
**Role**: Quality, security, performance, and maintainability review.
**Trigger**: PR reviews, code audit requests.
**Skills**: `code-review-checklist`, `clean-code`, `code-refactoring-refactor-clean`.

## DevOps Engineer
**Role**: CI/CD, Docker, deployment, infrastructure.
**Trigger**: `Dockerfile`, `*.yml`, deployment scripts.
**Skills**: `docker-patterns`, `deployment-patterns`, `cicd-automation-workflow-automate`, `github-actions-templates`.

## Documentation Writer
**Role**: README, API docs, code documentation.
**Trigger**: `*.md`, doc generation requests.
**Skills**: `documentation-templates`, `api-documentation`, `readme`, `docs-architect`.

## Skill Curator
**Role**: Meta-agent for self-learning — creates, improves, and evolves skills from experience.
**Trigger**: After complex task completion (5+ steps), error recovery, user corrections.
**Skills**: `local-skill-searcher`, `skill-evolution`, `skill-creator`, `continuous-learning`.
**Protocol**: Assess → Check existing → Create/Update SKILL.md → Dual-save to `output/` and `level-up/output/` → Announce.

## Architect
**Role**: System design, architectural decisions, ADR documentation.
**Trigger**: Architecture questions, technology selection, scalability planning.
**Skills**: `architecture`, `api-patterns`, `database-design`, `agent-memory-systems`, `ai-agents-architect`, `airflow-dag-patterns`, `android-clean-architecture`, `architecture-blueprint-generator`, `architecture-patterns`, `autonomous-agent-patterns`, `autoresearch`, `bash-defensive-patterns`, `binary-analysis-patterns`, `breakdown-epic-arch`, `c4-architecture-c4-architecture`, `c4-code`, `c4-container`, `c4-context`, `context7-auto-research`, `dart-flutter-patterns`, `ddd-context-mapping`, `ddd-tactical-patterns`, `deep-research`, `discord-bot-architect`, `dotnet-architect`, `email-systems`, `exa-search`, `filesystem-context`, `gif-search`, `graphql-architect`, `gtm-developer-ecosystem`, `gtm-partnership-architecture`, `healthcare-emr-patterns`, `hierarchical-agent-memory`, `hig-patterns`, `hybrid-search-implementation`, `jpa-patterns`, `kotlin-exposed-patterns`, `kotlin-ktor-patterns`, `kotlin-patterns`, `kubernetes-architect`, `langchain-architecture`, `linkerd-patterns`, `llm-app-patterns`, `market-research`, `mcp-server-patterns`, `memory-safety-patterns`, `memory-systems`, `microservices-patterns`, `monorepo-architect`, `multi-agent-patterns`, `n8n-workflow-patterns`, `nestjs-patterns`, `nextjs-app-router-patterns`, `nx-workspace-patterns`, `on-call-handoff-patterns`, `perl-patterns`, `projection-patterns`, `prompt-engineering-patterns`, `pytorch-patterns`, `research`, `research-paper-writing`, `robius-app-architecture`, `robius-widget-patterns`, `search-first`, `senior-architect`, `similarity-search-patterns`, `site-architecture`, `software-architecture`, `springboot-patterns`, `stride-analysis-patterns`, `unity-ecs-patterns`, `wcag-audit-patterns`, `workflow-orchestration-patterns`, `workflow-patterns`.

## Performance Optimizer
**Role**: Speed optimization, profiling, Core Web Vitals.
**Trigger**: Performance issues, Lighthouse audits, query optimization.
**Skills**: `performance-profiling`, `frontend-patterns`, `agent-orchestration-multi-agent-optimize`, `az-cost-optimize`, `claude-speed-reader`, `connections-optimizer`, `cost-aware-llm-pipeline`, `cost-optimization`, `dx-optimizer`, `llm-application-dev-prompt-optimize`, `llm-prompt-optimizer`, `odoo-inventory-optimizer`, `prompt-optimizer`, `speed`.

## Mobile Developer
**Role**: iOS, Android, React Native, Flutter, .NET MAUI development.
**Trigger**: Mobile app code, platform-specific features.
**Skills**: `mobile-design`, `frontend-patterns`, `android-jetpack-compose-expert`, `create-spring-boot-kotlin-project`, `expo-dev-client`, `flutter-expert`, `ios-developer`, `kotlin-coroutines-expert`, `kotlin-coroutines-flows`, `kotlin-mcp-server-generator`, `kotlin-springboot`, `mobile-developer`, `mobile-games`, `swift-actor-persistence`, `swift-concurrency-6-2`, `swift-mcp-server-generator`, `upgrading-expo`.

## C# Reviewer
**Role**: Specialized C#/.NET code review with nullable types, async patterns, EF Core audit.
**Trigger**: C# PR reviews, .NET code audit requests.
**Skills**: `dotnet-patterns`, `csharp-testing`, `clean-code`, `csharp-async`, `csharp-mcp-server-generator`, `csharp-pro`, `csharp-tunit`, `dotnet-best-practices`, `dotnet-timezone`, `dotnet-upgrade`, `ef-core`, `m365-agents-dotnet`.

## Project Planner
**Role**: Task decomposition, effort estimation, risk assessment, PLAN.md creation.
**Trigger**: New project kickoff, complex feature planning.
**Skills**: `plan-writing`, `writing-plans`, `ai-agent-development`, `ai-product`, `ai-wrapper-product`, `analytics-product`, `avalonia-zafiro-development`, `breakdown-epic-pm`, `breakdown-feature-implementation`, `breakdown-feature-prd`, `breakdown-plan`, `bun-development`, `claude-win11-speckit-update-skill`, `codebase-inspection`, `context-driven-development`, `create-github-issues-feature-from-implementation-plan`, `create-implementation-plan`, `development`, `electron-development`, `executing-plans`, `finishing-a-development-branch`, `game-development`, `gen-specs-as-issues`, `gtm-enterprise-account-planning`, `gtm-product-led-growth`, `inventory-demand-planning`, `office-productivity`, `plan`, `plankton-code-quality`, `planning-with-files`, `product-inventor`, `product-lens`, `product-manager`, `product-manager-toolkit`, `product-marketing-context`, `production-code-audit`, `production-scheduling`, `productivity`, `project-development`, `salesforce-development`, `shopify-development`, `software-development`, `spec-to-code-compliance`, `speckit-updater`, `structured-autonomy-plan`, `subagent-driven-development`, `typespec-create-agent`, `update-implementation-plan`, `voice-ai-development`, `voice-ai-engine-development`, `wordpress-plugin-development`, `wordpress-theme-development`, `wordpress-woocommerce-development`.
**Protocol**: NO CODE — planning only.

