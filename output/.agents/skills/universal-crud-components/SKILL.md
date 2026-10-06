---
name: universal-crud-components
description: Kiến trúc và hướng dẫn triển khai các component CRUD dùng chung (Universal) cho các ứng dụng Frontend. Dễ dàng áp dụng cho NextJS, Nuxt/Vue, Angular.
---

# Universal CRUD Components Skill

Skill này hướng dẫn các AI Agent (hoặc Developer) cách xây dựng hệ thống UI Components dùng chung cho các trang Quản trị (Admin Portal), bất kể đang sử dụng framework nào (NextJS, Vue/Nuxt, Angular). 

Thay vì tập trung vào code cụ thể của một ngôn ngữ, tài liệu này tập trung vào **Kiến trúc (Architecture)**, **Trách nhiệm của từng Component (Responsibilities)**, và **Quy trình hoạt động (Workflow)**.

---

## 1. Nguyên Tắc Cốt Lõi (Core Principles)

Khi xây dựng các component CRUD (List, Create, Edit, Show), hãy luôn tuân thủ các nguyên tắc sau:

1. **Tách Biệt Trách Nhiệm (Separation of Concerns)**: Component giao diện (UI Wrapper) không nên trực tiếp gọi API. Nó chỉ nhận dữ liệu (Props/Inputs) và phát ra sự kiện (Events/Outputs/Callbacks) để trang cha xử lý.
2. **Content Projection (Kế thừa Giao diện)**: Các component Layout (như AppList, AppCreate) đóng vai trò là "Cái vỏ" (Wrapper). Nội dung chính (như Table, Form) phải được truyền vào từ bên ngoài thông qua cơ chế `children` (React), `<slot>` (Vue), hoặc `<ng-content>` (Angular).
3. **Đồng Bộ URL (URL-Driven State)**: Các trạng thái mang tính chia sẻ (như phân trang, bộ lọc, từ khóa tìm kiếm) nên được đồng bộ lên URL. Điều này giúp người dùng có thể chia sẻ link hoặc reload trang mà không mất state.

---

## 2. Kiến Trúc Các Component Dùng Chung

### 2.1. Layout Wrappers (`AppList`, `AppCreate`, `AppEdit`, `AppShow`)
**Mục đích**: Cung cấp một bộ khung chuẩn cho mọi trang. Đảm bảo mọi màn hình quản trị đều có giao diện thống nhất.

**Các thành phần bắt buộc trong Wrapper:**
- **Breadcrumb (Điều hướng)**: Tự động render dựa trên Route hiện tại.
- **Tiêu đề (Title) & Mô tả**: Hiển thị tên của trang.
- **Vùng nút chức năng (Header Actions)**: 
  - `AppList`: Các nút Import, Export, Add New. (Tự động gom vào Dropdown nếu màn hình nhỏ / Mobile).
  - `AppCreate` / `AppEdit`: Nút Cancel (quay lại), Nút Save.
  - `AppShow`: Nút Edit, Nút Delete.
- **Vùng nội dung (Content Area)**: Nơi hiển thị Form hoặc Table từ trang cha truyền vào.
- **Bảo mật / Phân quyền (Tenant Guard)**: (Tùy chọn) Trước khi cho phép bấm nút "Tạo mới" hoặc "Lưu", tự động kiểm tra xem người dùng đã chọn Tenant/Chi nhánh hay chưa. Nếu chưa, hiển thị Modal cảnh báo.

**Cách dịch sang các Framework:**
- **React/NextJS**: Truyền qua `props.children` và render các actions thông qua `ReactNode` props.
- **Vue/Nuxt**: Sử dụng `<slot name="header-actions">` và `<slot>` mặc định.
- **Angular**: Sử dụng `<ng-content select="[header-actions]">` và `<ng-content>`.

---

### 2.2. Danh sách & Bảng Dữ Liệu (`AppTable`, `Pagination`)
**Mục đích**: Hiển thị dữ liệu dạng lưới, quản lý các trạng thái phức tạp (sắp xếp, chọn nhiều dòng).

**Quy trình hoạt động:**
1. **Khởi tạo**: Bảng nhận cấu hình cột (Columns config) và Dữ liệu (Data source) từ trang cha.
2. **Responsive**: Cố định (Sticky) dòng Header. Có khả năng cuộn ngang (Scroll X) khi trên Mobile, và giới hạn chiều cao (Scroll Y) để không bị tràn trang.
3. **Trạng thái Trống (Empty State)**: Nếu không có dữ liệu, hiển thị một component Empty thân thiện.
4. **Phân trang (Pagination)**: Component phân trang phải nằm độc lập hoặc dưới cùng. Cần cung cấp các sự kiện: Chuyển trang, Đổi số lượng item/trang (Page Size).
5. **Cột đặc biệt**: 
   - **Checkbox Column**: Cho phép chọn nhiều dòng để thao tác hàng loạt (Bulk Actions).
   - **Tenant/Chi nhánh Column**: Một cột mặc định có thể tự động được thêm vào (unshift) đầu danh sách cấu hình nếu tính năng Tenant được kích hoạt.

---

### 2.3. Bộ Lọc Nâng Cao (`AppFilters`)
**Mục đích**: Cung cấp thanh tìm kiếm nhanh và bộ lọc chi tiết cho danh sách.

**Quy trình hoạt động:**
1. **Search (Tìm kiếm nhanh)**: Thường là một ô Input Text, thay đổi giá trị sẽ cập nhật tham số `keyword` trên URL.
2. **Advanced Filters (Bộ lọc chi tiết)**: Nút bấm để mở một Panel/Drawer/Modal.
3. **Đếm số lượng Filter (Badge Count)**: Nút mở bộ lọc nên có một "Huy hiệu" (Badge) hiển thị số lượng điều kiện đang được áp dụng.
4. **Đồng bộ hóa (Synchronization)**:
   - Khi Component *Mount*: Đọc tham số từ URL và gán vào State của bộ lọc.
   - Khi người dùng bấm "Apply": Đẩy toàn bộ State của bộ lọc lên URL param. Reset về trang 1.
   - Khi bấm "Reset": Xóa toàn bộ tham số lọc khỏi URL, ngoại trừ tham số `keyword`.

---

### 2.4. Thao tác dữ liệu (`ActionButtons`, `AppTableSelectedRows`)

**ActionButtons (Trên từng dòng - Row Level)**
- **Mục đích**: Chứa các nút View, Edit, Delete, v.v. cho một dòng dữ liệu (Record).
- **Tính năng cần thiết**:
  - Thu gọn thông minh (Responsive Collapse): Trên Desktop, hiển thị dạng các icon nằm ngang. Trên Mobile (hoặc khi có quá nhiều nút), gom tất cả vào một Menu thả xuống (Ellipsis Dropdown `...`).
  - Phân quyền ẩn hiện: Có thể tắt/bật quyền View, Edit, Delete thông qua props.

**AppTableSelectedRows (Thao tác hàng loạt - Bulk Actions)**
- **Mục đích**: Bảng điều khiển nổi lên khi người dùng chọn (tick) vào các dòng trong Bảng.
- **Tính năng cần thiết**:
  - Nút "Hủy chọn" (Clear Selection).
  - Hiển thị tổng số lượng đang chọn.
  - Các nút thao tác tùy chỉnh (VD: Đổi trạng thái hàng loạt, Xuất file).
  - Nút Xóa hàng loạt (Hiển thị màu Đỏ + Cảnh báo).

---

### 2.5. Cơ Chế Xác Nhận Trước Khi Lưu (Confirm-To-Save Pattern)
**Mục đích**: Thay vì lưu ngay khi bấm "Save" trong form Create/Edit, hiển thị một Modal tóm tắt lại các dữ liệu người dùng vừa nhập để xác nhận lần cuối.

**Luồng thực thi logic (Workflow):**
1. Người dùng bấm "Save" (nằm ở `AppCreate` hoặc `AppEdit` wrapper).
2. Wrapper kích hoạt hàm `Validate` của Form (Nằm bên trong nội dung con).
3. Nếu Validate thành công: Wrapper lấy toàn bộ dữ liệu (Values) của Form.
4. **Parsing Data**: Lặp qua các key của Dữ liệu Form:
   - Bỏ qua các key như `id`, `_id`, hoặc dữ liệu rỗng.
   - Nếu là Hình ảnh/URL: Parse thành thẻ `<img />` hoặc `Avatar`.
   - Nếu là Boolean: Parse thành chữ "Hoạt động" / "Tạm khóa".
   - Nếu là Object/JSON lồng nhau: Chuyển thành một Card hoặc Section nhỏ để hiển thị trực quan.
5. Hiển thị thông tin đã Parse lên một Modal "Xác nhận cập nhật".
6. Người dùng bấm "Xác nhận" -> Kích hoạt API Submit.

**Hướng dẫn triển khai trên các Ngôn ngữ khác:**
- **React**: Gọi `form.validateFields()`, lấy `values`, ánh xạ Object thành React Nodes.
- **Vue**: Bắn event (emit) hoặc dùng `ref` gọi hàm của con để kiểm tra form hợp lệ (`formRef.validate()`). Lấy form model bind lên Modal.
- **Angular**: Lấy form group (`FormGroup.value`), dùng `*ngFor` và `Pipe` để hiển thị các cặp key-value lên Angular Material Dialog.

---

## 3. Tổng kết

Khi một Agent AI nhận yêu cầu: *"Hãy tạo một màn hình Quản lý Sản phẩm sử dụng components"*:
- Agent phải hiểu cần tách màn hình thành Layout Wrapper (`AppList` / `AppCreate` / `AppEdit` / `AppShow`).
- Form/Table phải được truyền vào Layout đó.
- Cần có bộ lọc URL, phân trang, và Dropdown Actions.
- Áp dụng đúng cú pháp của framework hiện tại (React, Vue, Angular) để hoàn thiện kết nối.
