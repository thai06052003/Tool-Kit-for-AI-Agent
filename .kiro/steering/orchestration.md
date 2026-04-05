---
inclusion: auto
description: Orchestrator-first routing protocol. Routes complex requests through the orchestrator agent for multi-agent coordination.
---

# Orchestrator-First Protocol

## Core Principle

All complex requests that touch multiple domains should be routed through the orchestrator agent for proper analysis, planning, and delegation.

## Routing Logic

| Request Type | Route To | Action |
|-------------|----------|--------|
| Simple question | Direct answer | Respond immediately |
| Single-file fix | Relevant specialist | Fix directly |
| Multi-file change | Orchestrator | Plan → Delegate → Execute |
| New feature | Orchestrator | Requirements → Plan → Implement |
| Security concern | Security reviewer | Scan → Report → Fix |
| Performance issue | Performance optimizer | Profile → Analyze → Optimize |

## Agent Selection

When orchestrating, select agents based on domains touched:

- **Frontend UI/UX**: Use planner → architect → code-reviewer
- **Backend API**: Use planner → architect → code-reviewer → security-reviewer
- **Full Stack**: Use planner → architect → code-reviewer → security-reviewer → e2e-runner
- **Database**: Use planner → database-reviewer → security-reviewer

## Workflow

1. **Analyze** — Decompose task into domain-specific subtasks
2. **Select** — Choose 2-5 agents based on domains affected
3. **Execute** — Invoke agents in logical order
4. **Synthesize** — Combine findings into actionable report
5. **Verify** — Run quality gate before completion

## Quality Gates

Before considering any task complete:
- All tests pass
- No security vulnerabilities
- Code is readable and maintainable
- Documentation is updated (if applicable)
