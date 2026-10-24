"""
scripts/trace.py — Bảng truy vết tay cho DT042 (bàn n=2)
Sinh viên : Từ Lê Nhật Long | MSSV: N24DCDT047
Lệnh      : python scripts/trace.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from DeTai import DR, DC

SEP = "=" * 72


def thu_ma_trace(ban, r, c, buoc, n, duong, da_tim, nut_dem, do_sau=0):
    """Phiên bản thu_ma in từng bước — chỉ dùng cho trace."""
    pad = "  " * do_sau
    ban_str = [row[:] for row in ban]  # bản sao để in
    print(f"{pad}Gọi thu_ma(r={r}, c={c}, buoc={buoc})")
    print(f"{pad}  ban = {ban_str}")
    print(f"{pad}  duong = {list(duong)}")
    nut_dem[0] += 1

    if buoc == n * n:
        print(f"{pad}  → buoc={buoc} == n²={n*n}  ── TÌM THẤY!")
        da_tim[0] = True
        return

    co_nuoc_di = False
    for k in range(8):
        r2 = r + DR[k]
        c2 = c + DC[k]
        in_board = 1 <= r2 <= n and 1 <= c2 <= n
        chua_tham = in_board and ban[r2-1][c2-1] == 0
        if not in_board:
            ly_do = "ngoài bàn"
        elif not chua_tham:
            ly_do = "đã thăm"
        else:
            ly_do = "HỢP LỆ ✓"

        print(f"{pad}  k={k+1}: (r2={r2}, c2={c2})  → {ly_do}")

        if chua_tham:
            co_nuoc_di = True
            ban[r2-1][c2-1] = buoc + 1
            duong.append((r2, c2))
            print(f"{pad}  Chọn ({r2},{c2}): ban[{r2-1}][{c2-1}]={ban[r2-1][c2-1]}")

            thu_ma_trace(ban, r2, c2, buoc+1, n, duong, da_tim, nut_dem, do_sau+1)
            if da_tim[0]:
                return

            print(f"{pad}  Rút lui ({r2},{c2}): ban[{r2-1}][{c2-1}]→0, pop duong")
            duong.pop()
            ban[r2-1][c2-1] = 0

    if not co_nuoc_di:
        print(f"{pad}  → Không có nước đi hợp lệ ── quay lui")


def main():
    print(SEP)
    print("BẢNG TRUY VẾT TAY — DT042 Quân mã đi tuần, n=2")
    print("Lần vết chuyên biệt: bảng bước, tọa độ, dấu ô khi thử/rút")
    print(SEP)
    print()

    n = 2
    ban = [[0] * n for _ in range(n)]
    ban[0][0] = 1
    duong = [(1, 1)]
    da_tim = [False]
    nut_dem = [0]

    print(f"Khởi tạo: n={n}, n²={n*n}")
    print(f"  ban[0][0] = 1  (ô (1,1) đặt bước 1)")
    print(f"  duong = [(1,1)]")
    print(f"  da_tim = False")
    print()
    print("─" * 72)

    thu_ma_trace(ban, 1, 1, 1, n, duong, da_tim, nut_dem)

    print()
    print("─" * 72)
    print(f"Kết quả cuối: da_tim={da_tim[0]}, duong={list(duong)}")
    print(f"Số nút đệ quy gọi: {nut_dem[0]}")
    print()
    print(SEP)
    print("Nhận xét:")
    print("  Bàn 2×2 — từ (1,1) tất cả 8 nước đi đều ngoài bàn.")
    print("  Hàm thu_ma không chọn được ô tiếp theo → trả về ngay.")
    print("  Không tìm được đường đi quân mã trên bàn 2×2.")
    print(SEP)


if __name__ == "__main__":
    main()
