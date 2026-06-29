# Requirements — Antigravity Kit → Kiro Integration

> Spec: `antigravity-kiro-integration`
> Status: **Confirmed** — quyết định đã chốt

## 0. Quyết định đã chốt

| # | Câu hỏi | Quyết định |
|---|---------|------------|
| 1 | Phạm vi skills | **Dịch toàn bộ ~1845 skills** |
| 2 | Migration tool | **Python** (cross-platform) |
| 3 | Định dạng agents | **Chỉ `.md` IDE** — đủ sau normalize 3 điểm (xem §2) |
| 4 | Workflows | **Dịch thành steering** — `/orchestrate` → `inclusion: auto` |
| 5 | ECC hiện có | **Giữ nguyên, bổ sung** — không thay thế |

---

## 1. Bảng ánh xạ định dạng (nguồn → đích)

| Thành phần | `.agent/` Antigravity | `.kiro/` Kiro |
|---|---|---|
| Agents (~61) | `tools: A,B` / `model: inherit` / `skills: x,y` | `tools: ["A","B"]` / `model: claude-sonnet-4-5` / xoá `skills:` |
| Skills (~1845) | `skills/<name>/SKILL.md` + sub-dirs | `skills/<name>/SKILL.md` + sub-dirs — cùng cấu trúc |
| Rules | `rules/GEMINI.md` (`trigger: always_on`) | `steering/antigravity-master-rules.md` (`inclusion: auto`) |
| Rules | `rules/CONTEXT-INPUT.md` | `steering/antigravity-context-input.md` (`inclusion: auto`) |
| Workflows (12) | `workflows/<name>.md` slash-command | `steering/workflow-<name>.md` (`inclusion: manual`) |
| `/orchestrate` | workflow đặc biệt | `steering/workflow-orchestrate.md` (`inclusion: auto`) |
| Hooks | `hooks.json` Claude-style (`SessionStart`) | `session-start.kiro.hook` (trigger: `promptSubmit`) |
| MCP | `mcp_config.json` (secrets raw) | `settings/mcp-antigravity.json.example` (placeholders) |
| Scripts | `scripts/*.py` | `scripts/python/*.py` + README Windows |

---

## 2. Đánh giá agent `.md`: đủ cho Kiro IDE không?

**Kết luận: Đủ, sau khi normalize 3 điểm frontmatter.**

| Vấn đề | Antigravity | Kiro IDE cần | Hành động khi dịch |
|--------|-------------|----------|-----------|
| `tools` format | `Read, Grep, Bash` (CSV string) | `["Read", "Grep", "Bash"]` (JSON array) | Auto-convert |
| `model` | `inherit` (không hợp lệ) | `claude-sonnet-4-5` | Map `inherit` → `claude-sonnet-4-5` |
| `skills:` frontmatter | `skills: a, b` (Antigravity-only) | Không dùng trong frontmatter Kiro | Xoá khỏi frontmatter; tham chiếu vẫn còn trong body |

Body markdown: hoàn toàn tương thích — Kiro IDE đọc giống Claude. Không sửa nội dung.

**Kết quả thực tế:** `.kiro/agents/` hiện có 61 agents `.md` — Antigravity cũng có 61 agents → phần lớn **trùng tên và đã tốt**. Migration chỉ cần normalize và skip trùng.

---

## 3. Phạm vi tích hợp

### Source (`.agent/`)
- 61 agents `.md` (Antigravity format)
- ~1845 skill folders
- 13 workflows (`brainstorm`, `clone-source`, `create`, `debug`, `deploy`, `enhance`, `orchestrate`, `plan`, `preview`, `status`, `test`, `ui-ux-pro-max`, `update-sources`)
- 2 rule files (`GEMINI.md`, `CONTEXT-INPUT.md`)
- Hooks: `hooks.json` (SessionStart), `hooks-cursor.json`, `run-hook.cmd`
- Scripts: `checklist.py`, `verify_all.py`, `session_manager.py`, `auto_preview.py`
- `mcp_config.json`

### Target (`.kiro/`) — thêm vào, không xoá cũ
- Agents: normalize + skip trùng → `agents/`
- Skills: copy + skip trùng → `skills/`
- Rules → `steering/antigravity-*.md`
- Workflows → `steering/workflow-*.md` (orchestrate = auto)
- Hook → `hooks/session-start.kiro.hook`
- MCP → `settings/mcp-antigravity.json.example`
- Scripts → `scripts/python/`

---

## 4. Requirements (EARS format)

### R1 — Inventory / Bóc tách
1. WHEN tool chạy, SHALL quét toàn bộ `.agent/` và tạo `inventory.json` với mỗi entry: `name`, `type`, `source_path`, `dest_path`, `status` (`pending`/`translated`/`skipped`/`invalid`), `note`.
2. IF thành phần thiếu trường bắt buộc, THEN SHALL đánh dấu `invalid` + `reason`.
3. SHALL chạy inventory trước mọi bước dịch (dry-run mode khả dụng).

### R2 — Dịch Agents (~61)
1. SHALL normalize frontmatter: `tools` CSV→JSON array, `model: inherit`→`claude-sonnet-4-5`, xoá `skills:`.
2. SHALL giữ nguyên body markdown không sửa.
3. WHERE agent đã tồn tại ở đích (tên trùng), SHALL skip + log `skipped (already exists)`.
4. SHALL append agent mới vào `AGENTS.md` (không overwrite section cũ).

### R3 — Dịch Skills (~1845)
1. SHALL copy toàn bộ `skills/<name>/` kèm sub-directories (`scripts/`, `references/`, `assets/`).
2. SHALL skip nếu `skills/<name>/` đã tồn tại ở đích.
3. IF `SKILL.md` không có frontmatter hoặc thiếu `name`/`description`, SHALL inject minimal frontmatter từ tên thư mục.
4. SHALL xử lý theo batch (~100 skills/batch) và in tiến độ ra stdout mỗi batch.

### R4 — Dịch Rules → Steering
1. `rules/GEMINI.md` → `steering/antigravity-master-rules.md` với frontmatter `inclusion: auto` + `description: "Antigravity Kit master rules — always loaded"`.
2. `rules/CONTEXT-INPUT.md` → `steering/antigravity-context-input.md` với `inclusion: auto`.
3. SHALL skip nếu tên đích trùng với file ECC hiện có.

### R5 — Dịch Workflows → Steering
1. `workflows/<name>.md` (trừ orchestrate) → `steering/workflow-<name>.md` với frontmatter `inclusion: manual` + `description` mô tả mục đích.
2. `workflows/orchestrate.md` → `steering/workflow-orchestrate.md` với **`inclusion: auto`** — luôn nạp trong mọi session Kiro.
3. SHALL giữ nguyên nội dung workflow, chỉ thêm frontmatter.

### R6 — Dịch Hooks → `.kiro.hook`
1. SHALL dịch SessionStart hook trong `hooks.json` → `hooks/session-start.kiro.hook` với trigger `promptSubmit` (Kiro tương đương gần nhất).
2. SHALL thay `${CLAUDE_PLUGIN_ROOT}` bằng đường dẫn tương đối `.kiro/scripts/python/`.
3. Trigger không ánh xạ 1-1 SHALL được ghi vào `inventory.json[note]` với giải thích.

### R7 — MCP & Scripts
1. SHALL tạo `.kiro/settings/mcp-antigravity.json.example` từ `mcp_config.json` — **không đụng** `mcp.json` hay `mcp.json.example` hiện có.
2. SHALL thay mọi API key / secret bằng placeholder `<YOUR_API_KEY_HERE>`.
3. SHALL copy Python scripts → `.kiro/scripts/python/` kèm `README.md` hướng dẫn chạy trên Windows (`python .kiro\scripts\python\checklist.py .`).

### R8 — Migration tool (Python, cross-platform)
1. SHALL là script `migrate_antigravity.py` chạy được trên Windows (cmd/PowerShell) và Linux/Mac.
2. SHALL non-destructive: không ghi đè file đích đã tồn tại.
3. SHALL idempotent: chạy lại nhiều lần cho cùng kết quả.
4. WHEN gặp lỗi ở một thành phần, SHALL tiếp tục các thành phần khác (fail-soft) và ghi lỗi vào `inventory.json`.
5. SHALL hỗ trợ flag `--dry-run` (chỉ sinh inventory, không copy).
6. WHEN hoàn thành, SHALL in summary: `Agents: X/Y | Skills: X/Y | Steering: X | Hooks: X | Skipped: N | Errors: N`.

### R9 — Tương thích ECC hiện có
1. SHALL không xoá hoặc ghi đè bất kỳ file nào trong `.kiro/` hiện tại.
2. Tên trùng ở đích → skip + log, không raise error.
3. Files mới từ Antigravity SHALL dùng prefix `antigravity-` (steering) hoặc `workflow-` (workflows) để tránh xung đột với ECC.

---

## 5. Bước tiếp theo

Sau khi requirements được xác nhận, chuyển sang **design.md** với:
- Sơ đồ luồng xử lý `migrate_antigravity.py`
- Cấu trúc `inventory.json`
- Frontmatter template cho từng loại steering
- Schema `.kiro.hook` cho session-start
