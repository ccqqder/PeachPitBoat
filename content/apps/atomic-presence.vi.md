---
title: Atomic Presence
layout: simple
description: "Trước Deepfake và chỉnh sửa ác ý, hãy bảo vệ tính xác thực của bạn bằng hash chain mật mã và chữ ký số."
images:
  - images/og/atomic-presence.png
app_slug: atomic-presence
showDate: false
showReadingTime: false
---

## Trong kỷ nguyên Deepfake, thứ thực sự khan hiếm là tính xác thực có thể kiểm chứng

Việc hạ thấp rào cản sản xuất video và âm thanh nhìn chung là điều tốt. Vấn đề là chi phí để dựng giả, biên tập lại và tách khỏi ngữ cảnh cũng giảm theo, khiến "tôi đã ghi lại" ngày càng xa "tôi có thể chứng minh mọi thứ đã diễn ra đúng như vậy". Atomic Presence lấp khoảng trống đó: ngay khi bạn nhấn ghi, ứng dụng cho phép bạn bắt đầu xây dựng chuỗi bằng chứng có thể kiểm chứng.

Ứng dụng được thiết kế cho các tình huống mà bạn lo ngại bản ghi sẽ bị tranh cãi về sau: phỏng vấn, lời khai nhân chứng, whistleblowing, hiện trường có tranh chấp, hoặc bất kỳ bối cảnh nào bản ghi có thể bị phản bác, cắt ghép lại hoặc giả mạo. Nhu cầu ghi lại thường nhật thông thường không phải mục tiêu chính.

## Khác gì so với công cụ ghi hình thông thường

Phần lớn công cụ ghi hình đều theo cách "ghi file trước, bảo toàn tính toàn vẹn tính sau". Atomic Presence đan hash chain, QR code động và chữ ký số vào ngay luồng ghi trong lúc diễn ra. Tính kiểm chứng là lõi sản phẩm ngay từ đầu, không phải bản vá thêm vào sau.

Vì vậy, nó giống một công cụ phòng vệ kỹ thuật cho các kịch bản rủi ro. Có thể bạn không dùng mỗi ngày, nhưng khi cần, bạn sẽ muốn ứng dụng đã cài sẵn và quy trình đã quen tay, thay vì cuống cuồng ghép công cụ vào phút chót.

## Vì sao có bốn cấp bảo vệ: rủi ro khác nhau, chi phí khác nhau

Các cấp bảo vệ phản ánh khác biệt thực tế giữa các kịch bản. Có lúc bạn chỉ cần phát tín hiệu "đang ghi" cho bên còn lại; có lúc bạn cần mức gần với kiểm chứng toàn vẹn ở mức bằng chứng. Có các bước trung gian giúp công cụ đi vào quy trình thật, thay vì chỉ có công tắc bật/tắt thô.

Với nhà báo, người làm pháp lý, nhà báo công dân và bất kỳ ai thường xuyên cần bản ghi cuộc trò chuyện rõ ràng, điều này rất có giá trị. Thứ họ cần là một công cụ ghi hình có ít vùng mơ hồ hơn; thêm bộ lọc hay chế độ làm đẹp sẽ không giải quyết vấn đề.

## Quyền riêng tư và offline là một phần của độ tin cậy

Một công cụ tự nhận bảo vệ tính xác thực sẽ mất uy tín nếu xử lý dữ liệu cốt lõi phụ thuộc nhiều vào máy chủ bên ngoài. Atomic Presence giữ các tính toán quan trọng trên thiết bị, một phần vì quyền riêng tư, một phần để giảm phụ thuộc bên thứ ba ngay trong chuỗi bằng chứng. Càng ít bên thứ ba đi qua dữ liệu của bạn, về sau càng dễ giải thích điều gì đã xảy ra và điều gì không.

Nếu bạn muốn một công cụ ghi hình có cơ hội thuyết phục người khác tốt hơn khi nổ ra tranh chấp, hãy làm quen với Atomic Presence trước khi bạn thực sự cần đến nó.
