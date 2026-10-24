"""
demo.py — DT042: Tìm đường đi quân mã qua mọi ô
Sinh viên : Từ Lê Nhật Long | MSSV: N24DCDT047 | Lớp: D24CQDT01-N

Cách chạy:
  python demo.py              # chạy tất cả ca A01-A08
  python demo.py --ca=1       # chỉ chạy ca A01
  python demo.py --nhap       # nhập n từ bàn phím
"""
import sys
import os

# Đảm bảo import được DeTai từ thư mục src/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from DeTai import (
    giai_bai, kiem_tra_duong, kiem_tra_dau_vao,
    in_ban_co, giai_bai_voi_thong_ke
)


SEP = "=" * 62


def in_ca(ma_ca, n_input, expected_mo_ta, actual, trung_gian=""):
    print(SEP)
    print(f"Mã ca       : {ma_ca}")
    print(f"Input       : n = {n_input}")
    print(f"Expected    : {expected_mo_ta}")
    if trung_gian:
        print(f"Trung gian  : {trung_gian}")
    if actual is None:
        actual_str = "None  (khong_co_duong_di)"
    else:
        actual_str = str(actual)
    print(f"Actual      : {actual_str}")
    print()


# ─────────────────────────────────────────────────────────────
# A01  Ví dụ 1: n=1 → [(1,1)]
# ─────────────────────────────────────────────────────────────
def demo_A01():
    print("\n--- A01: Ví dụ 1 — n=1 ---")
    n = 1
    in_ca("VD01/A01", n,
          "duong == [(1,1)] và kiem_tra_duong trả (True,'hop le')",
          giai_bai(n))
    ket = giai_bai(n)
    ok1 = ket == [(1, 1)]
    ok2, msg2 = kiem_tra_duong(ket, n) if ket else (False, "")
    print(f"Kiểm duong == [(1,1)]           : {'PASS' if ok1 else 'FAIL'}")
    print(f"Kiểm kiem_tra_duong == True     : {'PASS' if ok2 else 'FAIL'}  ({msg2})")
    print(f"Kết luận A01: {'PASS' if ok1 and ok2 else 'FAIL'}")


# ─────────────────────────────────────────────────────────────
# A02  Ví dụ 2: n=3 → None
# ─────────────────────────────────────────────────────────────
def demo_A02():
    print("\n--- A02: Ví dụ 2 — n=3 ---")
    n = 3
    ket = giai_bai(n)
    in_ca("VD02/A02", n, "None (khong_co_duong_di)", ket)
    ok = ket is None
    print(f"Kiểm ket == None                : {'PASS' if ok else 'FAIL'}")
    print(f"Kết luận A02: {'PASS' if ok else 'FAIL'}")


# ─────────────────────────────────────────────────────────────
# A03  Ca tự thiết kế 1: n=5, kiểm đủ 25 ô hợp lệ
# ─────────────────────────────────────────────────────────────
def demo_A03():
    print("\n--- A03: Ca tự thiết kế 1 — n=5, kiểm đủ 25 ô ---")
    n = 5
    ket = giai_bai(n)
    in_ca("TK01/A03", n,
          "len==25 và kiem_tra_duong==(True,'hop le')",
          ket)
    ok1 = ket is not None and len(ket) == 25
    ok2, msg2 = kiem_tra_duong(ket, n) if ket else (False, "")
    print(f"Kiểm len(duong) == 25           : {'PASS' if ok1 else 'FAIL'}")
    print(f"Kiểm kiem_tra_duong == True     : {'PASS' if ok2 else 'FAIL'}  ({msg2})")
    print(f"Kết luận A03: {'PASS' if ok1 and ok2 else 'FAIL'}")
    if ket:
        in_ban_co(ket, n)


# ─────────────────────────────────────────────────────────────
# A04  Ca tự thiết kế 2: kiem_tra_duong phát hiện nước đi sai
# ─────────────────────────────────────────────────────────────
def demo_A04():
    print("\n--- A04: Ca tự thiết kế 2 — kiem_tra_duong phát hiện nước đi sai ---")
    # (1,1)→(1,2): |Δr|=0, |Δc|=1 — không phải {1,2}
    duong_sai = [(1, 1), (1, 2), (2, 1), (2, 2)]
    n = 2
    ok, msg = kiem_tra_duong(duong_sai, n)
    print(SEP)
    print(f"Mã ca       : TK02/A04")
    print(f"Input       : duong_sai={duong_sai}, n={n}")
    print(f"Expected    : (False, chứa 'nuoc di')")
    print(f"Actual      : ({ok}, '{msg}')")
    print()
    ket_luan = not ok and "nuoc di" in msg
    print(f"Kiểm ok==False và chứa 'nuoc di': {'PASS' if ket_luan else 'FAIL'}")
    print(f"Kết luận A04: {'PASS' if ket_luan else 'FAIL'}")


# ─────────────────────────────────────────────────────────────
# A05  Ca biên 1: n=1 (biên dưới miền)
# ─────────────────────────────────────────────────────────────
def demo_A05():
    print("\n--- A05: Ca biên 1 — n=1, biên dưới miền hợp lệ ---")
    n = 1
    ket = giai_bai(n)
    in_ca("BIEN01/A05", n, "[(1,1)]", ket)
    ok = ket == [(1, 1)]
    print(f"Kiểm ket == [(1,1)]             : {'PASS' if ok else 'FAIL'}")
    print(f"Kết luận A05: {'PASS' if ok else 'FAIL'}")


# ─────────────────────────────────────────────────────────────
# A06  Ca biên 2: n=2 (bàn nhỏ nhất không có đường)
# ─────────────────────────────────────────────────────────────
def demo_A06():
    print("\n--- A06: Ca biên 2 — n=2, bàn 2×2 không có đường ---")
    n = 2
    ket = giai_bai(n)
    in_ca("P2/A06", n,
          "None  (từ (1,1) tất cả 8 nước đi đều ngoài bàn 2×2)",
          ket)
    ok = ket is None
    print(f"Kiểm ket == None                : {'PASS' if ok else 'FAIL'}")
    print(f"Kết luận A06: {'PASS' if ok else 'FAIL'}")


# ─────────────────────────────────────────────────────────────
# A07  Ca biên 3: kiem_tra_duong phát hiện điểm đầu sai
# ─────────────────────────────────────────────────────────────
def demo_A07():
    print("\n--- A07: Ca biên 3 — kiem_tra_duong phát hiện điểm đầu sai ---")
    duong_sai_start = [(1, 2), (1, 1), (2, 1), (2, 2)]
    n = 2
    ok, msg = kiem_tra_duong(duong_sai_start, n)
    print(SEP)
    print(f"Mã ca       : BIEN03/A07")
    print(f"Input       : duong={duong_sai_start}, n={n}")
    print(f"Expected    : (False, chứa '(1,1)')")
    print(f"Actual      : ({ok}, '{msg}')")
    print()
    ket_luan = not ok and "(1,1)" in msg
    print(f"Kiểm ok==False và chứa '(1,1)' : {'PASS' if ket_luan else 'FAIL'}")
    print(f"Kết luận A07: {'PASS' if ket_luan else 'FAIL'}")


# ─────────────────────────────────────────────────────────────
# A08  Input không hợp lệ: n=0, validator từ chối
# ─────────────────────────────────────────────────────────────
def demo_A08():
    print("\n--- A08: Input không hợp lệ — n=0, validator từ chối ---")
    n_xau = 0
    print(SEP)
    print(f"Mã ca       : LOI01/A08")
    print(f"Input       : n = {n_xau}")
    print(f"Expected    : ValueError với thông báo 'n phai trong [1,5]'")
    try:
        giai_bai(n_xau)
        print("Actual      : [KHÔNG ném lỗi — SAI]")
        print("Kết luận A08: FAIL")
    except ValueError as e:
        print(f"Actual      : ValueError: {e}")
        ok = "n phai trong [1,5]" in str(e)
        print(f"Kiểm đúng loại lỗi và thông báo: {'PASS' if ok else 'FAIL'}")
        print(f"Kết luận A08: {'PASS' if ok else 'FAIL'}")


# ─────────────────────────────────────────────────────────────
# Chế độ nhập từ bàn phím
# ─────────────────────────────────────────────────────────────
def demo_nhap_ban_phim():
    print(SEP)
    print("CHẾ ĐỘ NHẬP BÀN PHÍM — DT042 Quân mã đi tuần")
    print("Nhập n (1 ≤ n ≤ 5):")
    raw = input().strip()
    try:
        n = int(raw)
    except ValueError:
        print(f"Lỗi: '{raw}' không phải số nguyên")
        return
    try:
        ket = giai_bai(n)
        if ket is None:
            print(f"Kết quả: Không có đường đi (khong_co_duong_di) với n={n}")
        else:
            print(f"Kết quả: Tìm được đường đi gồm {len(ket)} ô")
            print(f"Danh sách tọa độ: {ket}")
            ok, msg = kiem_tra_duong(ket, n)
            print(f"Kiểm nghiệm độc lập: ({ok}, '{msg}')")
            in_ban_co(ket, n)
    except ValueError as e:
        print(f"Lỗi đầu vào: {e}")


# ─────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────
def main():
    print("DT042 — Tìm đường đi quân mã qua mọi ô (Knight's Tour)")
    print("Sinh viên: Từ Lê Nhật Long | MSSV: N24DCDT047 | Lớp: D24CQDT01-N")
    print("Lệnh: python demo.py [--ca=N] [--nhap]")
    print()

    args = sys.argv[1:]

    if "--nhap" in args:
        demo_nhap_ban_phim()
        return

    # Xác định ca cần chạy
    ca_can_chay = None
    for arg in args:
        if arg.startswith("--ca="):
            try:
                ca_can_chay = int(arg.split("=")[1])
            except ValueError:
                pass

    demos = [demo_A01, demo_A02, demo_A03, demo_A04,
             demo_A05, demo_A06, demo_A07, demo_A08]

    if ca_can_chay is not None:
        if 1 <= ca_can_chay <= 8:
            demos[ca_can_chay - 1]()
        else:
            print(f"Ca {ca_can_chay} không tồn tại (chỉ có A01-A08)")
    else:
        for demo in demos:
            demo()

    print()
    print(SEP)
    print("Hoàn tất demo. Chạy test: python test/runtests.py")


if __name__ == "__main__":
    main()
