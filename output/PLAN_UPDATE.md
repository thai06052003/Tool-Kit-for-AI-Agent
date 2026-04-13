# 📋 PLAN_UPDATE — Kế hoạch nâng cấp Unified AI Toolkit

> Tài liệu lộ trình phát triển, ưu tiên theo phiên bản.
> Cập nhật: 2026-04-13

---

## 🏷️ Phiên bản hiện tại: v2.0

### Đã hoàn thành
- [x] Kiểm kê & loại trùng 5 toolkits (241 agents → 58, 1753 skills → 203)
- [x] Tạo shared/ Single Source of Truth
- [x] Build 6 IDE folders (.agent, .cursor, .vscode, .kiro, .opencode, .vs)
- [x] Root configs: GEMINI.md, .cursorrules, AGENTS.md
- [x] C#/.NET first-class support (dotnet-patterns, csharp-testing, csharp-reviewer)
- [x] Kiro fileMatch steering cho C#, TypeScript, Testing, Security
- [x] VS Code Custom Agents (orchestrator, backend-specialist, code-reviewer, debugger, test-engineer)
- [x] MASTER_CATALOG.md với phân loại 10 danh mục
- [x] README.md tiếng Việt với hướng dẫn sử dụng

---

## 🚀 Phiên bản v2.1 — Ngắn hạn (1-2 tháng)

### Mục tiêu: Automation & Polish

| # | Task | Ưu tiên | Mô tả |
|---|------|---------|-------|
| 1 | **Auto-sync Script** | 🔴 Cao | PowerShell/Bash script: `shared/` → generate 6 IDE folders tự động |
| 2 | **Cursor Hooks** | 🟡 TB | Thêm hooks khi Cursor IDE hỗ trợ (đang preview) |
| 3 | **VS Code agents mở rộng** | 🟡 TB | Thêm: database-architect, security-auditor, devops-engineer, frontend-specialist |
| 4 | **Kiro skills** | 🟡 TB | Convert top skills thành Kiro steering files |
| 5 | **Slim mode** | 🟢 Thấp | Bộ cài nhẹ (~20 skills cốt lõi) cho dự án nhỏ |
| 6 | **OpenCode enrich** | 🟢 Thấp | Thêm commands: `/frontend`, `/database`, `/deploy` |

### Chi tiết kỹ thuật

#### Auto-sync Script (`sync-toolkit.ps1`)
```powershell
# Workflow:
# 1. Đọc shared/
# 2. Transform format theo từng IDE
# 3. Generate output/ tự động
# 4. Validate cấu trúc

param(
    [string]$Source = "shared",
    [string]$Output = "output",
    [switch]$SlimMode
)
```

#### VS Code Agents cần thêm
```
.vscode/agents/
├── orchestrator.md          ✅ Có
├── backend-specialist.md    ✅ Có
├── code-reviewer.md         ✅ Có
├── debugger.md              ✅ Có
├── test-engineer.md         ✅ Có
├── frontend-specialist.md   ⬜ Cần thêm
├── database-architect.md    ⬜ Cần thêm
├── security-auditor.md      ⬜ Cần thêm
└── devops-engineer.md       ⬜ Cần thêm
```

---

## 🎯 Phiên bản v3.0 — Trung hạn (3-6 tháng)

### Mục tiêu: Ecosystem & Integration

| # | Task | Mô tả |
|---|------|-------|
| 1 | **MCP Server** | Server MCP chung cho tất cả IDE — cung cấp tools/resources thống nhất |
| 2 | **Template Generator** | `npx create-unified-toolkit` — scaffold dự án với toolkit đã tích hợp |
| 3 | **Agent Dashboard** | Web UI theo dõi agent usage, skill activation, rule violations |
| 4 | **Mobile Skills** | React Native, Flutter, Swift, Kotlin skills cho mobile-developer agent |
| 5 | **CI/CD Integration** | GitHub Actions workflow kiểm tra toolkit compliance |
| 6 | **IDE Version Detection** | Tự detect IDE version và adjust config accordingly |

### MCP Server Architecture
```
mcp-unified-toolkit/
├── src/
│   ├── tools/
│   │   ├── plan.ts          # /plan command
│   │   ├── review.ts        # /review command
│   │   ├── test.ts          # /test command
│   │   └── security.ts      # /security scan
│   ├── resources/
│   │   ├── agents.ts        # Agent definitions
│   │   ├── skills.ts        # Skill catalog
│   │   └── rules.ts         # Rule sets
│   └── server.ts            # MCP server entry
├── package.json
└── README.md
```

---

## 🌐 Phiên bản v4.0 — Dài hạn (6-12 tháng)

### Mục tiêu: AI-Driven Evolution

| # | Task | Mô tả |
|---|------|-------|
| 1 | **Self-Learning Rules** | AI phân tích codebase → tự đề xuất rules mới |
| 2 | **Cross-IDE Sync** | Cloud-based sync giữa các IDE instances |
| 3 | **Community Marketplace** | Publish/share custom agents, skills, rules |
| 4 | **Multi-Language Agent Teams** | Agents chuyên ngôn ngữ tự phối hợp |
| 5 | **Performance Analytics** | Đo lường hiệu quả AI assistance theo project |
| 6 | **Enterprise Features** | RBAC, audit logs, compliance reporting |

---

## 📊 Metrics & KPIs

### Đo lường thành công

| Metric | v2.0 (hiện tại) | v2.1 (mục tiêu) | v3.0 (mục tiêu) |
|--------|:---:|:---:|:---:|
| IDE được hỗ trợ | 6 | 6 | 6+ |
| Agents hoạt động | 58 | 58 | 65+ |
| Skills chọn lọc | 203 | 203 (+ slim 20) | 250+ |
| Auto-sync | ❌ | ✅ | ✅ |
| MCP Server | ❌ | ❌ | ✅ |
| Template generator | ❌ | ❌ | ✅ |
| Setup time | ~5 phút (copy) | ~1 phút (script) | ~10 giây (npx) |

---

## 🔄 Cách đóng góp

1. Fork repository
2. Thêm skill/agent vào `shared/`
3. Chạy sync script để update IDE folders
4. Submit PR với mô tả chi tiết

---

> **Tạo bởi**: Unified AI Toolkit Orchestrator v2.0
> **Cập nhật**: 2026-04-13
