# BẢNG CA KIỂM — DT042 Tìm đường đi quân mã qua mọi ô

## Hợp đồng input/output

| Tham số | Kiểu | Ràng buộc | Ghi chú |
|---|---|---|---|
| n | Int | 1 <= n <= 5 | Kích thước bàn cờ n x n |
| Điểm đầu | (Int, Int) | Cố định (1,1) | Không thay đổi |
| Bàn cờ | Không có vật cản | — | Tất cả ô đều có thể đi |

**Kết quả:**
- Nếu tìm được: danh sách n² tọa độ [(r1,c1), (r2,c2), ...] — đường đi hợp lệ
- Nếu không tìm được: nothing (hoặc thông báo "khong_co_duong_di")

**Validator từ chối khi:**
- n < 1 hoặc n > 5: báo lỗi "n phai trong [1,5]"
- n không phải số nguyên: báo lỗi "n phai la so nguyen"

**Phân biệt:**
- "Bài toán hợp lệ nhưng không có nghiệm" (n=2,3,4): trả về nothing, không phải lỗi
- "Input sai" (n=0, n=6, n=-1): validator từ chối trước khi chạy thuật toán

---

## Giải tay Ví dụ 1 và Ví dụ 2

### Ví dụ 1: n=1
- Bàn cờ 1x1, chỉ có ô (1,1)
- Bước 1: đặt quân mã tại (1,1), ban[1][1] = 1
- buoc = 1 = n² = 1 → tìm thấy ngay
- Đường đi: [(1,1)] — không cần nước đi nào
- Kiểm: length=1 ✓, (1,1) là điểm đầu ✓, không có cặp liên tiếp để kiểm ✓
- Expected: duong = [(1,1)], kiem_tra_duong trả true

### Ví dụ 2: n=3
- Bàn cờ 3x3, cần thăm 9 ô
- Từ (1,1), các nước đi hợp lệ: (1+2,1+1)=(3,2), (1+1,1+2)=(2,3)
  Các ô (1-2,..), (1,..-1) không hợp lệ (ngoài bàn)
- Thử (3,2): từ (3,2) có thể đến (1,1)[đã thăm], (1,3), (2,4)[ngoài]...
  → (1,3): từ (1,3) chỉ đến (2,1), (3,2)[đã thăm]
    → (2,1): từ (2,1) chỉ đến (1,3)[đã thăm], (3,3), (3,2)[?]...
      → (3,3): từ (3,3) chỉ đến (1,2), (2,1)[đã thăm]
        → (1,2): từ (1,2) chỉ đến (2,4)[ngoài], (3,1), (3,3)[đã thăm]
          → (3,1): từ (3,1) chỉ đến (1,2)[đã thăm], (2,3), (1,0)[ngoài]
            → (2,3): từ (2,3) chỉ đến (1,1)[đã thăm], (3,1)[đã thăm]... hết nước đi
            Rút lui khỏi (2,3) → rút lui khỏi (3,1) → ...
- Sau khi thử hết tất cả nhánh từ (1,1), không có đường nào đủ 9 ô
- Expected: nothing (khong_co_duong_di)

---

## Bảng truy vết tay — Ca nhỏ n=2 (bàn 2x2, cần 4 bước)

| Bước | Thao tác | Tọa độ hiện tại | ban[][] | duong | Giải thích |
|---|---|---|---|---|---|
| Init | Đặt bước 1 tại (1,1) | (1,1) | [1,0;0,0] | [(1,1)] | ban[1][1]=1, buoc=1 |
| 1 | thu_ma(1,1,1): thử nước đi từ (1,1) | — | — | — | 8 hướng, chỉ (r2,c2) trong [1,2] và ban=0 |
| 1.1 | k=1: (1+2,1+1)=(3,2) → ngoài bàn | — | — | — | 3>2, bỏ qua |
| 1.2 | k=2: (1+2,1-1)=(3,0) → ngoài bàn | — | — | — | 3>2 và 0<1 |
| 1.3 | k=3: (1-2,1+1)=(-1,2) → ngoài bàn | — | — | — | -1<1 |
| 1.4 | k=4: (1-2,1-1)=(-1,0) → ngoài bàn | — | — | — | -1<1 |
| 1.5 | k=5: (1+1,1+2)=(2,3) → ngoài bàn | — | — | — | 3>2 |
| 1.6 | k=6: (1+1,1-2)=(2,-1) → ngoài bàn | — | — | — | -1<1 |
| 1.7 | k=7: (1-1,1+2)=(0,3) → ngoài bàn | — | — | — | 0<1 và 3>2 |
| 1.8 | k=8: (1-1,1-2)=(0,-1) → ngoài bàn | — | — | — | 0<1 |
| 2 | Không có nước đi hợp lệ từ (1,1) sau bước 1 | — | — | — | Quay lui ngay |
| KQ | Kết thúc thu_ma(1,1,1): da_tim=false | — | [1,0;0,0] | [(1,1)] | Rút lui: ban[1][1]=0, pop (1,1) |
| KQ | giai_bai(2): trả về nothing | — | | | Không tìm được đường |

*Nhận xét: Bàn 2x2 không thể có đường đi quân mã vì từ (1,1) không có nước đi hợp lệ nào trong bàn 2x2 (tất cả ô kề của quân mã đều ngoài bàn).*

---

## Giả mã chi tiết (theo tên biến thực tế trong code)

```
# Hằng 8 nước đi quân mã (1-indexed)
DR = [2, 2, -2, -2, 1,  1, -1, -1]
DC = [1, -1,  1, -1, 2, -2,  2, -2]

# Validator
function kiem_tra_dau_vao(n):
    if not isinteger(n): throw "n phai la so nguyen"
    if n < 1 or n > 5: throw "n phai trong [1,5]; nhan duoc n=$n"

# Kiểm ô hợp lệ (trong bàn và chưa thăm)
function nuoc_di_hop_le(r, c, ban, n):
    return 1 <= r <= n and 1 <= c <= n and ban[r][c] == 0

# Đệ quy quay lui
# Bất biến vào: ban[r][c] = buoc; 1<=buoc<=n*n
# Bất biến ra: nếu da_tim[]=true thì duong chứa n*n tọa độ hợp lệ
function thu_ma(ban, r, c, buoc, n, duong, da_tim):
    if buoc == n*n:
        da_tim[] = true
        return
    for k = 1..8:
        r2 = r + DR[k]; c2 = c + DC[k]
        if nuoc_di_hop_le(r2, c2, ban, n):
            ban[r2][c2] = buoc + 1
            push!(duong, (r2, c2))
            thu_ma(ban, r2, c2, buoc+1, n, duong, da_tim)
            if da_tim[]: return     # đã tìm, không thử nữa
            pop!(duong)             # rút lui
            ban[r2][c2] = 0

# Kiểm nghiệm đường đi
function kiem_tra_duong(duong, n):
    N = n*n
    if length(duong) != N: return false, "do dai sai"
    if duong[1] != (1,1): return false, "khong bat dau tu (1,1)"
    if length(Set(duong)) != N: return false, "co o lap"
    for (r,c) in duong:
        if not (1<=r<=n and 1<=c<=n): return false, "toa do ngoai ban"
    for i = 1..N-1:
        (r1,c1) = duong[i]; (r2,c2) = duong[i+1]
        dr = abs(r2-r1); dc = abs(c2-c1)
        if not ({dr,dc} == {1,2}): return false, "nuoc di khong hop le tai buoc $i"
    return true, "hop le"

# Hàm chính
function giai_bai(n):
    kiem_tra_dau_vao(n)   # ném lỗi nếu sai
    ban = zeros(Int, n, n)
    ban[1][1] = 1
    duong = [(1,1)]
    da_tim = Ref(false)
    thu_ma(ban, 1, 1, 1, n, duong, da_tim)
    if da_tim[]:
        ok, msg = kiem_tra_duong(duong, n)
        assert ok
        return duong
    else:
        return nothing
```

---

## Độ phức tạp

| Pha | Phép toán chính | Độ phức tạp |
|---|---|---|
| Kiểm tra input | So sánh n | O(1) |
| Chuẩn bị bảng | Khởi tạo n×n ô | O(n²) |
| Lõi thuật toán (quay lui) | Duyệt cây 8 nhánh đến sâu n² | O(8^(n²)) worst case |
| Kiểm nghiệm kết quả | Duyệt đường n² phần tử | O(n²) |
| In kết quả | In n² tọa độ | O(n²) |

**Bộ nhớ:** O(n²) — bảng ban[] + danh sách duong[]

*Ghi chú: Với n<=5 (N<=25), thuật toán thực tế kết thúc rất nhanh nhờ cắt nhánh.
Không thể kết luận tốc độ tăng chính xác chỉ từ n=1..5.*

---

## Bảng >= 12 ca kiểm độc lập

| ID | Nguồn & Đối tượng | Input | Mục tiêu | Expected & Cách tính |
|---|---|---|---|---|
| VD01 | Phiếu Ví dụ 1 — giai_bai | n=1 | Bàn 1 ô, tìm đường | duong=[(1,1)]; tính tay: chỉ 1 ô, không cần nước đi |
| VD02 | Phiếu Ví dụ 2 — giai_bai | n=3 | Bàn 3x3, không có đường | nothing; tính tay + biết kết quả đã biết từ lý thuyết |
| P1 | Phiếu Ca 1 — kiem_tra_duong | duong=[(1,1)], n=1 | Kiểm nghiệm chấp nhận [(1,1)] | (true,"hop le"); tính: đủ 1 ô, bắt đầu (1,1), không cặp liên tiếp cần kiểm |
| P2 | Phiếu Ca 2 — giai_bai | n=2 | Bàn 2x2, không có đường | nothing; tính tay: (1,1) không có nước đi trong bàn 2x2 |
| P3 | Phiếu Ca 3 — giai_bai | n=3 | Bàn 3x3, không có đường | nothing; đồng với VD02 |
| P4 | Phiếu Ca 4 — giai_bai | n=4 | Bàn 4x4, không có open tour từ (1,1) | nothing; kết quả đã biết từ lý thuyết knight's tour |
| P5 | Phiếu Ca 5 — giai_bai + kiem_tra_duong | n=5 | Bàn 5x5, có đường; không ép thứ tự | length(duong)==25 và kiem_tra_duong(duong,5)==true; không so cứng tọa độ |
| TK01 | Tự thiết kế — kiem_tra_duong | duong=[(1,1),(2,3),(1,1)], n=2 | Phát hiện tọa độ lặp | (false,"co o lap"); tính: Set có 2 phần tử thay vì 4 |
| TK02 | Tự thiết kế — kiem_tra_duong | duong=[(1,1),(2,2)], n=2 | Phát hiện nước đi không hợp lệ | (false,"nuoc di khong hop le..."); |dr|=1,|dc|=1 không phải {1,2} |
| BIEN01 | Ca biên — giai_bai, n nhỏ nhất | n=1 | Biên dưới miền hợp lệ | duong=[(1,1)]; tính tay n²=1 |
| BIEN02 | Ca biên — giai_bai, n lớn nhất | n=5 | Biên trên miền hợp lệ | length(duong)==25 và kiem_tra_duong true |
| BIEN03 | Ca biên — kiem_tra_duong không bắt đầu (1,1) | duong=[(2,1),(1,3)], n=2 | Phát hiện điểm đầu sai | (false,"khong bat dau tu (1,1)") |
| LOI01 | Input sai — kiem_tra_dau_vao | n=0 | Validator từ chối n<1 | throws/returns error "n phai trong [1,5]" |
| KT09 | Input sai — kiem_tra_dau_vao | n=6 | Validator từ chối n>5 | throws/returns error "n phai trong [1,5]" |
| KT10 | Input sai — kiem_tra_dau_vao | n=-1 | Validator từ chối n âm | throws/returns error "n phai trong [1,5]" |
| KT11 | Ca biên — kiem_tra_duong độ dài sai | duong=[(1,1)], n=2 | Phát hiện thiếu ô | (false,"do dai sai"); length=1 != n²=4 |
| KT12 | Ca biên — kiem_tra_duong tọa độ ngoài bàn | duong=[(1,1),(3,2),(1,3),(2,1)], n=2 | Phát hiện ô ngoài bàn | (false,"toa do ngoai ban"); (3,2) có r=3>n=2 |

### Ghi chú phân biệt số ca và số assert

- 17 ca độc lập trong bảng trên (ID khác nhau, mục tiêu khác nhau)
- Số assert >= số ca (mỗi ca có thể có nhiều @test)
- Ca P3 và VD02 kiểm cùng giai_bai(3)=nothing nhưng P3 là ca phiếu bắt buộc (được tính riêng cho bảng ánh xạ), VD02 là ca ví dụ phiếu — hai mục tiêu khác nhau (ví dụ vs ca bắt buộc phiếu)

### Ba quy mô khảo sát Q1, Q2, Q3

| Quy mô | n | N=n² | Phép đo |
|---|---|---|---|
| Q1 | n=1 | N=1 | Đếm số nút đã gọi (so_nut) và số lần rút lui (so_rut) |
| Q2 | n=3 | N=9 | Đếm số nút đã gọi và số lần rút lui |
| Q3 | n=5 | N=25 | Đếm số nút đã gọi và số lần rút lui |

*Lưu ý: n=2,4 không có nghiệm nên số nút có thể lớn hơn n=1,3,5. Chọn Q1,Q2,Q3 theo gợi ý phiếu (đếm nút/rút lui, không đo thời gian vì n nhỏ). Kích thước cố định (n<=5) nên dùng ba giá trị n khác nhau làm ba "cấu hình".*
