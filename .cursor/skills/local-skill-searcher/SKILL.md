---
name: local-skill-searcher
description: Tìm kiếm và trích xuất các kỹ năng (skills) từ kho lưu trữ nội bộ (~1800 kỹ năng) để giải quyết các vấn đề chuyên sâu. Khi một Agent không có sẵn kiến thức để xử lý vấn đề, hãy gọi kỹ năng này để lục tìm trong thư viện.
---

# Local Skill Searcher

Kỹ năng này giúp bạn tìm kiếm trong kho tàng khổng lồ (gần 2000 skills) của Tool-Kit nội bộ. Vì `AGENTS.md` chỉ nạp các kỹ năng cốt lõi (Core Skills) để tối ưu ngữ cảnh, nên `local-skill-searcher` là cầu nối để bạn tiếp cận phần còn lại.

## Khi nào nên sử dụng
- Khi người dùng hỏi một công cụ, framework, hoặc phương pháp luận mà bạn chưa có sẵn kỹ năng.
- Khi cần tìm best practices, template, hoặc hướng dẫn chuyên môn ngách (niche).
- Ví dụ: "Tìm cho tôi skill liên quan đến performance optimization cho Vue", "Chúng ta có skill nào về penetration testing không?".

## Cách sử dụng (How to Use)

Bạn hãy chạy script Python được đính kèm để quét các file `SKILL.md` trong hệ thống:

```bash
python .agent/skills/local-skill-searcher/scripts/search_skills.py "từ_khóa_1" "từ_khóa_2"
```

Script này sẽ:
1. Đọc qua tất cả các thư mục trong `.agent/skills/` và `output/shared/skills/`.
2. Tìm kiếm các từ khóa (keywords) trong tên thư mục, title và description của các file `SKILL.md`.
3. Trả về cho bạn danh sách top 5-10 kỹ năng phù hợp nhất cùng với đường dẫn tuyệt đối để bạn có thể dùng tool `view_file` đọc nội dung của chúng.

## Quy Trình (Workflow)

1. **Nhận diện nhu cầu:** Xác định các từ khóa chính xác (VD: `react`, `seo`, `security`, `docker`).
2. **Tìm kiếm:** Chạy lệnh `python search_skills.py [keywords]`.
3. **Đọc kỹ năng:** Chọn kỹ năng phù hợp nhất từ kết quả trả về, sau đó dùng `view_file` đọc nội dung file `SKILL.md` của nó.
4. **Áp dụng:** Hấp thụ kiến thức từ file đó và trả lời/giải quyết bài toán cho người dùng.

> ⚠️ **Lưu ý:** Tuyệt đối KHÔNG ĐƯỢC bịa ra tên kỹ năng. Hãy luôn luôn sử dụng script search này để tìm kiếm thực tế trên ổ cứng.
