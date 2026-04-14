# Đánh giá và Tích hợp CodeGraphContext vào Tool-Kit-for-AI-Agent

Căn cứ vào yêu cầu của bạn, tôi đã nghiên cứu `CodeGraphContext` (CGC) và đối chiếu với cấu trúc dự án hiện tại (`Tool-Kit-for-AI-Agent`). Dưới đây là kế hoạch phân tích và đề xuất.

## User Review Required

> [!IMPORTANT]
> **Hạn chế về ngôn ngữ:** CGC hiện tại hỗ trợ tốt Python, JS/TS, Go nhưng **chưa hỗ trợ C#**. Nếu dự án của bạn là thuần C#/.NET, chúng ta cần cân nhắc việc mở rộng parser cho nó hoặc sử dụng giải pháp thay thế.

> [!TIP]
> **MCP Integration:** CGC cung cấp giao diện MCP (Model Context Protocol). Đây là điểm cộng lớn vì dự án của bạn đã có hạ tầng MCP, việc tích hợp sẽ rất tự nhiên.

## Proposed Changes

### 1. Giai đoạn Nghiên cứu (Research Phase)
- Phân tích chi tiết khả năng mở rộng của `CodeGraphContext` để hỗ trợ C# (thông qua Tree-Sitter).
- Thử nghiệm chạy CGC MCP Server với một codebase mẫu (Python/JS) để đánh giá hiệu quả thực tế so với RAG truyền thống.

### 2. Giai đoạn Thử nghiệm (PoC Phase)
- Cài đặt CGC cục bộ.
- Cấu hình một Agent trong `Tool-Kit-for-AI-Agent` sử dụng CGC MCP Server để truy vấn ngữ cảnh.
- So sánh kết quả trả về của Agent khi có và không có CGC.

### 3. Giai đoạn Tích hợp (Integration Phase)
- Nếu kết quả PoC tốt, sẽ xây dựng một "Skill" mới trong dự án của bạn (ví dụ: `codegraph-context-skill`) để bọc lại các tính năng của CGC.
- Cập nhật `AGENTS.md` để các Agent biết khi nào nên sử dụng "đồ thị ngữ cảnh" thay vì tìm kiếm file thông thường.

## Open Questions

1. **Ngôn ngữ mục tiêu:** Bạn muốn dùng CGC để Agent hiểu chính codebase của dự án này (C#) hay để Agent hỗ trợ bạn viết các dự án khác (Python, JS, v.v.)?
2. **Infrastructure:** Bạn có sẵn sàng chạy một Graph Database (FalkorDB hoặc Neo4j) làm backend cho CGC không?
3. **Mức độ tích hợp:** Bạn muốn tích hợp CGC ở mức độ "Tool" (Agent gọi khi cần) hay mức độ "Core" (Tự động index mọi thứ)?

## Verification Plan

### Automated Tests
- Chạy các script test của CGC trên một repo mẫu.
- Kiểm tra tính kết nối của MCP Server thông qua `mcp-inspector`.

### Manual Verification
- Đặt các câu hỏi hóc búa về quan hệ hàm (call graphs) cho Agent và kiểm chứng độ chính xác.
