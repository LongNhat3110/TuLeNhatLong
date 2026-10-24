"""
scripts/khao_sat.py — Khảo sát ba quy mô Q1, Q2, Q3 cho DT042
Q1: n=1 | Q2: n=3 | Q3: n=5
Phép đo: đếm nút đệ quy (so_nut) và số lần rút lui (so_rut)
Lệnh   : python scripts/khao_sat.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from DeTai import giai_bai_voi_thong_ke

SEP = "=" * 72


def main():
    print(SEP)
    print("KHẢO SÁT BA QUY MÔ — DT042 Quân mã đi tuần")
    print("Phép đo: đếm nút đệ quy và số lần rút lui (tách chi phí in)")
    print("Ba quy mô trong miền phiếu [1,5]: Q1=n=1, Q2=n=3, Q3=n=5")
    print(SEP)
    print()

    quy_mo = [(1, "Q1"), (3, "Q2"), (5, "Q3")]

    # Tiêu đề bảng
    print(f"{'Quy mô':<8} {'n':<4} {'N=n²':<6} {'Kết quả':<22} {'Nút gọi':>10} {'Rút lui':>10}")
    print("-" * 65)

    for n, ten in quy_mo:
        ket_qua, so_nut, so_rut = giai_bai_voi_thong_ke(n)
        if ket_qua is None:
            ket_str = "khong_co_duong_di"
        else:
            ket_str = f"tim_thay ({n*n} o)"
        print(f"{ten:<8} {n:<4} {n*n:<6} {ket_str:<22} {so_nut:>10} {so_rut:>10}")

    print()
    print("Ghi chú:")
    print("  'Nút gọi' = số lần hàm thu_ma được gọi đệ quy (kể cả nút lá).")
    print("  'Rút lui' = số lần hủy chọn một ô (ban[r][c] = 0).")
    print("  Miền phiếu cố định n ≤ 5 nên không vẽ đường cong tăng chắc chắn.")
    print("  n=2,4 không có nghiệm → số nút thường lớn hơn n=1,3,5.")
    print("  Không kết luận thuật toán nhanh cho bàn lớn từ các bàn n≤5.")
    print(SEP)


if __name__ == "__main__":
    main()
