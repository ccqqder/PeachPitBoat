---
title: Hỗ Trợ Atomic Presence
layout: simple
summary: Support and contact for Atomic Presence
app_slug: atomic-presence
showDate: false
showReadingTime: false
---

[App Store](https://apps.apple.com/app/id6759192866) · [Chính Sách Quyền Riêng Tư](/en/privacy/atomic-presence/)

---

## Câu hỏi thường gặp

**H: QR code trong video bị mờ và không quét được khi xác minh?**  
Đ: Hãy đảm bảo độ sáng màn hình đủ cao khi ghi và giữ camera cách màn hình 30–50 cm. QR code cập nhật mỗi giây một lần — camera cần lấy nét rõ. Nếu vẫn gặp lỗi, hãy thử giảm độ phân giải ghi.

**H: Xác minh watermark âm thanh bị thất bại?**  
Đ: Xác minh watermark có thể thất bại nếu: âm thanh bị nén quá mạnh (ví dụ chuyển tiếp qua WhatsApp), âm thanh bị cắt ngắn, hoặc có quá nhiều tạp âm nền. Hãy ghi trong môi trường yên tĩnh và dùng tệp âm thanh gốc để xác minh.

**H: Chữ ký số không hợp lệ trên thiết bị mới?**  
Đ: Khóa ký của mỗi thiết bị được lưu trong iOS Keychain, và thiết bị mới sẽ tạo khóa khác. Bạn KHÔNG cần xuất khóa công khai thủ công — mỗi `.evidence.json` do ứng dụng ghi ra đã nhúng sẵn khóa công khai dùng cho chữ ký của bản ghi đó, nên bất kỳ bên xác minh nào có tệp bằng chứng đều có thể xác minh, bất kể đang dùng thiết bị nào.

**H: Ứng dụng bị crash khi đang ghi — tệp còn không?**  
Đ: Khi ứng dụng crash bất ngờ, các bản ghi chưa hoàn chỉnh có thể vẫn nằm trong thư mục Documents. Mở lại ứng dụng, nhấn nút **VERIFY** ở đầu màn hình chính, rồi kiểm tra ba tab (Cấp 1 / Cấp 2 / Cấp 3) để tìm tệp có thể khôi phục.

**H: Xác minh hash chain báo "integrity broken" nhưng tôi không chỉnh sửa bản ghi?**  
Đ: Nguyên nhân có thể gồm: ứng dụng bị hệ thống ngắt trong lúc ghi, pin yếu, hoặc lỗi ghi do thiếu dung lượng. Hãy đảm bảo đủ pin và dung lượng lưu trữ trước khi ghi.

---

## Khắc phục sự cố

1. **Đảm bảo thiết bị còn đủ dung lượng** (khuyến nghị còn trống ít nhất 2 GB)
2. **Giữ màn hình luôn bật khi ghi** để tránh hệ thống làm gián đoạn
3. **Buộc đóng và mở lại ứng dụng**
4. **Kiểm tra phiên bản iOS** ≥ 17.0
5. Nếu một tình huống cụ thể luôn gây lỗi, hãy chụp màn hình thông báo lỗi và gửi email cho chúng tôi

---

## Liên hệ hỗ trợ

📧 **qqder339@gmail.com**  
Tiêu đề: `[Atomic Presence] Issue Description`

Vui lòng gửi kèm: mẫu thiết bị, phiên bản iOS, phiên bản ứng dụng, chế độ ghi (video/audio), các bước tái hiện lỗi.

> Ứng dụng này không thu thập dữ liệu người dùng. Mọi thao tác mật mã đều chạy hoàn toàn trên thiết bị. Chúng tôi không có quyền truy cập bản ghi của bạn. [Xem Chính Sách Quyền Riêng Tư →](/en/privacy/atomic-presence/)
