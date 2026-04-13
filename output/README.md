# 🤖 Unified AI Agent Toolkit v2.0

> **Hệ thống cấu hình AI Agent thống nhất cho 6 IDE** — Một nguồn duy nhất, đồng bộ mọi nơi.

---

## 📋 Mục lục

1. [Tổng quan](#-tổng-quan)
2. [Cấu trúc thư mục](#-cấu-trúc-thư-mục)
3. [Hướng dẫn sử dụng theo IDE](#-hướng-dẫn-sử-dụng-theo-ide)
4. [Bảng thống kê](#-bảng-thống-kê)
5. [Ma trận khả năng IDE](#-ma-trận-khả-năng-ide)
6. [Điểm mạnh](#-điểm-mạnh)
7. [Hạn chế hiện tại](#-hạn-chế-hiện-tại)
8. [Ví dụ sử dụng](#-ví-dụ-sử-dụng)
9. [Kế hoạch nâng cấp](#-kế-hoạch-nâng-cấp)

---

## 🎯 Tổng quan

### Mục đích

Dự án này **hợp nhất 5 bộ AI Agent Toolkit** khác nhau thành **1 hệ thống cấu hình chuẩn hóa**, giúp developer có thể:

- Copy 1 lần → Hoạt động tự động trên bất kỳ IDE nào
- Đảm bảo AI assistant luôn tuân thủ cùng 1 bộ quy tắc, bất kể IDE
- Tận dụng tối đa tính năng riêng của từng IDE (agents, steering, hooks...)

### Nguồn gốc

| # | Toolkit nguồn | Đóng góp chính |
|---|---|---|
| 1 | **antigravity-kit** | 20 agents gốc, 65 skills, 11 workflows, Socratic Gate |
| 2 | **everything-claude-code (ECC)** | 37 agents, 138+ skills, 89 rule files theo ngôn ngữ |
| 3 | **superpowers** | TDD workflow, git worktrees, verification loop, parallel agents |
| 4 | **awesome-copilot** | 182 agents, 173 instructions cho Copilot |
| 5 | **antigravity-awesome-skills** | 1300+ skills chuyên biệt |

### Kết quả sau khi hợp nhất

| Loại | Thô (5 toolkit) | Sau xử lý | Tỉ lệ tối ưu |
|------|-----------------|-----------|---------------|
| **Agents** | 241 | 58 (shared) | -76% |
| **Skills** | 1,753 | 203 (shared) | -88% |
| **Rules** | 189 | 89 files | -53% |
| **Workflows** | 86 | 11 | -87% |
| **Hooks** | 10 | 4 | -60% |

---

## 📁 Cấu trúc thư mục

```
output/
├── 📄 GEMINI.md              ← Root config cho Antigravity
├── 📄 .cursorrules            ← Root config cho Cursor
├── 📄 AGENTS.md               ← Chuẩn AGENTS.md cho Kiro & OpenCode
│
├── 🔷 shared/                 ← SINGLE SOURCE OF TRUTH
│   ├── agents/    (58 files)  ← Tất cả agent definitions
│   ├── skills/    (203 dirs)  ← Tất cả skill SKILL.md
│   ├── rules/     (89 files)  ← Rules theo ngôn ngữ (csharp/, typescript/...)
│   ├── workflows/ (11 files)  ← Workflow definitions
│   └── hooks/     (4 files)   ← Event hooks
│
├── 🟢 .agent/                 ← Antigravity IDE
│   ├── agents/    (58 files)
│   ├── skills/    (203 dirs)
│   ├── workflows/ (11 files)
│   └── scripts/              ← Verify scripts
│
├── 🟡 .cursor/                ← Cursor IDE
│   ├── rules/     (89 files)  ← Language-specific rules
│   └── skills/    (203 dirs)  ← On-demand skills
│
├── 🔵 .vscode/                ← Visual Studio Code
│   ├── agents/    (5 files)   ← Custom Agents (orchestrator, backend, etc.)
│   ├── skills/    (19 dirs)   ← Core skills
│   ├── copilot-instructions.md
│   └── settings.json
│
├── 🟣 .kiro/                  ← Kiro IDE
│   └── steering/  (7 files)   ← Steering files with fileMatch modes
│       ├── product.md         ← Always included
│       ├── tech.md            ← Always included
│       ├── structure.md       ← Always included
│       ├── csharp-standards.md ← Auto for *.cs files
│       ├── typescript-standards.md ← Auto for *.ts/*.tsx
│       ├── testing-standards.md ← Auto for *.test.* 
│       └── security-audit.md  ← Auto-include on security context
│
├── ⚪ .opencode/              ← OpenCode
│   ├── opencode.json          ← Config with 6 commands
│   └── AGENTS.md              ← Agent routing
│
├── 🔴 .vs/                    ← Visual Studio
│   └── copilot-instructions.md ← C#/.NET focused instructions
│
└── 📚 docs/
    └── MASTER_CATALOG.md      ← Kiểm kê chi tiết toàn bộ
```

---

## 🚀 Hướng dẫn sử dụng theo IDE

### Antigravity

1. Copy toàn bộ folder `.agent/` và file `GEMINI.md` vào root dự án
2. Mở dự án bằng Antigravity → AI tự động nhận agents, skills, workflows
3. Sử dụng: `@orchestrator`, `@backend-specialist`, `/plan`, `/debug`, v.v.

### Cursor

1. Copy folder `.cursor/` và file `.cursorrules` vào root dự án
2. Mở dự án bằng Cursor → Rules tự động load theo ngôn ngữ
3. Skills được reference tự động khi cần

### Visual Studio Code

1. Copy folder `.vscode/` vào root dự án
2. Đảm bảo GitHub Copilot extension đã cài (với Agent Mode)
3. Custom Agents xuất hiện khi dùng `@agent-name` trong chat
4. Copilot instructions tự động áp dụng

### Kiro

1. Copy folder `.kiro/` và file `AGENTS.md` vào root dự án
2. Mở bằng Kiro → Steering files tự động load
3. Mở file `.cs` → C# standards tự kích hoạt (fileMatch)
4. Mở file `.tsx` → TypeScript standards tự kích hoạt
5. Gõ `#security-audit` trong chat để load manual steering

### OpenCode

1. Copy folder `.opencode/` vào root dự án
2. Sử dụng commands: `/plan`, `/review`, `/test`, `/debug`, `/security`, `/dotnet`

### Visual Studio

1. Copy folder `.vs/` vào root dự án (hoặc solution folder)
2. Copilot instructions tối ưu cho C#/.NET sẽ tự áp dụng
3. Hỗ trợ: Clean Architecture, EF Core, xUnit, Minimal API

---

## 📊 Bảng thống kê

### Agents theo danh mục

| Danh mục | Số lượng | Agents chính |
|----------|----------|-------------|
| Orchestration & Planning | 4 | orchestrator, project-planner, chief-of-staff, explorer-agent |
| Code Quality & Review | 4 | code-reviewer, refactor-cleaner, code-archaeologist, architect |
| Security | 3 | security-auditor, penetration-tester, healthcare-reviewer |
| Testing & TDD | 4 | test-engineer, tdd-guide, e2e-runner, qa-automation-engineer |
| Frontend & UI/UX | 2 | frontend-specialist, flutter-reviewer |
| Backend & API | 3 | backend-specialist, database-architect, docs-lookup |
| Language-Specific | 12 | typescript-reviewer, python-reviewer, csharp-reviewer, go/rust/java/kotlin... |
| DevOps | 2 | devops-engineer, build-error-resolver |
| Documentation | 2 | documentation-writer, doc-updater |
| Specialized | 8 | game-developer, mobile-developer, performance-optimizer, seo-specialist... |

### Skills theo danh mục

| Danh mục | Số lượng | Ví dụ |
|----------|----------|-------|
| Core (luôn cần) | 10 | clean-code, coding-standards, security-review, tdd-workflow |
| Frontend | 5 | frontend-design, frontend-patterns, tailwind-patterns |
| Backend | 7 | api-design, dotnet-patterns, nodejs-best-practices, database-design |
| Testing | 5 | testing-patterns, e2e-testing, csharp-testing |
| Language-Specific | 7 | python-patterns, golang-patterns, rust-pro |
| Workflow | 14 | plan-writing, executing-plans, git-workflow, verification-loop |
| Specialized | 17+ | game-development, mcp-builder, seo-fundamentals, i18n-localization |
| ECC Extended | 138+ | django-patterns, laravel-patterns, springboot-patterns, swift... |

---

## 🗺️ Ma trận khả năng IDE

| Tính năng | Antigravity | Cursor | VS Code | Kiro | OpenCode | VS |
|-----------|:-----------:|:------:|:-------:|:----:|:--------:|:--:|
| **Agents** | ✅ Full | ⚡ Rules | ✅ Custom | ✅ AGENTS.md | ✅ AGENTS.md | ❌ |
| **Subagents** | ✅ Built-in | ❌ | ✅ Native | ❌ | ❌ | ❌ |
| **Skills** | ✅ Full | ✅ Full | ✅ Agent Skills | ❌ | ❌ | ❌ |
| **Rules** | ✅ GEMINI.md | ✅ .cursorrules | ✅ Instructions | ✅ Steering | ⚡ AGENTS.md | ⚡ Instructions |
| **Workflows** | ✅ /slash | ❌ | ❌ | ❌ | ⚡ Commands | ❌ |
| **Hooks** | ✅ Native | ❌ | ✅ Native | ✅ Native | ❌ | ❌ |
| **fileMatch** | ❌ | ❌ | ❌ | ✅ Native | ❌ | ❌ |
| **MCP** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **C#/.NET Focus** | ⚡ Skill | ⚡ Rules | ⚡ Agent | ✅ Steering | ⚡ Command | ✅ Full |

> ✅ = Hỗ trợ đầy đủ | ⚡ = Hỗ trợ qua workaround | ❌ = Không hỗ trợ

---

## 💪 Điểm mạnh

### 1. Single Source of Truth (SSoT)
- Folder `shared/` chứa bản gốc duy nhất
- Mọi IDE folder đều derive từ `shared/`
- Thay đổi 1 nơi → cập nhật tất cả

### 2. Đồng nhất từ gốc
- 5 toolkit → 1 bộ tinh hoa đã loại trùng
- Agents merged: lấy ưu điểm nhất từ mỗi nguồn
- Skills chọn lọc theo chất lượng

### 3. IDE-Aware Adaptation
- Tận dụng tính năng riêng của từng IDE
- Kiro: fileMatch steering (tự load C# rules khi mở .cs)
- VS Code: Custom Agents + Copilot Instructions + Hooks
- Cursor: Language-specific rules directory
- Visual Studio: C#/.NET optimized instructions

### 4. C#/.NET First-Class Support
- Skill `dotnet-patterns` với async/await, DI, EF Core, Minimal API
- Skill `csharp-testing` với xUnit, FluentAssertions, Moq
- Agent `csharp-reviewer` chuyên review code C#
- Agent `backend-specialist` tích hợp cả C# và Node.js
- Rules `csharp/` với 5 files: coding-style, patterns, security, testing, hooks

### 5. Orchestrator-First Protocol
- Socratic Gate: Hỏi trước khi làm
- Plan → Execute → Verify
- Multi-agent coordination

---

## ⚠️ Hạn chế hiện tại

| # | Hạn chế | Ảnh hưởng | Mức độ |
|---|---------|-----------|--------|
| 1 | VS không hỗ trợ Custom Agents | Chỉ dùng copilot-instructions.md | Trung bình |
| 2 | Cursor không hỗ trợ Subagents native | Phải mô phỏng qua rules | Thấp |
| 3 | OpenCode hạn chế tính năng | Chỉ có AGENTS.md + commands | Trung bình |
| 4 | shared/ chứa nhiều skill chuyên biệt | Có thể bloat dự án nhỏ | Thấp |
| 5 | Chưa có auto-sync script | Cần copy thủ công khi update | Trung bình |
| 6 | Kiro không hỗ trợ skills folder | Phải dùng steering thay thế | Thấp |

---

## 📝 Ví dụ sử dụng

### Ví dụ 1: Tạo API endpoint mới (C#)

**Trong Antigravity:**
```
@backend-specialist Tạo endpoint GET /api/orders/{id} với EF Core
```

**Trong Cursor:**
AI tự động load `.cursor/rules/csharp/` khi bạn mở file `.cs` và viết code theo patterns.

**Trong Kiro:**
Mở file `OrdersController.cs` → Steering `csharp-standards.md` tự kích hoạt → AI viết code theo chuẩn.

### Ví dụ 2: Debug lỗi N+1 Query

**Trong VS Code:**
```
@debugger Ứng dụng chậm khi load danh sách orders
```
→ Debugger agent tự động theo 4-phase methodology: Observe → Hypothesize → Test → Fix.

### Ví dụ 3: Review code trước khi merge

**Trong OpenCode:**
```
/review
```
→ Code reviewer kiểm tra Security + Performance + Maintainability + Testing.

---

## 🔮 Kế hoạch nâng cấp

> Chi tiết tại [PLAN_UPDATE.md](PLAN_UPDATE.md)

### Ngắn hạn (v2.1)
- Auto-sync script: Từ `shared/` → generate 6 IDE folders tự động
- Thêm hooks cho Cursor (khi Cursor hỗ trợ)
- Mở rộng VS Code agents (thêm database-architect, devops-engineer)

### Trung hạn (v3.0)
- MCP Server tích hợp cho tất cả IDE
- Template generator: `npx create-unified-toolkit`
- Dashboard web theo dõi agent usage
- Thêm Android/iOS skills cho mobile-developer agent

### Dài hạn (v4.0)
- AI tự đề xuất rules mới dựa trên codebase
- Cross-IDE sync qua cloud
- Marketplace cho community skills

---

## 📄 Giấy phép

MIT License — Tự do sử dụng, sao chép, chỉnh sửa.

---

> **Tạo bởi**: Unified AI Toolkit Orchestrator v2.0
> **Cập nhật**: 2026-04-13
> **Nguồn**: 5 toolkit × 6 IDE → 1 hệ thống thống nhất
