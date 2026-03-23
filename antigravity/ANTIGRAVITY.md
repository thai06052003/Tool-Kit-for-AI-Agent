# Antigravity Superpowers Integration

This workspace has the [Superpowers](https://github.com/obra/superpowers) toolkit configured for the Antigravity AI agent.

## Core Rules

1. **Test-Driven Development (TDD) Always:** You must practice TDD when creating or modifying skills and code. Write tests first, watch them fail, write minimal code, watch them pass, and refactor.
2. **Consult Superpowers Skills:** A library of skills exists in the `../superpowers/skills` directory.
   - If a skill might apply to your current task, invoke it and follow its instructions EXACTLY.
   - Do NOT rely on assumptions when a skill exists for the action.
3. **Brainstorming:** Use the `brainstorming` skill when starting a task to refine rough ideas, save the design document, and present it in manageable chunks.
4. **Subagent-Driven Development:** Break tasks into bite-sized segments (2-5 minutes each) and complete them systematically.

## How to use skills in Antigravity

- Check `using-superpowers/SKILL.md` before proceeding with any action.
- Read skill files dynamically as required and map their logic to your toolchain.
- Do not skip workflows or rationalise cutting corners. Follow the exact conditions mapped in the *When to Use* description of the skills.
