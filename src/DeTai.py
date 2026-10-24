"""
DT042 — Tìm đường đi của quân mã qua mọi ô (Knight's Tour)
Module: DeTai.py

Sinh viên  : Từ Lê Nhật Long
MSSV       : N24DCDT047
Lớp        : D24CQDT01-N
Môn học    : INT13185 — Cấu trúc dữ liệu và giải thuật, Nhóm 03
Giáo trình : Chương 3, Bài tập câu 27, trang in 86, trang PDF 98
Ngôn ngữ   : Python 3 (thay thế Julia theo yêu cầu sinh viên)

Hợp đồng input/output
----------------------
Input  : n (int), 1 ≤ n ≤ 5, điểm đầu cố định (1,1) — chỉ số từ 1
Output : list[(int,int)] gồm n² tọa độ theo thứ tự thăm, hoặc None
Từ chối: ném ValueError nếu n ngoài [1,5] hoặc không phải int
"""

# ---------------------------------------------------------------------------
# Hằng số: 8 nước đi hợp lệ của quân mã (delta hàng, delta cột)
# Quân mã lệch 2 hàng 1 cột hoặc 1 hàng 2 cột — tất cả 8 hướng
# ---------------------------------------------------------------------------
DR = [2,  2, -2, -2,  1,  1, -1, -1]
DC = [1, -1,  1, -1,  2, -2,  2, -2]


def kiem_tra_dau_vao(n):
    """
    Kiểm tra tính hợp lệ của đầu vào n.

    Hợp đồng
    --------
    - n phải là kiểu int (hoặc có thể chuyển sang int không mất mát)
    - 1 ≤ n ≤ 5

    Hành vi
    -------
    - Nếu hợp lệ : trả về None (không làm gì)
    - Nếu không  : ném ValueError với thông báo rõ lý do từ chối

    Ví dụ
    -----
    >>> kiem_tra_dau_vao(5)          # ok
    >>> kiem_tra_dau_vao(0)
    ValueError: n phai trong [1,5]; nhan duoc n=0
    """
    if not isinstance(n, (int,)) or isinstance(n, bool):
        raise ValueError(
            f"n phai la so nguyen int; nhan duoc kieu {type(n).__name__}"
        )
    if n < 1 or n > 5:
        raise ValueError(
            f"n phai trong [1,5]; nhan duoc n={n}"
        )


def nuoc_di_hop_le(r2: int, c2: int, ban: list, n: int) -> bool:
    """
    Kiểm tra ô (r2, c2) có phải nước đi hợp lệ tiếp theo không.

    Điều kiện hợp lệ
    ----------------
    1. 1 ≤ r2 ≤ n  (trong bàn — chỉ số 1-based)
    2. 1 ≤ c2 ≤ n
    3. ban[r2-1][c2-1] == 0  (chưa thăm)

    Tham số
    -------
    r2, c2 : tọa độ đích (1-indexed)
    ban    : bảng n×n (list of list); ban[r-1][c-1] = bước thăm (0 nếu chưa)
    n      : kích thước bàn

    Trả về True nếu hợp lệ, False nếu không.
    """
    return 1 <= r2 <= n and 1 <= c2 <= n and ban[r2 - 1][c2 - 1] == 0


def thu_ma(ban: list, r: int, c: int, buoc: int, n: int,
           duong: list, da_tim: list, so_nut: list, so_rut: list) -> None:
    """
    Đệ quy quay lui tìm đường đi quân mã.

    Bất biến vào  : ban[r-1][c-1] == buoc; len(duong) == buoc
    Bất biến ra   : nếu da_tim[0]==True thì duong chứa đúng n² tọa độ hợp lệ
                    nếu da_tim[0]==False thì ban và duong được khôi phục

    Điều kiện dừng
    --------------
    - buoc == n² : đã thăm đủ mọi ô → đặt da_tim[0]=True, trả về
    - Hết nhánh  : rút lui (backtrack)

    Tham số
    -------
    ban    : bảng trạng thái (sửa tại chỗ)
    r, c   : tọa độ hiện tại (1-indexed)
    buoc   : bước thứ buoc vừa đặt tại (r,c)
    n      : kích thước bàn
    duong  : danh sách tọa độ tích lũy (sửa tại chỗ)
    da_tim : [bool] — cờ tìm thấy (dùng list để mô phỏng tham chiếu)
    so_nut : [int]  — đếm số nút gọi đệ quy (cho khảo sát)
    so_rut : [int]  — đếm số lần rút lui (cho khảo sát)
    """
    so_nut[0] += 1

    # Điều kiện dừng: đã thăm đủ n² ô
    if buoc == n * n:
        da_tim[0] = True
        return

    # Thử 8 nước đi theo thứ tự DR/DC
    for k in range(8):
        r2 = r + DR[k]
        c2 = c + DC[k]
        if nuoc_di_hop_le(r2, c2, ban, n):
            # Chọn ô (r2,c2): đánh số bước
            ban[r2 - 1][c2 - 1] = buoc + 1
            duong.append((r2, c2))

            # Đệ quy
            thu_ma(ban, r2, c2, buoc + 1, n, duong, da_tim, so_nut, so_rut)

            # Nếu tìm thấy, dừng ngay — không thử nhánh khác
            if da_tim[0]:
                return

            # Rút lui: hủy chọn ô (r2,c2)
            duong.pop()
            ban[r2 - 1][c2 - 1] = 0
            so_rut[0] += 1


def kiem_tra_duong(duong: list, n: int) -> tuple:
    """
    Kiểm nghiệm độc lập tính hợp lệ của đường đi quân mã.

    Kiểm tra theo thứ tự
    --------------------
    1. Số ô == n²
    2. Bắt đầu tại (1,1)
    3. Không có tọa độ lặp
    4. Mọi tọa độ trong [1,n]×[1,n]
    5. Mỗi cặp liên tiếp là nước đi quân mã: {|Δr|,|Δc|} = {1,2}

    Trả về
    ------
    (True,  "hop le")           nếu đường đi hợp lệ
    (False, "<lý do từ chối>")  nếu vi phạm

    Ví dụ
    -----
    >>> kiem_tra_duong([(1,1)], 1)
    (True, 'hop le')
    >>> kiem_tra_duong([(1,1),(2,2)], 2)
    (False, 'do dai sai: can 4, co 2')
    """
    N = n * n

    # Kiểm 1: độ dài
    if len(duong) != N:
        return (False, f"do dai sai: can {N}, co {len(duong)}")

    # Kiểm 2: bắt đầu tại (1,1)
    if duong[0] != (1, 1):
        return (False, f"khong bat dau tu (1,1); bat dau tu {duong[0]}")

    # Kiểm 3: không lặp
    if len(set(duong)) != N:
        return (False, "co toa do lap trong duong di")

    # Kiểm 4: tọa độ trong bàn
    for r, c in duong:
        if not (1 <= r <= n and 1 <= c <= n):
            return (False, f"toa do ngoai ban: ({r},{c}) voi n={n}")

    # Kiểm 5: nước đi quân mã
    for i in range(N - 1):
        r1, c1 = duong[i]
        r2, c2 = duong[i + 1]
        dr = abs(r2 - r1)
        dc = abs(c2 - c1)
        if not ((dr == 1 and dc == 2) or (dr == 2 and dc == 1)):
            return (
                False,
                f"nuoc di khong hop le tai buoc {i}->{i+1}: "
                f"({r1},{c1})->({r2},{c2}), |dr|={dr}, |dc|={dc}"
            )

    return (True, "hop le")


def giai_bai(n: int):
    """
    Hàm chính: tìm một đường đi của quân mã trên bàn n×n từ (1,1).

    Hợp đồng
    --------
    Input  : n — kích thước bàn cờ; 1 ≤ n ≤ 5 (int)
    Output :
      - list[(int,int)] gồm n² tọa độ theo thứ tự thăm, nếu tìm thấy
      - None, nếu không có đường đi
    Ném    : ValueError nếu n không hợp lệ (trước khi chạy thuật toán)

    Ví dụ
    -----
    >>> giai_bai(1)
    [(1, 1)]
    >>> giai_bai(3)
    (None — không có đường đi)
    >>> giai_bai(5)
    [(1,1), (2,3), ...]  # 25 tọa độ hợp lệ
    """
    # Bước 1: kiểm tra đầu vào (ném ValueError nếu sai)
    kiem_tra_dau_vao(n)

    # Bước 2: khởi tạo bảng và đường đi
    ban = [[0] * n for _ in range(n)]
    ban[0][0] = 1                        # bước 1 tại (1,1)
    duong = [(1, 1)]
    da_tim = [False]
    so_nut = [0]
    so_rut = [0]

    # Bước 3: đệ quy quay lui
    thu_ma(ban, 1, 1, 1, n, duong, da_tim, so_nut, so_rut)

    # Bước 4: trả kết quả
    if da_tim[0]:
        # Bước 5: kiểm nghiệm độc lập (bất biến hậu)
        ok, msg = kiem_tra_duong(duong, n)
        if not ok:
            raise RuntimeError(f"Loi noi tai: duong di tim duoc khong hop le — {msg}")
        return duong
    else:
        return None


def giai_bai_voi_thong_ke(n: int) -> tuple:
    """
    Phiên bản giai_bai trả thêm thống kê số nút và rút lui — dùng cho khảo sát Q1-Q3.

    Trả về
    ------
    (ket_qua, so_nut, so_rut)
    - ket_qua : list tọa độ hoặc None
    - so_nut  : số lần hàm thu_ma được gọi
    - so_rut  : số lần rút lui (ban[r][c] = 0)
    """
    kiem_tra_dau_vao(n)
    ban = [[0] * n for _ in range(n)]
    ban[0][0] = 1
    duong = [(1, 1)]
    da_tim = [False]
    so_nut = [0]
    so_rut = [0]
    thu_ma(ban, 1, 1, 1, n, duong, da_tim, so_nut, so_rut)
    ket_qua = duong if da_tim[0] else None
    return (ket_qua, so_nut[0], so_rut[0])


def in_ban_co(duong: list, n: int) -> None:
    """In bảng n×n đánh số bước thăm để nhìn rõ đường đi."""
    ban = [[0] * n for _ in range(n)]
    for i, (r, c) in enumerate(duong):
        ban[r - 1][c - 1] = i + 1
    print("   Bảng đánh số bước:")
    for row in ban:
        print("   " + "".join(f"{x:4}" for x in row))
