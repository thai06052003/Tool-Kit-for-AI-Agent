# 🧰 Unified AI Agent Toolkit v2.2

> **Bộ công cụ AI Agent hợp nhất** — Drop-in configs cho 6 IDE.
> Copy folder tương ứng vào dự án → AI tự động hoạt động, tự học, và ngày càng thông minh hơn.

---

## 📖 Mục lục

1. [Tổng quan](#-tổng-quan)
2. [Nguồn gốc & Phương pháp](#-nguồn-gốc--phương-pháp)
3. [Cấu trúc thư mục](#-cấu-trúc-thư-mục)
4. [Thống kê chi tiết](#-thống-kê-chi-tiết)
5. [Hướng dẫn sử dụng từng IDE](#-hướng-dẫn-sử-dụng-từng-ide)
6. [Self-Learning Protocol](#-self-learning-protocol-hermes-inspired)
7. [Shared — Single Source of Truth](#-shared--single-source-of-truth)
8. [Điểm mạnh & Hạn chế](#-điểm-mạnh--hạn-chế)
9. [Ví dụ thực tế](#-ví-dụ-thực-tế)
10. [Kế hoạch nâng cấp](#-kế-hoạch-nâng-cấp)

---

## 🎯 Tổng quan

Dự án này hợp nhất **6 bộ AI toolkit** thành **1 hệ thống cấu hình chuẩn hóa** cho **6 IDE**, với kiến trúc **Single Source of Truth** (SSoT). Mọi IDE đều chia sẻ cùng kiến thức nhưng được adapt sang đúng format native.

### Tính năng nổi bật
- 🤖 **59 agents chuyên biệt** (orchestrator, backend, frontend, security, debugger...)
- 📚 **322 skills** (bao gồm 117 skills từ Hermes Agent)
- 🧠 **Self-Learning Protocol** — AI tự tạo skills mới từ kinh nghiệm (Hermes-inspired)
- 🔒 **OWASP Top 10** tích hợp sẵn trong security-auditor
- 🎯 **C#/.NET first-class support** (Clean Architecture, EF Core, xUnit)
- 📦 **Zero-Config** — Copy-Paste là hoạt động ngay

---

## 🔬 Nguồn gốc & Phương pháp

### 6 Toolkits đã hợp nhất

| # | Toolkit | Đóng góp chính |
|---|---------|----------------|
| 1 | **antigravity-kit** | Agents, skills, workflows, hooks — nền tảng Antigravity |
| 2 | **everything-claude-code (ECC)** | 203 skills + dotnet-patterns, TDD workflow |
| 3 | **superpowers** | TDD, planning, subagent coordination |
| 4 | **awesome-copilot** | 182+ agents, 173+ instructions |
| 5 | **antigravity-awesome-skills** | 1293+ community skills |
| 6 | **hermes-agent** (NousResearch) | Self-learning loop, 117 skills, skill-evolution |

### Phương pháp
1. **Kiểm kê** — Thu thập toàn bộ từ 6 nguồn
2. **Loại trùng** — 241→59 agents, 1753→322 skills, 189→89 rules
3. **Phân loại** — 10 danh mục chuẩn
4. **Tạo SSoT** — `shared/` folder chứa bản đầy đủ nhất
5. **Adapt IDE** — Transform format cho từng IDE
6. **Self-Learning** — Tích hợp Hermes self-improving protocol

---

## 📂 Cấu trúc thư mục (`output/`)

```
output/
├── shared/                    ← 🧠 Single Source of Truth (KHÔNG IDE nào đọc trực tiếp)
│   ├── agents/     (59 files) ← Tất cả agent definitions
│   ├── skills/     (322 dirs) ← Tất cả skills (SKILL.md format)
│   ├── rules/      (89 files) ← Rules theo ngôn ngữ (14 ngôn ngữ)
│   ├── workflows/  (11 files) ← Workflow definitions
│   └── hooks/      (4 files)  ← Hook scripts
│
├── .agent/                    ← Antigravity IDE (full sync từ shared/)
│   ├── agents/     (59 files)
│   ├── skills/     (322 dirs)
│   ├── workflows/  (11 files)
│   └── hooks/      (4 files)
│
├── .cursor/                   ← Cursor IDE
│   ├── rules/      (89 files) ← Language-specific rules
│   ├── skills/     (322 dirs)
│   └── hooks/                 ← Cursor hooks integration
│
├── .vscode/                   ← Visual Studio Code
│   ├── agents/     (16 files) ← Custom Agents (copilot agent mode)
│   ├── skills/     (31 dirs)  ← Chọn lọc skills quan trọng nhất
│   ├── copilot-instructions.md
│   └── settings.json
│
├── .kiro/                     ← Kiro IDE
│   └── steering/   (8 files)  ← Auto-loaded rules (fileMatch)
│
├── .opencode/                 ← OpenCode
│   ├── opencode.json          ← 6 commands (/plan, /review, /test...)
│   └── AGENTS.md              ← Agent definitions
│
├── .vs/                       ← Visual Studio
│   └── copilot-instructions.md ← C#/.NET focused
│
├── docs/
│   └── MASTER_CATALOG.md      ← Kiểm kê chi tiết gốc
│
├── GEMINI.md                  ← Root config cho Antigravity
├── .cursorrules               ← Root config cho Cursor
├── AGENTS.md                  ← Root config cho Kiro/OpenCode (15 agents)
├── hermes-config.yaml.example ← Template config cho Hermes Agent
├── README.md                  ← Tài liệu này
└── PLAN_UPDATE.md             ← Lộ trình nâng cấp
```

---

## 📊 Thống kê chi tiết

### Tổng quát

| Metric | Số lượng |
|--------|:---:|
| Agents | 59 |
| Skills | 322 |
| Rules | 89 (14 ngôn ngữ) |
| Workflows | 11 |
| Hooks | 4 |
| IDE được hỗ trợ | 6 |
| Toolkits gốc | 6 |

### Chi tiết theo IDE

| IDE | Agents | Skills | Rules/Steering | Configs | Self-Learning |
|-----|:---:|:---:|:---:|:---:|:---:|
| **Antigravity** (.agent/) | 59 | 322 | — | GEMINI.md | ✅ |
| **Cursor** (.cursor/) | — | 322 | 89 | .cursorrules | ✅ |
| **VS Code** (.vscode/) | 16 | 31 | — | copilot-instructions.md, settings.json | ✅ |
| **Kiro** (.kiro/) | — | — | 8 steering | AGENTS.md | ✅ |
| **OpenCode** (.opencode/) | — | — | — | opencode.json, AGENTS.md | ✅ |
| **Visual Studio** (.vs/) | — | — | — | copilot-instructions.md | ✅ |

### Skills theo Category (top 10)

| Category | Số lượng | Ví dụ |
|----------|:---:|-------|
| Software Development | 42 | plan, tdd, debugging, code-review |
| DevOps | 28 | docker, deployment, CI/CD |
| Security | 19 | OWASP, vulnerability-scanner, 1password |
| MLOps / AI | 35 | axolotl, vllm, pytorch, dspy |
| Frontend | 22 | react, tailwind, frontend-design |
| Backend | 18 | dotnet-patterns, api-design, golang |
| Database | 12 | postgres, migrations, schema-design |
| GitHub | 8 | pr-workflow, code-review, issues |
| Creative | 15 | excalidraw, p5js, songwriting |
| Research | 11 | arxiv, deep-research, polymarket |

---

## 🚀 Hướng dẫn sử dụng từng IDE

### 1. Antigravity IDE ⭐ (Đầy đủ nhất)
```bash
# Copy vào project root:
cp -r output/.agent/ your-project/
cp output/GEMINI.md your-project/

# Sử dụng:
/orchestrate <yêu cầu phức tạp>
/plan <lên kế hoạch>
/debug <phân tích lỗi>
```

### 2. Cursor IDE
```bash
cp -r output/.cursor/ your-project/
cp output/.cursorrules your-project/

# Cursor tự động đọc rules. Mở Chat/Composer để dùng.
```

### 3. Visual Studio Code
```bash
cp -r output/.vscode/ your-project/

# GitHub Copilot Agent Mode → tự nhận diện copilot-instructions.md
# Sử dụng custom agents: @orchestrator, @backend-specialist, @debugger...
```

### 4. Kiro IDE
```bash
cp -r output/.kiro/ your-project/
cp output/AGENTS.md your-project/

# Kiro tự load steering files dựa trên fileMatch.
# Mở file .cs → C# standards tự active.
```

### 5. OpenCode
```bash
cp -r output/.opencode/ your-project/

# Dùng commands: /plan, /review, /test, /debug, /security, /dotnet
```

### 6. Visual Studio
```bash
cp -r output/.vs/ your-project/

# GitHub Copilot tự đọc copilot-instructions.md
# Focus sâu: C#/.NET, Clean Architecture, EF Core, xUnit
```

### 7. Hermes Agent (Bonus)
```bash
# Copy template config:
cp output/hermes-config.yaml.example ~/.hermes/config.yaml

# External dirs trỏ vào shared/skills → Hermes dùng ngay 322 skills!
```

### Dùng tất cả IDE cùng lúc
```bash
# Copy toàn bộ output/ vào project:
cp -r output/* your-project/
cp -r output/.* your-project/   # Đừng quên hidden folders
```

---

## 🧠 Self-Learning Protocol (Hermes-inspired)

Đây là tính năng **game-changer** — AI tự tạo skills mới từ kinh nghiệm:

### Cách hoạt động
1. Sau khi hoàn thành task phức tạp (5+ bước), AI tự đánh giá skill-worthiness
2. Nếu đáng lưu → viết `SKILL.md` với YAML frontmatter + procedure + pitfalls
3. Lưu vào thư mục skills tương ứng
4. Thông báo: `💡 Created skill: <name>`

### Trigger conditions
- ✅ Task phức tạp hoàn thành thành công
- ✅ Tìm được đường đi đúng sau khi bị lỗi
- ✅ User sửa lại approach
- ✅ Phát hiện workflow không rõ ràng

### Agents liên quan
- **`skill-curator`** — Meta-agent quản lý vòng đời skill
- **`self-learning-loop`** — Protocol tạo skill mới
- **`skill-evolution`** — Protocol cải thiện skill có sẵn

→ **Càng code càng thông minh**, skills tích lũy theo thời gian!

---

## 📦 Shared — Single Source of Truth

### Mục đích
`shared/` là **kho nguyên liệu gốc** — chứa bản đầy đủ nhất đã loại trùng. Nó **KHÔNG trực tiếp được IDE nào đọc**.

### Vai trò

| Vai trò | Giải thích |
|---------|-----------|
| **Nguồn gốc duy nhất** | Sửa 1 rule → sửa trong `shared/` → sync ra các IDE folders |
| **Tham chiếu** | AI hoặc bạn đọc `shared/` để biết toàn bộ kiến thức |
| **Input cho auto-sync** | Script tự generate 6 IDE folders từ `shared/` (v2.3 planned) |
| **Hermes compatible** | Hermes Agent đọc trực tiếp via `external_dirs` config |

### Tác động với từng IDE

| IDE | Lấy gì từ shared/? | Đọc trực tiếp? |
|-----|---------------------|:---:|
| Antigravity | Copy nguyên agents/, skills/, workflows/, hooks/ | ❌ |
| Cursor | Copy rules/ + skills/ | ❌ |
| VS Code | Chọn lọc 16 agents + 31 skills | ❌ |
| Kiro | Transform → 8 steering files | ❌ |
| OpenCode | Tóm tắt → AGENTS.md + commands | ❌ |
| Visual Studio | Tóm tắt → copilot-instructions.md | ❌ |
| Hermes | Đọc qua external_dirs | ✅ |

---

## 💪 Điểm mạnh & Hạn chế

### 🌟 Điểm mạnh
- **Hợp nhất 6 toolkit** — tinh hoa từ 6 nguồn + 66.6k star Hermes Agent
- **Self-Learning** — AI tự cải thiện theo thời gian (unique feature)
- **Orchestrator-First** — Quy trình Plan → Execute → Verify nhất quán
- **C#/.NET first-class** — dotnet-patterns, csharp-testing, EF Core, Clean Architecture
- **Zero-Config** — Copy-Paste là hoạt động ngay
- **IDE-native** — Tận dụng tính năng riêng từng IDE (Kiro fileMatch, VS Code Custom Agents)
- **Hermes compatible** — Skills portable theo chuẩn agentskills.io
- **322 skills** — Từ coding đến MLOps, DevOps, security, creative

### ⚠️ Hạn chế
- **Dung lượng lớn** — 322 skills + 59 agents chiếm ~5MB
- **Context window** — Chạy nhiều agent đồng thời cần LLM context lớn
- **Chưa auto-sync** — Cập nhật shared/ cần manual sync (planned v2.3)
- **IDE giới hạn** — VS, OpenCode chỉ hỗ trợ via instruction files

---

## 💡 Ví dụ thực tế

### Ví dụ 1: Orchestrate xây dựng API (Antigravity/Cursor)
```
User: /orchestrate Xây dựng REST API cho hệ thống quản lý đơn hàng

AI Workflow:
1. 🤖 orchestrator → nhận và phân tích yêu cầu
2. 📋 project-planner → tạo PLAN.md
3. 🏗️ architect → chọn Clean Architecture + Minimal API
4. 💾 database-architect → thiết kế schema Orders, OrderItems
5. ⚙️ backend-specialist → viết API endpoints + EF Core
6. 🔒 security-auditor → quét OWASP vulnerabilities
7. 🧪 test-engineer → viết xUnit tests
8. 💡 skill-curator → tạo skill mới "order-api-pattern"
```

### Ví dụ 2: Debug lỗi C# (Visual Studio)
```
User: Tại sao API trả về 500 khi gọi /api/orders?

AI (đọc copilot-instructions.md):
1. 🔍 debugger → 4-phase systematic debugging
2. Phát hiện: thiếu CancellationToken, async void
3. Fix + tạo skill "aspnet-common-pitfalls"
```

### Ví dụ 3: Kiro auto-steering
```
Khi mở file OrderService.cs:
→ Kiro tự load csharp-standards.md steering
→ AI biết dùng sealed class, record DTO, CancellationToken
→ Khi task hoàn thành → self-learning.md trigger tạo skill mới
```

---

## 📅 Kế hoạch nâng cấp

Chi tiết tại [PLAN_UPDATE.md](PLAN_UPDATE.md). Tóm tắt:

| Version | Timeline | Key Feature |
|---------|----------|-------------|
| **v2.2** ✅ | Hiện tại | Hermes integration, self-learning, 322 skills, 16 VS Code agents |
| **v2.3** | 1-2 tháng | Auto-sync script (shared/ → 6 IDE folders tự động) |
| **v3.0** | 3-6 tháng | MCP Server, Template Generator (`npx create-unified-toolkit`) |
| **v4.0** | 6-12 tháng | Self-Learning AI, Community Marketplace, Cloud Sync |

---

## 📄 License

MIT — Free to use, modify, and distribute.

---

*Dự án v2.2 — Unified AI Agent Toolkit Orchestrator — 2026*
*Powered by: antigravity-kit + ECC + superpowers + awesome-copilot + antigravity-awesome-skills + hermes-agent*
