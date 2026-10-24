# GHI CHÚ GIÁO TRÌNH — DT042

**Nguồn:** Giao-trinh-Cau-truc-du-lieu-va-Giai-thuat-INT1306.pdf
**Chương 3, Bài tập chương 3, câu 27 — Bài toán mã đi tuần (Knight''s Tour)**
**Trang in 86; trang PDF 98**

---

## Tóm tắt định nghĩa và thuật toán (Chương 3)

### Quay lui (Backtracking)

Quay lui là kỹ thuật tìm kiếm vét cạn có hệ thống: xây dựng nghiệm theo từng bước,
tại mỗi bước thử các ứng viên hợp lệ; nếu không có ứng viên nào dẫn đến nghiệm
thì rút lui về bước trước và thử ứng viên tiếp theo.

**Giả mã tổng quát quay lui:**
```
procedure quay_lui(buoc)
    if buoc > N then
        lưu nghiệm; return
    for each ung_vien in tap_ung_vien(buoc) do
        if hop_le(ung_vien, buoc) then
            chon(ung_vien, buoc)
            quay_lui(buoc + 1)
            if da_tim_thay then return   // nếu chỉ cần 1 nghiệm
            huy_chon(ung_vien, buoc)    // rút lui
```

---

## Bài toán mã đi tuần (Knight''s Tour Problem)

### Mô tả

Quân mã (chess knight) trên bàn cờ n×n xuất phát từ ô (1,1). Cần tìm một đường đi
sao cho mỗi ô được thăm đúng một lần (n² lượt thăm tổng cộng).

### 8 nước đi hợp lệ của quân mã

Từ ô (r, c), quân mã có thể đến 8 ô sau:
```
(r+2, c+1), (r+2, c-1)
(r-2, c+1), (r-2, c-1)
(r+1, c+2), (r+1, c-2)
(r-1, c+2), (r-1, c-2)
```
dr = [2,  2, -2, -2,  1,  1, -1, -1]
dc = [1, -1,  1, -1,  2, -2,  2, -2]

### Điều kiện hợp lệ của ô (r2, c2) kế tiếp

1. 1 <= r2 <= n và 1 <= c2 <= n (trong bàn cờ)
2. ban[r2][c2] == 0 (chưa thăm)

### Bất biến của thuật toán

- Mỗi ô được đánh số từ 1 đến n² theo thứ tự thăm (ban[r][c] = buoc).
- Khi rút lui: ban[r][c] trở về 0; buoc giảm về giá trị trước.
- Không thay đổi điểm đầu (1,1) là bước 1.
- Không yêu cầu quay về ô đầu (open tour, không phải closed tour).

### Giả mã cho bài DT042

```
# Hằng 8 nước đi
DR = [2, 2, -2, -2, 1, 1, -1, -1]
DC = [1, -1, 1, -1, 2, -2, 2, -2]

function thu_ma(ban, r, c, buoc, n, duong, da_tim)
    # Tiền điều kiện: ban[r][c] == buoc, 1<=r,c<=n
    if buoc == n*n
        lưu duong; da_tim = true; return
    for k = 1..8
        r2 = r + DR[k]; c2 = c + DC[k]
        if 1<=r2<=n và 1<=c2<=n và ban[r2][c2]==0
            ban[r2][c2] = buoc + 1
            push!(duong, (r2,c2))
            thu_ma(ban, r2, c2, buoc+1, n, duong, da_tim)
            if da_tim then return
            pop!(duong)              # rút lui
            ban[r2][c2] = 0          # hủy đánh số
    # Hậu điều kiện: mọi nhánh đã thử, không tìm được → da_tim vẫn false

function giai_ma_di_tuan(n)
    # Kiểm đầu vào: 1 <= n <= 5
    ban = zeros(Int, n, n)
    ban[1][1] = 1
    duong = [(1, 1)]
    da_tim = Ref(false)
    thu_ma(ban, 1, 1, 1, n, duong, da_tim)
    if da_tim[]
        return duong   # danh sách n² tọa độ
    else
        return nothing  # không có đường đi
```

### Kiểm nghiệm đường đi (kiem_tra_duong)

1. length(duong) == n²
2. duong[1] == (1, 1)
3. Không có tọa độ lặp (Set(duong) có đúng n² phần tử)
4. Mỗi (r,c) thỏa 1<=r,c<=n
5. Mỗi cặp liên tiếp (r1,c1)→(r2,c2): |r2-r1| và |c2-c1| là bộ {1,2}

### Độ phức tạp

- **Thời gian:** O(8^(n²)) trong trường hợp xấu nhất (chặn thô theo cây đệ quy),
  thực tế ít hơn nhiều nhờ cắt nhánh khi ô đã thăm.
- **Bộ nhớ:** O(n²) cho bảng ban + O(n²) cho danh sách đường đi = O(n²) tổng.

### Kết quả đã biết (tham khảo, không dùng làm expected)

- n=1: có (trivially), đường = [(1,1)]
- n=2: không có
- n=3: không có  
- n=4: không có (open tour từ (1,1))
- n=5: có (nhiều nghiệm, không ép thứ tự)

### Heuristic Warnsdorff (tùy chọn)

Ưu tiên nước đi tới ô có ít đường đi tiếp nhất (degree thấp nhất). Giảm số nút
cần khảo sát đáng kể trên bàn lớn.

---

## Quy ước chỉ số

Chỉ số từ 1 (1-indexed): hàng r từ 1→n, cột c từ 1→n.
ban[r][c] lưu bước thăm ô (r,c); = 0 nếu chưa thăm.

---

## Trang trích dẫn cho báo cáo

- Định nghĩa quay lui: Chương 3, mục tổng quát — trang in ~76-86; trang PDF ~88-98
- Bài toán mã đi tuần: Chương 3, Bài tập câu 27 — trang in 86; trang PDF 98
- Heuristic Warnsdorff: Chương 3, câu 27 (chú thích hoặc mục 3.6)
