# Hướng Dẫn Sử Dụng Claude-Mem 🧠

Chào mừng bạn đến với **Claude-Mem**, hệ thống nén bộ nhớ vĩnh cửu được thiết kế dành riêng cho Claude Code, Gemini CLI và các AI Agent khác. Tài liệu này sẽ hướng dẫn bạn chi tiết từng bước từ cài đặt, tích hợp đến cách sử dụng hiệu quả.

---

## 1. Giới thiệu
Claude-Mem giúp AI của bạn "nhớ" những gì đã làm trong các phiên làm việc trước đó. Nó tự động ghi lại quá trình sử dụng công cụ, tóm tắt các sự kiện quan trọng và đưa chúng vào ngữ cảnh của các phiên làm việc tương lai, giúp duy trì sự liên tục của dự án.

---

## 2. Yêu cầu hệ thống
Trước khi bắt đầu, hãy đảm bảo máy tính của bạn đã cài đặt:
- **Node.js**: Phiên bản 18.0.0 trở lên.
- **Claude Code**: Phiên bản mới nhất.
- **Bun**: Runtime JavaScript (sẽ tự động cài đặt nếu chưa có).
- **uv**: Quản lý gói Python (sẽ tự động cài đặt để hỗ trợ tìm kiếm vector).

---

## 3. Hướng dẫn Cài đặt

Bạn có thể cài đặt nhanh chóng bằng một trong các phương thức sau:

### Cách 1: Cài đặt qua NPX (Khuyên dùng)
Mở terminal và chạy lệnh:
```bash
npx claude-mem install
```

### Cách 2: Cài đặt trực tiếp trong Claude Code
Nếu bạn đang ở trong phiên làm việc của Claude Code:
```bash
/plugin marketplace add thedotmack/claude-mem
/plugin install claude-mem
```

*Lưu ý: Sau khi cài đặt, hãy khởi động lại Claude Code để các thay đổi có hiệu lực.*

---

## 4. Hướng dẫn Tích hợp

### Tích hợp với Gemini CLI
Để sử dụng Claude-Mem cho Gemini CLI:
```bash
npx claude-mem install --ide gemini-cli
```
Hệ thống sẽ tự động phát hiện thư mục cấu hình tại `~/.gemini`.

### Tích hợp với OpenCode
Dành cho người dùng OpenCode:
```bash
npx claude-mem install --ide opencode
```

### Tích hợp với OpenClaw Gateway
OpenClaw là một gateway mạnh mẽ cho các AI Agent. Để cài đặt Claude-Mem như một plugin bộ nhớ vĩnh cửu trên OpenClaw:
```bash
curl -fsSL https://install.cmem.ai/openclaw.sh | bash
```
Lệnh này sẽ thiết lập tất cả các phụ thuộc, cấu hình AI provider và khởi chạy worker service.

---

## 5. Hướng dẫn Sử dụng Chi tiết

### Hoạt động Tự động
Sau khi cài đặt, Claude-Mem sẽ hoạt động hoàn toàn tự động:
1. **Ghi lại**: Mỗi khi bạn yêu cầu Claude thực hiện một lệnh (chạy test, sửa code...), Claude-Mem sẽ ghi lại kết quả.
2. **Tóm tắt**: Khi phiên làm việc kết thúc, hệ thống sẽ nén thông tin thành các tóm tắt ngữ nghĩa.
3. **Nhắc lại**: Khi bạn bắt đầu dự án mới hoặc phiên mới, các thông tin liên quan sẽ tự động được "nhắc lại" cho Claude.

### Tìm kiếm Bộ nhớ (mem-search)
Bạn có thể chủ động hỏi Claude về lịch sử dự án. Claude sẽ sử dụng công cụ `mem-search` để trả lời các câu hỏi như:
- *"Lần trước chúng ta đã sửa lỗi xác thực như thế nào?"*
- *"Tổng hợp các thay đổi quan trọng trong tuần này."*
- *"Chúng ta đã thảo luận gì về kiến trúc database?"*

### Giao diện Web (Web Viewer)
Bạn có thể xem luồng bộ nhớ thời gian thực và quản lý cài đặt tại:
**[http://localhost:37777](http://localhost:37777)**

---

## 6. Cấu hình Chế độ Tiếng Việt 🇻🇳

Để Claude-Mem hoạt động tối ưu với Tiếng Việt (tạo tóm tắt và ghi chú bằng Tiếng Việt), bạn cần cấu hình lại chế độ làm việc.

1. Tìm tệp cấu hình tại: `~/.claude-mem/settings.json`
2. Cập nhật dòng `CLAUDE_MEM_MODE`:
```json
{
  "CLAUDE_MEM_MODE": "code--vi"
}
```
3. Khởi động lại Claude Code. Giờ đây, các quan sát và bộ nhớ sẽ được ưu tiên xử lý bằng Tiếng Việt.

---

## 7. Các Tính năng Nâng cao

### Kiểm soát Quyền riêng tư
Nếu bạn làm việc với thông tin nhạy cảm (mật khẩu, khóa API), hãy sử dụng thẻ `<private>`:
```text
Cấu hình API với key là <private>SECRET_KEY_123</private>
```
Nội dung bên trong thẻ sẽ bị loại bỏ hoàn toàn trước khi lưu vào cơ sở dữ liệu bộ nhớ.

### Quy trình Tìm kiếm 3 Lớp (Dành cho hiệu quả Token)
Khi tìm kiếm bộ nhớ sâu, Claude-Mem sử dụng mô hình tiết lộ tuần tự:
1. **Search**: Tìm kiếm danh sách các ID liên quan (ít tốn token).
2. **Timeline**: Xem dòng thời gian xung quanh các ID đó.
3. **Get Observations**: Chỉ tải nội dung chi tiết của các ID thực sự cần thiết.

---

## 8. Khắc phục Sự cố

- **Lỗi không nhận diện lệnh `npm`**: Đảm bảo Node.js đã được thêm vào biến môi trường PATH.
- **Bộ nhớ không cập nhật**: Kiểm tra xem Worker Service có đang chạy không (truy cập http://localhost:37777). Nếu không, hãy chạy lại lệnh cài đặt.
- **Sử dụng lệnh Troubleshoot**: Bạn có thể hỏi trực tiếp Claude: *"Lỗi Claude-Mem, hãy giúp tôi kiểm tra"*. Claude sẽ tự động chẩn đoán hệ thống.

---

Cảm ơn bạn đã sử dụng Claude-Mem! Nếu có bất kỳ câu hỏi nào, hãy truy cập [Tài liệu chính thức](https://docs.claude-mem.ai/).
