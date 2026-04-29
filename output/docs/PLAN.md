# Orchestration Plan: Hermes Agent Review

## 1. Goal
Rà soát toàn bộ source code của `hermes-agent` (tập trung vào các file vừa chỉnh sửa như `auxiliary_client.py` và `credential_pool.py`) để phát hiện lỗi logic, lỗi cú pháp, xử lý edge case bị thiếu, và các vấn đề tiềm ẩn sau khi tích hợp API keys của Qwen, Gemini, v.v.

## 2. Orchestration Agents (Phase 2)
Để thực hiện đợt rà soát toàn diện này, 3 agent sau sẽ được khởi chạy đồng thời (song song) sau khi plan này được duyệt:

1. **`code-reviewer`**
   - **Nhiệm vụ**: Phân tích tĩnh (static analysis) mã nguồn Python. Rà soát việc import module, scope của các biến trong `_EXPLICIT_PROVIDERS` và `_EXPLICIT_ENVS`, kiểm tra xem code có nguy cơ văng exception (như `KeyError`, `ImportError`, `AttributeError`) hay không.
2. **`security-auditor`**
   - **Nhiệm vụ**: Đánh giá cách các API keys được load từ `os.getenv` và lưu trữ trong bộ nhớ (`credential_pool.py`). Kiểm tra xem liệu thông tin nhạy cảm có nguy cơ bị in ra log (logger.debug) hay không.
3. **`test-engineer`**
   - **Nhiệm vụ**: Chạy các script xác thực (verification scripts) nếu có, và thiết kế các test cases kiểm tra các luồng fallback khi `api_key` trống hoặc không hợp lệ.

## 3. Verification
Sẽ tiến hành chạy các script/công cụ để xác minh trạng thái mã nguồn.
- Rà soát các cú pháp bằng tools nội bộ.

---
*Created by: `project-planner` agent*
