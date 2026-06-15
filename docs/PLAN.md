# Orchestration Plan: Đánh Giá & Tích Hợp `taste-skill`

## 1. Goal
Rà soát, đánh giá toàn diện kho kỹ năng UI/FE `taste-skill` (tại `sources/taste-skill`) và tích hợp một cách có chọn lọc các kỹ năng thiết kế xuất sắc vào hệ thống Tool-Kit cốt lõi (`shared/skills/`), nhằm tăng cường khả năng thiết kế UI/UX (đặc biệt là cho `frontend-specialist`).

## 2. Phân Tích Hiện Trạng (Explorer Agent)
Thư mục `sources/taste-skill/skills/` chứa 13 thư mục con đại diện cho các phong cách và phương pháp thiết kế khác nhau:
- **Phong cách:** `brutalist-skill`, `minimalist-skill`, `soft-skill`
- **UI/UX Core:** `taste-skill`, `taste-skill-v1`, `brandkit`, `redesign-skill`
- **Tools/Generators:** `imagegen-frontend-web`, `imagegen-frontend-mobile`, `image-to-code-skill`, `stitch-skill`, `output-skill`, `gpt-tasteskill`

Mỗi thư mục chứa một file `SKILL.md` (ví dụ `taste-skill/SKILL.md` cực lớn ~88KB). Chúng ta cần chọn lọc, định dạng lại frontmatter (nếu cần) và đồng bộ vào `shared/skills/`.

## 3. Orchestration Agents (Phase 2 - Implementation)
Để thực hiện việc này theo đúng chuẩn Orchestration, tối thiểu 3 agent sẽ được invoke song song:

1. **`frontend-specialist` (Thẩm định UI/UX):**
   - Đọc và phân tích các kỹ năng chuyên về UI (như `taste-skill`, `brutalist-skill`, `minimalist-skill`, `soft-skill`).
   - Đánh giá chất lượng hướng dẫn thiết kế.
   - Sao chép và tích hợp các kỹ năng đạt chuẩn vào `shared/skills/` với metadata chuẩn xác.

2. **`code-reviewer` / `skill-curator` (Kiểm duyệt định dạng & Metadata):**
   - Kiểm tra cấu trúc file `SKILL.md` của các kỹ năng công cụ (`stitch-skill`, `image-to-code-skill`, v.v.).
   - Đảm bảo các file này có YAML frontmatter đúng chuẩn của hệ thống Kiro/Cursor (`name`, `description`).
   - Lược bỏ hoặc gộp các kỹ năng dư thừa (vd: `taste-skill` và `taste-skill-v1`).

3. **`devops-engineer` / `orchestrator` (Đồng bộ hệ thống):**
   - Xác nhận tất cả kỹ năng mới đã nằm đúng vị trí trong `shared/skills/`.
   - Chạy tập lệnh xác minh (verification scripts) hoặc script đồng bộ `sync_all.ps1`.
   - Đảm bảo `local-skill-searcher` có thể nhận diện được các kỹ năng mới.

## 4. Verification Plan
- Chạy `python .agent/skills/local-skill-searcher/scripts/search_skills.py "taste"` để xác nhận hệ thống có thể lập chỉ mục (index) các kỹ năng mới.
- Gọi script đồng bộ `sync_all.ps1`.

## User Review Required
> [!IMPORTANT]
> - Có cần giữ lại toàn bộ 13 kỹ năng không hay chỉ lọc ra những cái hay nhất?
> - Các kỹ năng được tích hợp sẽ nằm ở `shared/skills/`, từ đó tự động đẩy qua `.agent/skills/` và các thư mục IDE khác. Bạn đồng ý với luồng này chứ?

---
*Created by: `project-planner` agent*
