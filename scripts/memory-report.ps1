# memory-report.ps1 - Unified AI Toolkit Memory Reporting Utility
# Version: 1.0.0

Write-Host "Generating Graph Memory Report (Mem0)..." -ForegroundColor Cyan

$ReportPath = "./current_memory_report.md"

# Logic: This script serves as a trigger and instruction file.
# Since the actual query happens inside the AI Agent using MCP tools, 
# this script creates a task file that the agent will see and act upon.

$ReportContent = @"
# 🧠 Graph Memory Report (Requested)
Generated: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")

### Instructions for Agent:
1. Use the `search_memories` tool from Mem0 MCP with an empty query or top-level keywords.
2. Summarize the key entities, relationships, and user preferences found.
3. List the most recent 10 learned facts.
4. Output the results below.

### [Agent Output Starts Here]
"@

$ReportContent | Out-File -FilePath $ReportPath -Encoding utf8

Write-Host "Report template created at $ReportPath." -ForegroundColor Yellow
Write-Host "Please ask your AI Agent: '@memory-manager hoàn thiện báo cáo memory-report.ps1'" -ForegroundColor Green
