---
name: project-scanning
description: Pattern for extracting large-scale C# ASP.NET Boilerplate codebase information into a context document.
author: Orchestrator
version: 1.0.0
---

# Project Scanning Pattern

## Overview
When tasked with scanning a 100% of a massive codebase (like ABP Framework applications with hundreds of endpoints and entities) to build an `analyst-context-project.md` file, relying on manual agent reading or slow `cat`/`ls` tools is inefficient and will exceed context windows. 

## Procedure
1. **Automate Extraction**: Write a lightweight script (Python or PowerShell) that uses Regex or AST parsing to traverse the `.cs` files.
2. **Extract Key Components**:
    - Classes
    - Public Methods (Virtual, Async, Overrides)
    - API Endpoints (e.g., `[HttpGet]`, `[HttpPost]`)
3. **Generate Markdown Structure**:
    - Overview of the Architecture
    - Detailed Class & Call Graph breakdown
    - Core Flows (identified manually or via routing analysis)
    - Tech Debt & Security notes
4. **Final Checklist**:
    - Always run `security_scan` and `lint_runner` if applicable, although for large projects these may take a long time and should be run asynchronously.

## Pitfalls
- **Context Limit Exceeded**: Avoid writing the entire source code to a file. Focus only on signatures and annotations.
- **Script Timeout**: Limit the scope or write robust exception handling in the script to ensure the report generation finishes even if some files are corrupted.
- **Regex Limitations**: Simple Regex might miss complex signatures, but it is much faster than full AST parsing for quick context gathering.
