# 🧰 Unified AI Agent Toolkit v2.3

> **Giải pháp "Drop-in"** tích hợp AI Agent cho **6 IDE** phổ biến nhất.
> Tự động đồng bộ tri thức, tích hợp Graph Memory (Mem0) và thống nhất trên mọi môi trường.

[![Version](https://img.shields.io/badge/version-2.3-blue)]()
[![IDEs](https://img.shields.io/badge/IDEs-6-green)]()
[![Skills](https://img.shields.io/badge/skills-323-orange)]()
[![Agents](https://img.shields.io/badge/agents-60-purple)]()
[![License](https://img.shields.io/badge/license-MIT-brightgreen)]()

---

## 📖 Mục lục

1.  [Tổng quan](#-tổng-quan)
2.  [Nguồn gốc & Phương pháp](#-nguồn-gốc--phương-pháp)
    - [6 Toolkit gốc](#6-toolkit-đã-hợp-nhất)
    - [Phương pháp hợp nhất](#phương-pháp-hợp-nhất-5-bước)
3.  [Cấu trúc thư mục](#-cấu-trúc-thư-mục)
    - [Tổng quan cấu trúc output/](#tổng-quan-cấu-trúc)
    - [Chi tiết từng folder IDE](#chi-tiết-từng-folder-ide)
4.  [Thống kê chi tiết](#-thống-kê-chi-tiết)
    - [Tổng quát](#tổng-quát)
    - [Chi tiết theo IDE](#chi-tiết-theo-ide)
    - [Ngôn ngữ lập trình được hỗ trợ](#ngôn-ngữ-lập-trình-được-hỗ-trợ)
    - [Skills theo danh mục](#skills-theo-danh-mục-top-10)
5.  [Hướng dẫn sử dụng từng IDE](#-hướng-dẫn-sử-dụng-từng-ide)
    - [Antigravity IDE](#1-antigravity-ide--đầy-đủ-nhất)
    - [Cursor IDE](#2-cursor-ide)
    - [Visual Studio Code](#3-visual-studio-code)
    - [Kiro IDE](#4-kiro-ide)
    - [OpenCode](#5-opencode)
    - [Visual Studio](#6-visual-studio)
    - [Hermes Agent (Bonus)](#7-hermes-agent-bonus)
    - [Dùng tất cả IDE cùng lúc](#8-dùng-tất-cả-ide-cùng-lúc)
6.  [Self-Learning Protocol (Hermes-inspired)](#-self-learning-protocol-hermes-inspired)
    - [Quy trình tự học Dual-Save](#quy-trình-tự-học-dual-save)
    - [Level-Up Archive](#-level-up-archive)
    - [Trigger Conditions](#trigger-conditions)
    - [Agents liên quan](#agents-liên-quan)
7.  [Graph Memory (Mem0)](#-graph-memory-v23-integration)
8.  [Shared — Single Source of Truth](#-shared--single-source-of-truth)
    - [Mục đích](#mục-đích)
    - [Tác động với từng IDE](#tác-động-với-từng-ide)
9.  [Điểm mạnh & Hạn chế](#-điểm-mạnh--hạn-chế)
    - [Điểm mạnh](#-điểm-mạnh)
    - [Hạn chế](#-hạn-chế)
10. [Ví dụ thực tế](#-ví-dụ-thực-tế)
    - [Orchestrate xây dựng API](#ví-dụ-1-orchestrate-xây-dựng-api-antigravitycursor)
    - [Debug lỗi C#](#ví-dụ-2-debug-lỗi-c-visual-studio)
    - [Kiro auto-steering](#ví-dụ-3-kiro-auto-steering)
    - [Self-Learning trong hành động](#ví-dụ-4-self-learning-trong-hành-động)
11. [Kế hoạch nâng cấp](#-kế-hoạch-nâng-cấp)

---

## 🎯 Tổng quan

Dự án này hợp nhất **6 bộ AI toolkit hàng đầu** thành **1 hệ thống cấu hình chuẩn hóa** cho **6 IDE**, với kiến trúc **Single Source of Truth** (SSoT).

Mọi IDE đều chia sẻ cùng kiến thức nền tảng nhưng được chuyển đổi (adapt) sang đúng format native của từng IDE.

### Tính năng nổi bật

| Tính năng | Mô tả |
|-----------|-------|
| 🤖 **60 Agents chuyên biệt** | orchestrator, backend, frontend, security, debugger, memory-manager... |
| 📚 **323 Skills** | Bao gồm 117 skills từ Hermes Agent và Mem0 integration |
| 📏 **89 Rules** | Hỗ trợ **15 ngôn ngữ lập trình** |
| 🧠 **Graph Memory (v2.3)** | Tích hợp Mem0 ghi nhớ ngữ cảnh lâu dài và quan hệ thực thể |
| 🧠 **Self-Learning Protocol** | AI tự tạo skills mới từ kinh nghiệm (Hermes-inspired) |
| 🆙 **Level-Up Archive** | Tự động lưu trữ tiến hóa AI vào thư mục riêng để quản lý |
| 🔒 **OWASP Top 10** | Tích hợp sẵn trong `security-auditor` |
| 🎯 **C#/.NET first-class** | Clean Architecture, EF Core, xUnit, Minimal API |
| 📦 **Zero-Config** | Mirror-Sync hoàn hảo cho 6 IDE folders |

---

## 🔬 Nguồn gốc & Phương pháp

### 6 Toolkit đã hợp nhất

| # | Toolkit | Stars | Đóng góp chính |
|---|---------|:---:|----------------|
| 1 | **antigravity-kit** | — | Agents, skills, workflows, hooks — nền tảng Antigravity |
| 2 | **everything-claude-code (ECC)** | — | 203 skills + dotnet-patterns, TDD workflow |
| 3 | **superpowers** | — | TDD, planning, subagent coordination, Git nâng cao |
| 4 | **awesome-copilot** | — | 182+ agents, 173+ instructions cho GitHub Copilot |
| 5 | **antigravity-awesome-skills** | — | 1293+ community skills |
| 6 | **hermes-agent** (NousResearch) | 66.6k | Self-learning loop, 117 skills, skill-evolution protocol |

### Phương pháp hợp nhất (5 bước)

```mermaid
graph LR
    A[1. Kiểm kê<br/>Thu thập 6 nguồn] --> B[2. Loại trùng<br/>241→60 agents<br/>1753→323 skills]
    B --> C[3. Phân loại<br/>10 danh mục chuẩn<br/>15 ngôn ngữ]
    C --> D[4. Tạo SSoT<br/>shared/ folder<br/>Bản đầy đủ nhất]
    D --> E[5. Adapt IDE<br/>Transform format<br/>cho 6 IDE]
```

| Bước | Input | Output | Tỷ lệ giảm |
|------|:---:|:---:|:---:|
| Kiểm kê | 6 repos | ~2000 files | — |
| Loại trùng | 241 agents | **60 agents** | -75% |
| Loại trùng | 1753 skills | **323 skills** | -82% |
| Loại trùng | 189 rules | **89 rules** | -53% |
| Phân loại | — | 10 categories, 15 langs | — |
| Tạo SSoT | — | `shared/` folder | — |
| Adapt | 1 shared | **6 IDE folders** | — |

---

## 📂 Cấu trúc thư mục

### Tổng quan cấu trúc

```
output/
│
├── shared/                    ← 🧠 Single Source of Truth (KHÔNG IDE nào đọc trực tiếp)
│   ├── agents/     (60 files) ← Tất cả agent definitions
│   ├── skills/    (323 dirs)  ← Tất cả skills (SKILL.md format)
│   ├── rules/      (89 files) ← Rules theo ngôn ngữ (15 thư mục)
│   ├── workflows/  (11 files) ← Workflow definitions
│   └── hooks/       (4 files) ← Hook scripts (typecheck, quality-gate...)
│
├── .agent/                    ← Antigravity IDE (Full Sync)
├── .cursor/                   ← Cursor IDE (Rules + Skills)
├── .github/                   ← VS Code Native (copilot-instructions.md + skills/)
├── .kiro/                     ← Kiro IDE (Steering files)
├── .opencode/                 ← OpenCode (Agents + Json)
├── .vs/                       ← Visual Studio (Instructions)
├── scripts/                   ← ⚙️ Sync Engine (sync_all.ps1)
│
├── level-up/                  ← 🆙 Evolution Archive (mới)
│   └── README.md              ← Hướng dẫn merge kĩ năng mới vào toolkit
│
├── docs/
│   └── MASTER_CATALOG.md      ← Kiểm kê chi tiết gốc từ 6 toolkits
│
├── GEMINI.md                  ← Root config cho Antigravity
├── .cursorrules               ← Root config cho Cursor
├── AGENTS.md                  ← Root config cho Kiro/OpenCode (15 agents)
├── hermes-config.yaml.example ← Cấu hình cho Hermes Agent
├── README.md                  ← 📄 Tài liệu này
└── PLAN_UPDATE.md             ← 📅 Lộ trình nâng cấp tương lai (Updated v2.3)
```

### Chi tiết từng folder IDE

<details>
<summary><b>.agent/ — Antigravity IDE (Click để mở)</b></summary>

```
.agent/
├── agents/     (60 files)  ← orchestrator.md, backend-specialist.md...
├── skills/    (323 dirs)   ← Mỗi skill = 1 folder chứa SKILL.md
├── workflows/  (11 files)  ← brainstorm.md, create.md, debug.md...
└── hooks/       (4 files)  ← hooks.json, run-hook.cmd, session-start...
```
</details>

<details>
<summary><b>.cursor/ — Cursor IDE (Click để mở)</b></summary>

```
.cursor/
├── rules/      (89 files)  ← Phân theo ngôn ngữ (csharp/, typescript/...)
└── skills/    (323 dirs)   ← Full sync từ shared/
```
</details>

<details>
<summary><b>.github/ — Visual Studio Code (Click để mở)</b></summary>

```
.github/
├── skills/     (323 dirs)  ← Full Sync từ shared/
├── workflows/  (11 files)  ← brainstorming.md, creative.md...
└── copilot-instructions.md  ← Hướng dẫn chuẩn hóa cho Copilot
```
</details>

<details>
<summary><b>.kiro/ — Kiro IDE (Click để mở)</b></summary>

```
.kiro/
└── steering/   (8 files)   ← Auto-loaded rules theo fileMatch
    ├── csharp-standards.md
    ├── typescript-standards.md
    ├── python-standards.md
    ├── security-rules.md
    ├── testing-rules.md
    ├── api-design.md
    ├── self-learning.md     ← 🆙 Level-Up protocol
    └── ...
```
</details>

<details>
<summary><b>.opencode/ — OpenCode (Click để mở)</b></summary>

```
.opencode/
├── opencode.json            ← 6 commands (/plan, /review, /test...)
└── AGENTS.md                ← Agent definitions + Self-Learning
```
</details>

<details>
<summary><b>.vs/ — Visual Studio (Click để mở)</b></summary>

```
.vs/
└── copilot-instructions.md  ← C#/.NET focused + Self-Learning
```
</details>

---

## 📊 Thống kê chi tiết

### Tổng quát

| Metric | Số lượng |
|--------|:---:|
| Toolkits gốc đã hợp nhất | **6** |
| Agents chuyên biệt | **60** |
| Skills (kỹ năng) | **323** |
| Rules (quy tắc) | **89** |
| Workflows | **11** |
| Hooks | **4** |
| IDE được hỗ trợ | **6** |

### Chi tiết theo IDE

| IDE | Folder | Agents | Skills | Rules/Steering | Root Config | Self-Learning |
|-----|--------|:---:|:---:|:---:|:---:|:---:|
| **Antigravity** | `.agent/` | 60 | 323 | — | `GEMINI.md` | ✅ |
| **Cursor** | `.cursor/` | — | 323 | 89 | `.cursorrules` | ✅ |
| **VS Code** | `.github/` | 16 | 323 | — | `copilot-instructions.md` | ✅ |
| **Kiro** | `.kiro/` | — | — | 8 | `AGENTS.md` | ✅ |
| **OpenCode** | `.opencode/` | — | — | — | `AGENTS.md` + `opencode.json` | ✅ |
| **Visual Studio** | `.vs/` | — | — | — | `copilot-instructions.md` | ✅ |

### Ngôn ngữ lập trình được hỗ trợ

| # | Ngôn ngữ | Folder trong `rules/` | Số rules |
|---|----------|:---:|:---:|
| 1 | **C#/.NET** | `csharp/` | 8 |
| 2 | **TypeScript/JavaScript** | `typescript/` | 7 |
| 3 | **Python** | `python/` | 6 |
| 4 | **Go** | `golang/` | 5 |
| 5 | **Rust** | `rust/` | 5 |
| 6 | **Java** | `java/` | 5 |
| 7 | **Kotlin** | `kotlin/` | 5 |
| 8 | **Swift** | `swift/` | 4 |
| 9 | **Dart/Flutter** | `dart/` | 4 |
| 10 | **C++** | `cpp/` | 4 |
| 11 | **PHP/Laravel** | `php/` | 4 |
| 12 | **Perl** | `perl/` | 3 |
| 13 | **Web (HTML/CSS)** | `web/` | 4 |
| 14 | **Common** | `common/` | 6 |
| 15 | **Chinese (中文)** | `zh/` | 1 |

### Skills theo danh mục (Top 10)

| Danh mục | Số lượng | Ví dụ tiêu biểu |
|----------|:---:|-------|
| Software Development | 42 | plan, tdd, debugging, code-review, clean-code |
| MLOps / AI | 35 | axolotl, vllm, pytorch, dspy, unsloth |
| DevOps | 28 | docker, deployment, CI/CD, terraform |
| Frontend | 22 | react, tailwind, frontend-design, swiftui |
| Security | 19 | OWASP, vulnerability-scanner, 1password |
| Backend | 18 | dotnet-patterns, api-design, golang, django |
| Creative | 15 | excalidraw, p5js, songwriting, meme-generation |
| Database | 12 | postgres, migrations, schema-design, clickhouse |
| Research | 11 | arxiv, deep-research, polymarket, llm-wiki |
| GitHub | 8 | pr-workflow, code-review, issues, repo-management |

---

## 🚀 Hướng dẫn sử dụng từng IDE

### 1. Antigravity IDE ⭐ (Đầy đủ nhất)

```powershell
# Copy vào project root:
Copy-Item -Path "output/.agent" -Destination "your-project/" -Recurse
Copy-Item "output/GEMINI.md" "your-project/"

# Sử dụng (trong Chat):
/orchestrate Xây dựng REST API cho hệ thống quản lý đơn hàng
/plan Lên kế hoạch refactor module Auth
/debug Phân tích tại sao API trả về 500
```

**Tính năng riêng:** 60 agents, 323 skills, 11 workflows, 4 hooks.

---

### 2. Cursor IDE

```powershell
Copy-Item -Path "output/.cursor" -Destination "your-project/" -Recurse
Copy-Item "output/.cursorrules" "your-project/"

# Cursor tự động đọc .cursorrules + rules/. Mở Chat hoặc Composer để dùng.
```

**Tính năng riêng:** 89 language-specific rules, 323 skills.

---

### 3. Visual Studio Code ⭐ (Đường dẫn chuẩn)

```powershell
# Copy vào project root (Sử dụng path chuẩn GitHub):
Copy-Item -Path "output/.github" -Destination "your-project/" -Recurse

# Gọi agents: @orchestrator, @backend-specialist...
# AI tự động truy cập 323 skills trong .github/skills/
```

**Tính năng riêng:** Tự động kích hoạt, truy cập full skills qua path native `.github/`.

---

### 4. Kiro IDE

```powershell
Copy-Item -Path "output/.kiro" -Destination "your-project/" -Recurse
Copy-Item "output/AGENTS.md" "your-project/"

# Kiro tự load steering files dựa trên fileMatch.
# Mở file .cs → csharp-standards.md tự kích hoạt.
```

**Tính năng riêng:** 8 steering files với auto-activation theo loại file.

---

### 5. OpenCode

```powershell
Copy-Item -Path "output/.opencode" -Destination "your-project/" -Recurse

# Dùng commands: /plan, /review, /test, /debug, /security, /dotnet
```

**Tính năng riêng:** 6 pre-defined commands.

---

### 6. Visual Studio

```powershell
Copy-Item -Path "output/.vs" -Destination "your-project/" -Recurse

# GitHub Copilot tự đọc copilot-instructions.md
# Tối ưu sâu cho: C#/.NET, Clean Architecture, EF Core, xUnit
```

**Tính năng riêng:** Chuyên sâu C#/.NET với đầy đủ patterns và code samples.

---

### 7. Hermes Agent (Đã hỗ trợ Qwen & Nhiều Provider Khác)

Toolkit giờ đây đã tích hợp sâu và nâng cấp `hermes-agent` để hỗ trợ trực tiếp các API Key của **Qwen**, **Gemini**, **Mistral**, **DeepSeek**, v.v. mà không cần cấu hình phức tạp qua CLI.

**Cách thiết lập:**

```powershell
# 1. Khai báo API Key vào môi trường (hoặc đặt trong file .env)
$env:QWEN_API_KEY="sk-qwen-key-cua-ban"
# (Hoặc: DASHSCOPE_API_KEY, GEMINI_API_KEY, DEEPSEEK_API_KEY, MISTRAL_API_KEY)

# 2. Copy template config cho Hermes:
Copy-Item "output/hermes-config.yaml.example" "$HOME/.hermes/config.yaml"

# 3. Chỉnh sửa external_dirs trong ~/.hermes/config.yaml để trỏ vào thư mục shared/skills/ của bạn
# → Hermes sẽ nhận ngay 323 skills mà không cần import gì thêm!
```

> [!TIP]
> **Sử dụng Qwen cho Agent:**
> Do đã tích hợp trực tiếp, bạn chỉ cần cấu hình `QWEN_API_KEY`, hệ thống sẽ tự động điều hướng các lời gọi mô hình về URL chuẩn của Qwen (`https://dashscope.aliyuncs.com/compatible-mode/v1`) và sử dụng model `qwen-plus` làm mặc định cho các auxiliary tasks (như memory flush, summary).

---

### 8. Dùng tất cả IDE cùng lúc

```powershell
# Copy toàn bộ output/ vào project:
Copy-Item -Path "output/*" -Destination "your-project/" -Recurse -Force
# Copy hidden folders:
Get-ChildItem "output" -Directory -Hidden | ForEach-Object {
    Copy-Item $_.FullName "your-project/$($_.Name)" -Recurse -Force
}
```

> **Lưu ý:** Các IDE sẽ chỉ đọc folder của mình. Việc copy tất cả không gây xung đột.

---

## 🧠 Self-Learning Protocol (Hermes-inspired)

Đây là tính năng **game-changer** — AI tự tạo skills mới từ kinh nghiệm, giúp bộ Toolkit của bạn **ngày càng thông minh hơn** theo thời gian.

### Quy trình tự học Dual-Save

```mermaid
graph TD
    A[Hoàn thành Task phức tạp] --> B{Đáng lưu lại?}
    B -->|Không| C[Kết thúc]
    B -->|Có| D[Viết SKILL.md mới]
    D --> E[Lưu vào output/shared/skills/<br/>Dùng ngay lập tức]
    D --> F[Mirror vào level-up/output/shared/skills/<br/>Archive để tracking]
    E --> G[💡 Level-Up! Created skill]
    F --> G
```

1.  Sau khi hoàn thành task phức tạp (5+ bước), AI tự đánh giá "skill-worthiness".
2.  Nếu đáng lưu → Viết `SKILL.md` với YAML frontmatter + procedure + pitfalls.
3.  **Dual-Save (Lưu kép)**:
    -   Ghi vào `output/shared/skills/` → IDE dùng ngay.
    -   Ghi vào `level-up/output/shared/skills/` → Bạn tracking và merge sau.
4.  AI thông báo: `💡 Level-Up! Created skill: <name> | Archived in level-up/`

### 🆙 Level-Up Archive

Thư mục `level-up/` phản chiếu chính xác cấu trúc của bộ Toolkit. Khi bạn muốn merge vĩnh viễn:

```powershell
# Merge toàn bộ kiến thức mới vào toolkit gốc:
Copy-Item -Path "level-up/*" -Destination "." -Recurse -Force
```

| Vai trò | Giải thích |
|---------|-----------|
| **Tracking** | Biết AI đã học được gì mới hôm nay |
| **Review** | Xem lại chất lượng skills trước khi merge |
| **Portable** | Copy `level-up/` sang dự án khác để chia sẻ kiến thức |

### Trigger Conditions

| Điều kiện | Mô tả |
|-----------|-------|
| ✅ Task phức tạp thành công | 5+ bước hoặc đa file |
| ✅ Error recovery | Tìm được đường đi đúng sau khi bị lỗi |
| ✅ User correction | Người dùng sửa lại approach của AI |
| ✅ Non-trivial workflow | Phát hiện quy trình không rõ ràng |

### Agents liên quan

| Agent | Vai trò |
|-------|---------|
| **`skill-curator`** | Meta-agent quản lý vòng đời skill |
| **`memory-manager`** | Chuyên gia Mem0 & Knowledge Graph |
| **`self-learning-loop`** | Protocol kỹ thuật tạo skill mới |
| **`skill-evolution`** | Protocol cải thiện skill có sẵn |

---

## 🧠 Graph Memory (v2.3 Integration)

Đây là cốt lõi của phiên bản v2.3, cho phép AI Agent không chỉ làm việc hiệu quả trong phiên mà còn ghi nhớ sở thích và quan hệ giữa các tệp/logic xuyên suốt lịch sử dự án.

### Tác động của Mem0
- **Long-term Context**: Nhớ được user thích Clean Architecture hơn Repository pattern.
- **Faster Recall**: Tìm thấy logic xử lý authentication cũ mà không cần lội ngược conversation logs.
- **Graph Relations**: Hiểu được `Agent A` đã thay đổi `File B` phục vụ `Feature C`.

### Cách kích hoạt
1. Cài đặt Mem0 MCP: `npx -y @mem0/mcp-server`
2. Cấu hình `MEMO_API_KEY` (nếu dùng Cloud) hoặc local instance.
3. Agent `orchestrator` sẽ tự động phối hợp với `memory-manager` để lưu trữ tri thức sau mỗi task.

---

## 📦 Shared — Single Source of Truth

### Mục đích

`shared/` là **"kho nguyên liệu gốc"** — chứa bản đầy đủ nhất đã loại trùng từ 6 toolkits. Nó **KHÔNG trực tiếp được IDE nào đọc** (trừ Hermes via `external_dirs`).

```
shared/
├── agents/     (60)   ← Nguồn gốc của .agent/agents/, .vscode/agents/...
├── skills/    (323)   ← Nguồn gốc của .agent/skills/, .cursor/skills/...
├── rules/      (89)   ← Nguồn gốc của .cursor/rules/, .kiro/steering/...
├── workflows/  (11)   ← Nguồn gốc của .agent/workflows/
└── hooks/       (4)   ← Nguồn gốc của .agent/hooks/
```

### Tác động với từng IDE

| IDE | Lấy gì từ shared/? | Cách chuyển đổi | Đọc trực tiếp? |
|-----|---------------------|-----------------|:---:|
| **Antigravity** | agents/ + skills/ + workflows/ + hooks/ | Copy nguyên | ❌ |
| **Cursor** | rules/ + skills/ | Copy nguyên | ❌ |
| **VS Code** | 16 agents + 31 skills (chọn lọc) | Copy chọn lọc | ❌ |
| **Kiro** | rules/ | Transform → 8 steering files | ❌ |
| **OpenCode** | agents/ | Tóm tắt → AGENTS.md | ❌ |
| **Visual Studio** | rules/csharp/ | Tóm tắt → copilot-instructions.md | ❌ |
| **Hermes** | skills/ | Đọc qua `external_dirs` config | ✅ |

### Quy trình cập nhật (Consistency Engine)

```bash
# 1. Chỉnh sửa trong shared/ (Skills/Agents)
# 2. Chạy lệnh đồng bộ:
./scripts/sync_all.ps1
# -> 6 IDE folders (.agent, .github, .cursor...) tự động cập nhật 100%
```

---

## 🏛️ IDE Capability Matrix (Độ tương thích)

Phần này giúp bạn hiểu rõ mỗi bộ kit có thể làm được những gì trong từng IDE cụ thể.

| Tính năng | Antigravity | Cursor | VS Code | Kiro/OpenCode | Visual Studio |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Multi-Agent (60+)** | ✅ Full | ❌ (1) | ❌ (1) | ⚠️ (Limited) | ❌ |
| **Skills Library (531)**| ✅ 100% | ✅ 100% | ✅ 100% | ⚠️ (Subset) | ❌ (Instr) |
| **Custom Rules (.md)** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Supervisor Model** | ✅ | ⚠️ (Rule) | ⚠️ (Rule) | ❌ | ❌ |
| **Auto-Sync** | ✅ | ✅ | ✅ | ✅ | ✅ |

*(1): Có thể gọi qua scripts hoặc dùng Orchestrator workflow thủ công.*

---

## 🛠️ Automation & Utilities (v2.4)

Để duy trì tính nhất quán và thúc đẩy khả năng tự tiến hóa của bộ Toolkit, bạn có thể sử dụng các script sau trong thư mục `scripts/`:

| Script | Tính năng | Cách dùng |
| :--- | :--- | :--- |
| **`sync_all.ps1`** | Đồng bộ hóa toàn cầu (SSoT -> IDEs -> Output) | `./scripts/sync_all.ps1` |
| **`merge-levelup.ps1`** | Hợp nhất kiến thức AI tự học được vào bộ kit gốc | `./scripts/merge-levelup.ps1` |
| **`memory-report.ps1`** | Yêu cầu Agent tạo báo cáo về bộ nhớ Graph (Mem0) | `./scripts/memory-report.ps1` |

> [!TIP]
> Hãy chạy `merge-levelup.ps1` định kỳ để làm giàu bộ Toolkit của bạn bằng những kinh nghiệm thực tế mà AI đã đúc rút được trong các phiên làm việc trước đó.

---

## 💪 Điểm mạnh & Hạn chế

### 🌟 Điểm mạnh

| # | Điểm mạnh | Chi tiết |
|---|-----------|----------|
| 1 | **Hợp nhất 6 toolkit** | Tinh hoa từ 6 nguồn + 66.6k star Hermes Agent |
| 2 | **Self-Learning** | AI tự cải thiện theo thời gian — unique feature |
| 3 | **Level-Up Archive** | Theo dõi tiến hóa AI, merge bằng 1 lệnh copy |
| 4 | **Orchestrator-First** | Quy trình Plan → Execute → Verify nhất quán |
| 5 | **C#/.NET first-class** | dotnet-patterns, csharp-testing, EF Core, Clean Architecture |
| 6 | **15 ngôn ngữ** | C#, TS, Python, Go, Rust, Java, Kotlin, Swift, Dart, C++, PHP, Perl... |
| 7 | **Zero-Config** | Copy-Paste là hoạt động ngay — không cần cài đặt gì thêm |
| 8 | **IDE-native** | Tận dụng tính năng riêng từng IDE (Kiro fileMatch, VS Code Custom Agents) |
| 9 | **Hermes compatible** | Skills portable theo chuẩn agentskills.io |
| 10 | **Open Source** | MIT License — tự do sử dụng và sửa đổi |

### ⚠️ Hạn chế

| # | Hạn chế | Giải pháp tương lai |
|---|---------|---------------------|
| 1 | **Dung lượng lớn** (~5MB) | Slim Mode ở v2.3 (~30 skills cốt lõi) |
| 2 | **Context window** | Cần LLM context ≥128k cho multi-agent |
| 3 | **Chưa auto-sync** | Script tự động ở v2.3 |
| 4 | **IDE giới hạn** | VS, OpenCode chỉ qua instruction files |
| 5 | **Manual merge** | Level-Up Merger script ở v2.3 |

---

## 💡 Ví dụ thực tế

### Ví dụ 1: Orchestrate xây dựng API (Antigravity/Cursor)

```
📝 User: /orchestrate Xây dựng REST API cho hệ thống quản lý đơn hàng

🤖 AI Workflow:
1. 📋 orchestrator    → Nhận và phân tích yêu cầu
2. 📝 project-planner → Tạo PLAN.md chi tiết
3. 🏗️ architect       → Chọn Clean Architecture + Minimal API
4. 💾 database-architect → Thiết kế schema: Orders, OrderItems, Customers
5. ⚙️ backend-specialist → Viết API endpoints + EF Core DbContext
6. 🔒 security-auditor → Quét OWASP vulnerabilities, kiểm tra auth
7. 🧪 test-engineer   → Viết xUnit tests + integration tests
8. 💡 skill-curator   → Tạo skill mới "order-api-pattern"
                         → Lưu vào output/shared/ VÀ level-up/
```

### Ví dụ 2: Debug lỗi C# (Visual Studio)

```
📝 User: Tại sao API trả về 500 khi gọi /api/orders?

🤖 AI (đọc copilot-instructions.md):
1. 🔍 debugger        → 4-phase systematic debugging
2. 🔎 Phát hiện:      → Thiếu CancellationToken, dùng async void
3. 🔧 Fix applied:    → Thêm CancellationToken, đổi async Task
4. 💡 skill-curator   → Tạo skill "aspnet-common-pitfalls"
                         → Lưu vào level-up/ để tracking
```

### Ví dụ 3: Kiro auto-steering

```
📝 Khi mở file OrderService.cs:

🤖 Kiro tự động:
1. Load csharp-standards.md steering   (fileMatch: "*.cs")
2. AI biết dùng sealed class, record DTO, CancellationToken
3. Khi task hoàn thành → self-learning.md trigger tạo skill mới
4. Skill mới xuất hiện trong level-up/ folder
```

### Ví dụ 4: Self-Learning trong hành động

```
📝 Phiên làm việc phức tạp (8 bước):

🤖 AI hoàn thành → skill-curator kích hoạt:
1. Đánh giá: "Quy trình tích hợp Stripe Payment là reusable? → CÓ"
2. Viết: level-up/output/shared/skills/stripe-integration/SKILL.md
3. Thông báo: 💡 Level-Up! Created skill: stripe-integration
4. Ngày mai, khi dự án khác cần Stripe → AI đã biết cách làm!
```

---

## 📅 Kế hoạch nâng cấp

Chi tiết tại [PLAN_UPDATE.md](PLAN_UPDATE.md).

| Version | Timeline | Key Feature |
|---------|----------|-------------|
| **v2.2** ✅ | Q1 2026 | Hermes integration, Self-Learning, 322 skills |
| **v2.3** ✅ | Hiện tại | **Graph Memory (Mem0)**, Mirror-Sync v1.2.1, Parallel Agents |
| **v2.4** ✅ | **Hôm nay** | **Horizon Integration**: Supervisor Agent, CROSS-IDE Parity, `DESIGN.md` |
| **v3.0** | 3-6 tháng | MCP Server, Template Generator (`npx create-unified-toolkit`) |
| **v4.0** | 6-12 tháng | Self-Learning v2, Community Marketplace, Cloud Sync |

---

## 📄 License

MIT — Free to use, modify, and distribute.

---

<p align="center">
  <b>Unified AI Agent Toolkit v2.2</b><br/>
  <i>Powered by: antigravity-kit + ECC + superpowers + awesome-copilot + antigravity-awesome-skills + hermes-agent</i><br/>
  <i>Built with ❤️ by Xuan Thai — 2026</i>
</p>
