# PHIẾU GIAO ĐỀ TÀI CÁ NHÂN — DT042

**Trích nguyên văn từ** `Danh_sach_va_de_giao/91_Phieu_giao_de_tai_INT13185_N03.docx`

---

## Thông tin chung

| Trường | Giá trị |
|---|---|
| Môn học | INT13185 — Cấu trúc dữ liệu và giải thuật |
| Nhóm | 03 |
| Giảng viên | Hồ Nhựt Minh |
| Sinh viên | Từ Lê Nhật Long |
| MSSV | N24DCDT047 |
| Lớp | D24CQDT01-N |
| Mã đề | DT042 |
| Tên đề | Tìm đường đi của quân mã qua mọi ô |

---

## Căn cứ giáo trình

Chương 3, Bài tập chương 3, câu 27: Bài toán mã đi tuần;
trang in 86; trang PDF 98.

---

## Đề bài

Viết chương trình tìm một đường đi của quân mã trên bàn cờ nhỏ, sao cho mỗi ô được thăm đúng một lần. Sinh viên tạo các nước đi hợp lệ từ vị trí hiện tại, đánh dấu ô đã thăm và quay lui khi không đi tiếp được. Bài làm chú trọng kiểm tra đường đi nhận được thay vì chỉ tin vào thông báo tìm thấy.

---

## Dữ liệu vào

Nhập n hoặc khai báo trong code; 1 <= n <= 5, điểm đầu cố định (1, 1). Quân mã đi lệch 2 hàng và 1 cột hoặc 1 hàng và 2 cột. Bàn cờ không có vật cản; không yêu cầu quay về điểm đầu.

---

## Kết quả ra

In một danh sách n^2 tọa độ theo thứ tự thăm, hoặc thông báo không có đường đi. Có thể in bảng đánh số bước để nhìn rõ lời giải.

---

## Ví dụ 1

| Dữ liệu vào | Kết quả chính |
|---|---|
| n=1 | duong=[(1, 1)] |

Một ô đã được thăm hết ngay từ trạng thái đầu, không cần một nước đi.

---

## Ví dụ 2

| Dữ liệu vào | Kết quả chính |
|---|---|
| n=3 | khong_co_duong_di |

Từ ô giữa không có nước đi nào trên bàn 3x3, nên không thể có đường đi qua mọi ô.

---

## Hướng dẫn thực hiện 5 bước

1. Khai báo tám độ lệch hàng, cột của quân mã; viết kiểm ô còn trong bàn và chưa được thăm.
2. Đặt bước 1 ở (1, 1); hàm thu(r, c, buoc) lần lượt thử các ô có thể đi đến.
3. Đánh số ô được chọn, gọi bước sau; rút lại số về 0 nếu lời gọi không tìm được lời giải.
4. Khi buoc = n^2, lưu đường đi và trả về; không cần nối lại ô cuối với ô đầu.
5. Kiểm danh sách tọa độ đủ n^2 ô khác nhau và từng cặp liên tiếp có đúng dạng nước đi quân mã.

---

## Các hàm nên viết

- nuoc_di_hop_le(r, c, ban) -- kiểm ô (r,c) nằm trong bàn và chưa thăm
- thu_ma(r, c, buoc) -- đệ quy quay lui thử nước đi tiếp theo
- kiem_tra_duong(duong, n) -- kiểm nghiệm đường đi nhận được

---

## 5 Ca kiểm tra bắt buộc của phiếu

| # | n | Kết quả kỳ vọng |
|---|---|---|
| 1 | n=1 | Đường chỉ gồm (1,1); bộ kiểm phải chấp nhận |
| 2 | n=2 | Không có đường đi thăm đủ bốn ô |
| 3 | n=3 | Không có đường đi thăm đủ chín ô |
| 4 | n=4 | Không có đường đi mở thăm đủ 16 ô từ điểm đầu |
| 5 | n=5 | Chấp nhận một đường đủ 25 ô hợp lệ; không ép cùng một thứ tự tọa độ |

---

## Phân tích và nhận xét

Mỗi ô có tối đa 8 nước thử; chặn thô theo độ sâu N = n^2 là O(8^N), còn đánh dấu giúp bỏ nhiều nhánh thực tế. Bộ nhớ bảng và đường đi O(N). Đếm nút đã gọi và số lần phải rút lui; không kết luận thuật toán nhanh cho bàn lớn chỉ từ các bàn rất nhỏ.

---

## Yêu cầu thêm / tùy chọn

Sau khi phần cơ bản chạy đúng: ưu tiên nước đi tới ô có ít đường đi tiếp như heuristic Warnsdorff nêu trong câu 27 và so số nút.

---

## Rubric và minh chứng đúng từng đề (từ 00_HUONG_DAN_SINH_VIEN.html)

DT042 - N24DCDT047 - Từ Lê Nhật Long — Tìm đường đi của quân mã qua mọi ô

- Lần vết chuyên biệt (C2, C3): Bảng bước, tọa độ, dấu ô khi thử/rút trên bàn cờ nhỏ.
- Bất biến hoặc lập luận đúng (C2, C3, C4): Đường bắt đầu (1,1), đủ n^2 ô khác nhau; chênh hàng/cột là (1,2)/(2,1); không yêu cầu đóng.
- Kiểm tra kỳ vọng và ca biên (C3, C4): n=1 một ô; n=2,3,4 không có; n=5 kiểm đủ 25 ô, không ép cùng nghiệm. Chọn ca theo miền phiếu; không xem ca rỗng, âm là hợp lệ.
