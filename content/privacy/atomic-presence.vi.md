---
title: Atomic Presence — Chính Sách Quyền Riêng Tư
layout: simple
showDate: false
showReadingTime: false
---

**Cập nhật lần cuối: 2026-04-15**

---

## 1. Tổng quan

Atomic Presence, được phát triển bởi QQder339, là công cụ chống deepfake sử dụng hash chain mật mã, chữ ký số và watermarking âm thanh để giúp người dùng tự xác minh tính toàn vẹn của bản ghi.

**Tóm tắt: Chúng tôi KHÔNG thu thập, lưu trữ hoặc truyền bất kỳ dữ liệu cá nhân nào của bạn tới máy chủ bên ngoài. Mọi thao tác mật mã và xác minh đều được thực hiện trên thiết bị.**

## 2. Dữ liệu chúng tôi KHÔNG thu thập

Ứng dụng này không thu thập:

- Thông tin định danh cá nhân (tên, email, số điện thoại)
- Dữ liệu vị trí
- Mã định danh thiết bị
- Dữ liệu phân tích sử dụng hoặc theo dõi

## 3. Dữ liệu lưu cục bộ

Các dữ liệu sau chỉ được lưu trên thiết bị của bạn và không bao giờ truyền ra ngoài:

- **Tệp Âm Thanh/Video**: toàn bộ nội dung ghi được lưu trong bộ nhớ cục bộ của thiết bị
- **Bản ghi Hash chain**: chuỗi hash SHA-256 và dữ liệu xác minh tương ứng
- **Chữ ký số**: dữ liệu chữ ký được tạo bởi thuật toán Curve25519 trên thiết bị
- **Báo cáo xác minh**: báo cáo toàn vẹn và bản ghi metadata
- **Mã định danh thiết bị đã ẩn danh**: mỗi `.evidence.json` nhúng tiền tố hex 16 ký tự của `SHA-256(identifierForVendor)`, chỉ dùng để liên kết các bản ghi từ cùng một thiết bị trong quá trình xác minh. Mã định danh này chỉ tồn tại trong tệp bằng chứng trên thiết bị của bạn, không bao giờ được truyền tới bất kỳ máy chủ nào, và không thể đảo ngược về thông tin thiết bị gốc

## 4. Tính năng mật mã (hoàn toàn offline)

Mọi tính năng cốt lõi đều chạy trên thiết bị mà không cần kết nối mạng:

- **Tạo Hash chain**: chuỗi hash SHA-256 thời gian thực; mọi tính toán chạy cục bộ
- **Ký số**: dùng thuật toán Curve25519 để ký bản ghi trên thiết bị
- **Watermarking âm thanh**: nhúng tín hiệu FSK vào bản ghi; toàn bộ xử lý tín hiệu chạy trên thiết bị
- **Xác minh**: kiểm tra toàn vẹn được tính toán cục bộ

## 5. Lưu ý quan trọng

Nội dung được ứng dụng xử lý (âm thanh, video) có thể chứa thông tin nhạy cảm. Mọi xử lý đều diễn ra trên thiết bị của bạn, và **chúng tôi không thể và sẽ không bao giờ truy cập bất kỳ nội dung ghi nào của bạn**.

## 6. Dịch vụ bên thứ ba

Ứng dụng này **KHÔNG** sử dụng bất kỳ framework phân tích hay quảng cáo bên thứ ba nào (No Google Analytics, No Facebook SDK, No Ads).

## 7. Truy cập mạng

Ứng dụng này **không yêu cầu kết nối mạng** để dùng tất cả tính năng. Truy cập mạng duy nhất là:

- **Liên kết ngoài**: mở trình duyệt khi chạm vào liên kết liên quan

## 8. Liên hệ

📧 **qqder339@gmail.com**  
Tiêu đề: Yêu cầu về Chính Sách Quyền Riêng Tư của Atomic Presence
