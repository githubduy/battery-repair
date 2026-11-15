---
name: bao-cao-kt-xh-xa
description: Soạn báo cáo tình hình kinh tế - xã hội 10 tháng và ước năm của xã/phường, xây dựng kế hoạch và kịch bản tăng trưởng năm sau, đúng cấu trúc I–V của đề cương định hướng (Phụ lục) và giữ định dạng Word của báo cáo cũ. Dùng khi người dùng đưa đề cương PDF và file Word báo cáo năm trước/bản nháp và yêu cầu đối chiếu, viết lại bản v2.
---

# Báo cáo KT-XH xã/phường theo đề cương

## Khi nào dùng
- Có file đề cương định hướng (PDF, thường là "Phụ lục 02 – Đề cương định hướng báo cáo").
- Có file Word báo cáo cũ hoặc bản nháp cần viết lại theo đề cương.
- Người dùng muốn giữ định dạng Word gốc và chừa trống các số liệu chưa có (ví dụ 10 tháng).

## Quy trình

1. **Đọc đề cương (PDF).** Dùng `Read` với `pages` (ví dụ `1-5`). Nếu không hiện chữ, xem ảnh trang và ghi lại cấu trúc I–V, các chỉ tiêu bắt buộc, yêu cầu về bảng (cột nào, theo quý, nguồn số liệu, cơ quan chịu trách nhiệm). Tóm tắt vào `reference/de_cuong.md` nếu cần.
2. **Đọc Word cũ.** `pandoc -t plain file.docx` để lấy nội dung; `python-docx` để xem style. Ghi lại số liệu, đoạn văn có thể tái sử dụng và mâu thuẫn trong số liệu.
3. **Đối chiếu.** Lập danh sách: mục đề cương nào thiếu, số liệu nào mâu thuẫn, số liệu nào thiếu (10 tháng, thu nhập bình quân, dự án khởi công/hoàn thành, việc làm, KPI, số hóa đất đai...). Số liệu thiếu **không được bịa**: để trống hoặc ô `[…]` có tô vàng.
4. **Dựng bản v2.** Chạy:
   ```bash
   python3 .claude/skills/bao-cao-kt-xh-xa/scripts/build_report.py <input.docx> <output.docx>
   ```
   Script giữ nguyên khối tiêu đề, chữ ký, lề, font và các đoạn văn tái sử dụng từ file gốc (sao chép XML nên định dạng không đổi). Cột "TH 10 tháng" của Bảng 1 được để trống. Các bảng mới dùng kẻ khung, căn lề ô đã chỉnh.
5. **Kiểm tra.** `soffice --headless --convert-to pdf` rồi `pdftoppm -jpeg -r 70` và xem vài trang, đặc biệt bảng (cột không bị vỡ chữ, không lệch).
6. **Báo lại người dùng:** file đã làm, các ô trống cần điền, các mâu thuẫn số liệu đã phát hiện, và các giả định đã dùng.

## Lưu ý quan trọng
- `scripts/build_report.py` hiện chứa nội dung của **xã An Nhơn Tây** (báo cáo năm 2026, kế hoạch 2027). Với xã/phường khác, phải sửa các đoạn văn và bảng trong script; phần định dạng và khung bảng dùng lại được.
- Không ghi tên, số điện thoại hay thông tin cá nhân ngoài những gì đã có trong báo cáo gốc. Không đặt số liệu không có căn cứ.
- Với chỉ tiêu tổng hợp cấp xã (GTSP, thu nhập bình quân đầu người), dùng phương pháp và mẫu biểu do cơ quan có thẩm quyền ban hành; ghi rõ đây là số liệu ước tính.
- Tỷ trọng ngành phải cộng đúng về tổng: kiểm tra GTSP 2027 bằng tổng có trọng số của các ngành trước khi trình.
- Mục nhiệm vụ: mỗi việc quan trọng phải có "việc gì – ai chủ trì – hoàn thành khi nào – kết quả bao nhiêu".

## Tài liệu tham chiếu
- `reference/de_cuong.md`: cấu trúc I–V của đề cương và yêu cầu từng mục.
