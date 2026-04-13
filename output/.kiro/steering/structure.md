---
inclusion: always
---

# Project Structure

## Repository Layout
```
project-root/
├── .agent/              # Antigravity IDE config
├── .cursor/             # Cursor IDE config
├── .vscode/             # VS Code config
├── .kiro/               # Kiro IDE config (this)
│   ├── steering/        # Context files
│   └── skills/          # On-demand skills
├── .opencode/           # OpenCode config
├── .vs/                 # Visual Studio config
├── shared/              # Single Source of Truth
│   ├── agents/          # All agent definitions
│   ├── skills/          # All skill definitions
│   ├── rules/           # Language-specific rules
│   ├── workflows/       # Workflow definitions
│   └── hooks/           # Event hooks
├── src/                 # Source code
├── tests/               # Test projects
├── docs/                # Documentation
├── GEMINI.md            # Antigravity root config
├── .cursorrules         # Cursor root config
└── README.md            # Project documentation
```

## Naming Conventions
- **C#**: PascalCase for types/methods, _camelCase for private fields
- **TypeScript**: camelCase for variables/functions, PascalCase for types
- **Python**: snake_case for variables/functions, PascalCase for classes
- **Files**: kebab-case for config files, PascalCase for C# files

## Import Ordering
1. System/Framework imports
2. Third-party libraries
3. Internal/project imports
4. Relative imports

## Architecture Decisions
- Clean Architecture for .NET services
- Feature-based folder structure for frontend
- Repository Pattern for data access
- Mediator Pattern for cross-cutting concerns
