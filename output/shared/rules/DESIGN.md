# 💎 High-Fidelity Design Knowledge Process (v2.5)

> **Objective**: Define a technology-agnostic knowledge protocol for creating premium UI/UX aesthetics.
> **Scope**: Applied automatically by all Frontend Specialists as the "Core Constitution".

## 1. Visual Theme & Atmosphere
- **Triết lý**: Ưu tiên tính cô đọng (Density), sự tinh tế trong phân tầng (Elevation) và sự mượt mà trong chuyển động.
- **Vibe**: Chuyên nghiệp, hiện đại, và có chiều sâu kỹ thuật.

## 2. Color Role Architecture (Semantic)
- Không gán cứng mã màu. Sử dụng hệ thống vai trò:
    - **Surface-L0/L1/L2**: Nền cơ sở và các lớp chồng phía trên.
    - **Brand-Primary**: Màu nhận diện chính.
    - **Accent-Glow**: Màu cho các hiệu ứng điểm nhấn (Glow/Neon).
    - **Critical/Warning/Success**: Màu trạng thái chức năng.

## 3. Typography Hierarchy
- **Font-Family**: Sử dụng Sans-serif hiện đại cho UI (Inter, Outfit) và Serif tinh tế cho nội dung dài.
- **Weight Gradient**: Luôn ưu tiên thay đổi độ dày font (`font-weight`) để phân cấp thay vì chỉ thay đổi kích thước.
- **Precision**: Một số phong cách yêu cầu `negative letter-spacing` (-0.02em đến -0.05em) để tạo cảm giác cô đọng.

## 4. Component Knowledge (Atomic Patterns)
- **Buttons**: Trạng thái hover phải có phản hồi tactile (shadow hoặc spring-scale).
- **Cards**: Sử dụng `border-radius` nhất quán. Phân biệt rõ ranh giới bằng `border` mỏng (`1px`) và `subtle shadow`.
- **Inputs**: Trọng tâm là trạng thái `Focus` (Glow hiệu ứng hoặc Stroke rõ ràng).

## 5. Layout & Spacing Principles
- **The Grids**: Sử dụng hệ thống 8px hoặc 4px làm cơ sở.
- **Breathing Room**: Ưu tiên khoảng cách (`Padding/Margin`) rộng rãi để giảm tải nhận thức cho người dùng.
- **Compaction**: Trong các dashboard kỹ thuật, tăng mật độ thông tin bằng cách giảm padding nhưng phải tăng sự rõ ràng về typography.

## 6. Depth & Elevation (Z-Index Logic)
- Sử dụng các lớp đổ bóng phức hợp (Multiple Shadows) thay vì một lớp bóng đậm.
- **Glassmorphism**: Áp dụng `backdrop-filter` (Blur) kết hợp với `border` trắng mờ để tạo cảm giác kính.

## 7. Responsive Behavior (Fluid Design)
- Không chỉ dừng ở `Mobile/Desktop`. Thiết kế phải co giãn mượt mà giữa các điểm ngắt.
- Ưu tiên công nghệ `Grid` và `Flexbox` hiện đại.

## 8. Anti-Patterns (Do's and Don'ts)
- **Don't**: Dùng màu đen thuần (#000) trên nền sáng. Hãy dùng màu xám cực đậm.
- **Don't**: Dùng quá nhiều border màu đậm. Hãy dùng shadow hoặc thay đổi sắc độ nền.
- **Do**: Luôn kiểm tra độ tương phản (Accessibility).

## 9. Agent Design Prompting Guide
- Khi yêu cầu thiết kế, hãy cung cấp: "Mục tiêu (Context), Đối tượng (Users), Cảm xúc (Vibe), và Nền tảng (Framework)".

---
*Unified AI Toolkit — Universal Design Protocol*
