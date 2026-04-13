# 📋 PLAN_UPDATE — Kế hoạch nâng cấp Unified AI Toolkit

> Lộ trình phát triển, ưu tiên theo phiên bản.
> Cập nhật: 2026-04-13

---

## 🏷️ Phiên bản hiện tại: v2.2 (Hermes-enhanced)

### Đã hoàn thành

| Phase | Nội dung | Trạng thái |
|-------|----------|:---:|
| Kiểm kê | 6 toolkits → MASTER_CATALOG.md | ✅ |
| Loại trùng | 241→59 agents, 1753→322 skills | ✅ |
| SSoT | shared/ với agents/skills/rules/workflows/hooks | ✅ |
| IDE Build | 6 IDE folders đầy đủ | ✅ |
| C#/.NET | dotnet-patterns, csharp-testing, csharp-reviewer | ✅ |
| Hermes Integration | Clone + filter + 117 skills mới | ✅ |
| Self-Learning | self-learning-loop + skill-evolution + skill-curator | ✅ |
| VS Code Agents | 16 Custom Agents (full specialist team) | ✅ |
| Đồng bộ | Self-learning tích hợp vào ALL 6 IDE configs | ✅ |
| Hooks | .agent/hooks/ synced from shared/ | ✅ |
| Root Configs | GEMINI.md, .cursorrules, AGENTS.md (15 agents) | ✅ |
| Docs | README.md + PLAN_UPDATE.md cập nhật | ✅ |

### Thống kê v2.2

| Metric | v2.0 | v2.2 | Thay đổi |
|--------|:---:|:---:|:---:|
| Toolkits gốc | 5 | **6** | +Hermes Agent |
| Agents | 58 | **59** | +skill-curator |
| Skills | 203 | **322** | +117 Hermes + 2 meta |
| VS Code agents | 5 | **16** | +10 chuyên gia |
| VS Code skills | 19 | **31** | +12 Hermes |
| Kiro steering | 7 | **8** | +self-learning |
| Self-Learning | ❌ | **✅** | New feature |
| AGENTS.md agents | 9 | **15** | +6 agents |

---

## 🚀 Phiên bản v2.3 — Ngắn hạn (1-2 tháng)

### Mục tiêu: Automation & Tooling

| # | Task | Ưu tiên | Mô tả |
|---|------|:---:|-------|
| 1 | **Auto-sync Script** | 🔴 | PowerShell/Bash: `shared/` → auto-generate 6 IDE folders |
| 2 | **Slim mode** | 🟡 | Bộ cài nhẹ (~30 skills cốt lõi) cho dự án nhỏ |
| 3 | **Hermes Skills Hub** | 🟡 | CLI kết nối với agentskills.io marketplace |
| 4 | **Version tracking** | 🟡 | `version.json` theo dõi phiên bản skills |
| 5 | **.gitignore template** | 🟢 | Auto-exclude IDE-specific caches |

### Auto-sync Script (chi tiết)
```powershell
# sync-toolkit.ps1
# Workflow: shared/ → transform → output/.*
param(
    [string]$Source = "shared",
    [string]$Output = "output",
    [switch]$SlimMode,
    [switch]$DryRun
)

# 1. Full copy → .agent/, .cursor/
# 2. Selective copy → .vscode/ (top agents + skills)
# 3. Transform → .kiro/ steering, .opencode/ json
# 4. Generate → .vs/ copilot-instructions.md
# 5. Validate structure
```

---

## 🎯 Phiên bản v3.0 — Trung hạn (3-6 tháng)

### Mục tiêu: Ecosystem & Platform

| # | Task | Mô tả |
|---|------|-------|
| 1 | **MCP Server** | Server MCP chung cho tất cả IDE — tools/resources thống nhất |
| 2 | **Template Generator** | `npx create-unified-toolkit` — scaffold dự án |
| 3 | **Agent Dashboard** | Web UI theo dõi agent usage, skill activation |
| 4 | **Mobile Skills** | React Native, Flutter, Swift, Kotlin skills |
| 5 | **CI/CD Integration** | GitHub Actions kiểm tra toolkit compliance |
| 6 | **IDE Version Detection** | Auto-detect IDE và adjust config |

### MCP Server Architecture
```
mcp-unified-toolkit/
├── src/
│   ├── tools/         # /plan, /review, /test, /security
│   ├── resources/     # agents, skills, rules catalog
│   └── server.ts      # MCP server entry
└── package.json
```

---

## 🌐 Phiên bản v4.0 — Dài hạn (6-12 tháng)

### Mục tiêu: AI-Driven Evolution

| # | Task | Mô tả |
|---|------|-------|
| 1 | **Self-Learning v2** | AI phân tích codebase → tự đề xuất rules mới |
| 2 | **Cross-IDE Sync** | Cloud-based sync giữa các IDE instances |
| 3 | **Community Marketplace** | Publish/share custom agents, skills, rules |
| 4 | **Multi-Language Teams** | Agents chuyên ngôn ngữ tự phối hợp |
| 5 | **Performance Analytics** | Đo lường hiệu quả AI assistance |
| 6 | **Enterprise Features** | RBAC, audit logs, compliance |

---

## 📊 KPI Tracking

| Metric | v2.2 ✅ | v2.3 | v3.0 |
|--------|:---:|:---:|:---:|
| IDE hỗ trợ | 6 | 6 | 6+ |
| Agents | 59 | 59 | 65+ |
| Skills | 322 | 322 (+ slim 30) | 400+ |
| Auto-sync | ❌ | ✅ | ✅ |
| MCP Server | ❌ | ❌ | ✅ |
| Self-Learning | ✅ v1 | ✅ v1 | ✅ v2 |
| Setup time | ~5 min (copy) | ~1 min (script) | ~10s (npx) |

---

> **Tạo bởi**: Unified AI Toolkit Orchestrator v2.2
> **Cập nhật**: 2026-04-13
