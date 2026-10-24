"""
test/runtests.py — DT042: Tìm đường đi quân mã qua mọi ô
Sinh viên : Từ Lê Nhật Long | MSSV: N24DCDT047 | Lớp: D24CQDT01-N

Lệnh chạy : python test/runtests.py

Quy tắc
-------
- Expected của mọi ca tính độc lập (tính tay hoặc lý thuyết đã biết),
  KHÔNG lấy từ chính hàm đang test.
- Mỗi ca in: MA CA | PASS/FAIL
- Tổng kết in: số ca độc lập (so_ca) và số phép kiểm (so_assert) riêng.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from DeTai import giai_bai, kiem_tra_duong, kiem_tra_dau_vao

# ─── Bộ đếm ────────────────────────────────────────────────────────────────
so_ca = 0          # số ca kiểm độc lập (mỗi ID tính 1 ca)
so_pass = 0        # số phép kiểm PASS
so_fail = 0        # số phép kiểm FAIL
ca_da_dem = set()  # theo dõi ca đã tính vào so_ca (mỗi ID đếm 1 lần)


def kiem(ma_ca: str, dieu_kien: bool, mo_ta: str = "") -> bool:
    """Đăng ký 1 phép kiểm; in MA CA | PASS/FAIL."""
    global so_ca, so_pass, so_fail
    # Mỗi ID ca chỉ tính 1 lần vào so_ca
    if ma_ca not in ca_da_dem:
        ca_da_dem.add(ma_ca)
        so_ca += 1
    if dieu_kien:
        so_pass += 1
        print(f"{ma_ca} | PASS" + (f"  ({mo_ta})" if mo_ta else ""))
    else:
        so_fail += 1
        print(f"{ma_ca} | FAIL" + (f"  ({mo_ta})" if mo_ta else ""))
    return dieu_kien


SEP = "=" * 60

print(SEP)
print("BỘ KIỂM THỬ DT042 — Quân mã đi tuần (Knight's Tour)")
print("Sinh viên: Từ Lê Nhật Long | MSSV: N24DCDT047")
print("Mỗi dòng: MA CA | PASS/FAIL (lý do)")
print(SEP)
print()

# ===========================================================================
# NHÓM 1: Ca ví dụ phiếu (VD01, VD02)
# Expected tính tay/lý thuyết độc lập với hàm đang test
# ===========================================================================
print("--- Nhóm 1: Ca ví dụ phiếu ---")

# VD01: n=1 → [(1,1)]
# Expected độc lập: bàn 1×1, đặt bước 1 tại (1,1), buoc=1=n²=1 → tìm ngay
ket = giai_bai(1)
kiem("VD01", ket is not None,            "giai_bai(1) != None")
kiem("VD01", ket == [(1, 1)],            "giai_bai(1) == [(1,1)]")
if ket:
    ok, msg = kiem_tra_duong(ket, 1)
    kiem("VD01", ok is True,             f"kiem_tra_duong([(1,1)],1)==True; {msg}")

# VD02: n=3 → None
# Expected độc lập: lý thuyết + tính tay — bàn 3×3 không có open tour từ (1,1)
ket = giai_bai(3)
kiem("VD02", ket is None,               "giai_bai(3) == None (khong_co_duong_di)")

# ===========================================================================
# NHÓM 2: 5 Ca bắt buộc của phiếu (P1-P5)
# ===========================================================================
print("\n--- Nhóm 2: 5 Ca bắt buộc của phiếu ---")

# P1: n=1 — kiem_tra_duong phải chấp nhận [(1,1)]
# Expected độc lập: len=1=n², bắt đầu (1,1), không cặp liên tiếp → mọi điều kiện thỏa
ok, msg = kiem_tra_duong([(1, 1)], 1)
kiem("P1", ok is True,                  "kiem_tra_duong([(1,1)],1) ok==True")
kiem("P1", msg == "hop le",             "msg=='hop le'")

# P2: n=2 — không có đường
# Expected độc lập: tính tay — từ (1,1) trên bàn 2×2, 8 nước đi đều ngoài bàn
ket = giai_bai(2)
kiem("P2", ket is None,                 "giai_bai(2) == None")

# P3: n=3 — không có đường
# Expected độc lập: lý thuyết + tính tay
ket = giai_bai(3)
kiem("P3", ket is None,                 "giai_bai(3) == None")

# P4: n=4 — không có open tour từ (1,1)
# Expected độc lập: kết quả đã biết từ lý thuyết knight's tour 4×4
ket = giai_bai(4)
kiem("P4", ket is None,                 "giai_bai(4) == None")

# P5: n=5 — có đường đi 25 ô; không ép cùng thứ tự tọa độ
# Expected độc lập: lý thuyết đã biết + kiểm nghiệm bằng kiem_tra_duong (hàm độc lập)
ket = giai_bai(5)
kiem("P5", ket is not None,             "giai_bai(5) tim duoc duong")
if ket:
    kiem("P5", len(ket) == 25,          f"len(duong)==25; co {len(ket)} o")
    ok, msg = kiem_tra_duong(ket, 5)
    kiem("P5", ok is True,              f"kiem_tra_duong(duong,5)==True; {msg}")
    kiem("P5", ket[0] == (1, 1),        "bat dau tai (1,1)")

# ===========================================================================
# NHÓM 3: Ca tự thiết kế (TK01, TK02)
# ===========================================================================
print("\n--- Nhóm 3: Ca tự thiết kế ---")

# TK01: kiem_tra_duong phát hiện tọa độ lặp
# Input : 9 ô cho n=3 nhưng (1,1) xuất hiện 2 lần (ô thứ 1 và thứ 9)
# Expected độc lập: Set có 8 phần tử ≠ n²=9 → "co toa do lap"
duong_lap = [(1,1),(3,2),(1,3),(2,1),(3,3),(1,2),(3,1),(2,3),(1,1)]
ok, msg = kiem_tra_duong(duong_lap, 3)
kiem("TK01", ok is False,               "phat hien lap: ok==False")
kiem("TK01", "lap" in msg,              f"thong_bao co 'lap': '{msg}'")

# TK02: kiem_tra_duong phát hiện nước đi không hợp lệ
# Input : 4 ô cho n=2, unique, trong bàn — nhưng (1,1)→(1,2): {|Δr|,|Δc|}={0,1} ≠ {1,2}
# Expected độc lập: tính tay: dr=0, dc=1 → không phải knight move
duong_sai = [(1,1),(1,2),(2,1),(2,2)]
ok, msg = kiem_tra_duong(duong_sai, 2)
kiem("TK02", ok is False,               "phat hien nuoc di sai: ok==False")
kiem("TK02", "nuoc di" in msg,          f"thong_bao co 'nuoc di': '{msg}'")

# ===========================================================================
# NHÓM 4: Ca biên (BIEN01, BIEN02, BIEN03)
# ===========================================================================
print("\n--- Nhóm 4: Ca biên ---")

# BIEN01: n=1 — biên dưới miền hợp lệ
# Expected độc lập: n²=1, đặt bước 1 xong → tìm ngay; tính tay
ket = giai_bai(1)
kiem("BIEN01", ket == [(1, 1)],         "giai_bai(1)==[(1,1)] (bien duoi)")

# BIEN02: n=5 — biên trên miền hợp lệ
# Expected độc lập: len=25 và kiem_tra_duong=True
ket = giai_bai(5)
kiem("BIEN02", ket is not None and len(ket) == 25,
                                        "giai_bai(5) co 25 o (bien tren)")
if ket:
    ok, msg = kiem_tra_duong(ket, 5)
    kiem("BIEN02", ok is True,          f"kiem_tra_duong(giai_bai(5),5)==True; {msg}")

# BIEN03: kiem_tra_duong phát hiện điểm đầu sai
# Input : [(1,2),(1,1),(2,1),(2,2)] — bắt đầu từ (1,2) thay vì (1,1)
# Expected độc lập: duong[0]=(1,2) ≠ (1,1) → "khong bat dau tu (1,1)"
duong_sai_start = [(1,2),(1,1),(2,1),(2,2)]
ok, msg = kiem_tra_duong(duong_sai_start, 2)
kiem("BIEN03", ok is False,             "phat hien diem dau sai: ok==False")
kiem("BIEN03", "(1,1)" in msg,          f"thong_bao co '(1,1)': '{msg}'")

# ===========================================================================
# NHÓM 5: Input không hợp lệ — validator (LOI01)
# ===========================================================================
print("\n--- Nhóm 5: Input không hợp lệ ---")

# LOI01: n=0 — validator từ chối trước khi chạy thuật toán
# Expected độc lập: 0 < 1 → vi phạm miền [1,5]; throws ValueError
caught = False
msg_loi = ""
try:
    giai_bai(0)
except ValueError as e:
    caught = True
    msg_loi = str(e)
kiem("LOI01", caught,                   "validator bat loi ValueError khi n=0")
kiem("LOI01", "n phai trong [1,5]" in msg_loi,
                                        f"thong_bao dung: '{msg_loi}'")

# ===========================================================================
# NHÓM 6: Ca bổ sung (KT09-KT12)
# ===========================================================================
print("\n--- Nhóm 6: Ca bổ sung ---")

# KT09: n=6 — validator từ chối n > 5
caught = False; msg_loi = ""
try:
    giai_bai(6)
except ValueError as e:
    caught = True; msg_loi = str(e)
kiem("KT09", caught,                    "validator bat loi khi n=6")
kiem("KT09", "n phai trong [1,5]" in msg_loi,
                                        f"thong_bao dung: '{msg_loi}'")

# KT10: n=-1 — validator từ chối n âm
caught = False; msg_loi = ""
try:
    giai_bai(-1)
except ValueError as e:
    caught = True; msg_loi = str(e)
kiem("KT10", caught,                    "validator bat loi khi n=-1")
kiem("KT10", "n phai trong [1,5]" in msg_loi,
                                        f"thong_bao dung: '{msg_loi}'")

# KT11: kiem_tra_duong phát hiện độ dài sai
# Input : [(1,1)] — len=1 ≠ n²=4 với n=2
# Expected độc lập: 1 ≠ 4 → "do dai sai"
ok, msg = kiem_tra_duong([(1, 1)], 2)
kiem("KT11", ok is False,               "phat hien do dai sai: ok==False")
kiem("KT11", "do dai" in msg,           f"thong_bao co 'do dai': '{msg}'")

# KT12: kiem_tra_duong phát hiện tọa độ ngoài bàn
# Input : [(1,1),(3,2),(1,3),(2,1)] với n=2 — (3,2) có r=3>n=2
# Expected độc lập: 3 > 2 → "toa do ngoai ban"
ok, msg = kiem_tra_duong([(1,1),(3,2),(1,3),(2,1)], 2)
kiem("KT12", ok is False,               "phat hien toa do ngoai ban: ok==False")
kiem("KT12", "ngoai" in msg,            f"thong_bao co 'ngoai': '{msg}'")

# ===========================================================================
# NHÓM 7: Bất biến (KT13-KT15)
# ===========================================================================
print("\n--- Nhóm 7: Bất biến ---")

# KT13: giai_bai(5) luôn bắt đầu tại (1,1)
ket = giai_bai(5)
kiem("KT13", ket is not None and ket[0] == (1, 1),
                                        "bat_bien: giai_bai(5)[0]==(1,1)")

# KT14: mọi ô trong [1,5]×[1,5] với n=5
ket = giai_bai(5)
if ket:
    tap_hop_le = all(1 <= r <= 5 and 1 <= c <= 5 for r, c in ket)
    kiem("KT14", tap_hop_le,            "bat_bien: moi o thuoc [1,5]x[1,5]")

# KT15: giai_bai(1) không chứa tọa độ trùng
ket = giai_bai(1)
kiem("KT15", ket is not None and len(set(ket)) == 1,
                                        "bat_bien: Set(giai_bai(1))=={(1,1)}")

# ===========================================================================
# Tổng kết
# ===========================================================================
print()
print(SEP)
print("TỔNG KẾT KIỂM THỬ DT042")
total = so_pass + so_fail
print(f"Số ca kiểm độc lập   : {so_ca} ca")
print(f"Số phép kiểm (assert): {total}")
print(f"  PASS               : {so_pass}")
print(f"  FAIL               : {so_fail}")
if so_fail == 0:
    print("KẾT QUẢ: TẤT CẢ PASS ✓")
else:
    print(f"KẾT QUẢ: CÓ {so_fail} PHÉP KIỂM FAIL ✗")
print(SEP)
