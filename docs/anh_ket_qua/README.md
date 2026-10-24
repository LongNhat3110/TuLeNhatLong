# Kế hoạch 11 ảnh A01-A11 — DT042 N24DCDT047

Ảnh A01-A09 được dựng từ **log stdout thực chạy** (không phải ảnh chụp desktop).
Ghi rõ theo quy định: "anh duoc dung tu log thuc chay".

| Mã ảnh | Hình | Tên tệp | Mục tiêu |
|---|---|---|---|
| A01 | 4.1 | `01_vi_du_1.png` | Ví dụ 1: n=1, duong=[(1,1)] |
| A02 | 4.2 | `02_vi_du_2.png` | Ví dụ 2: n=3, None |
| A03 | 4.3 | `03_tu_thiet_ke_1.png` | Ca TK01: n=5, 25 ô, kiem_tra_duong=True |
| A04 | 4.4 | `04_tu_thiet_ke_2.png` | Ca TK02: kiem_tra_duong phát hiện nước đi sai |
| A05 | 4.5 | `05_bien_1.png` | Ca BIEN01: n=1 biên dưới |
| A06 | 4.6 | `06_bien_2.png` | Ca P2: n=2 không có đường |
| A07 | 4.7 | `07_bien_3.png` | Ca BIEN03: điểm đầu sai |
| A08 | 4.8 | `08_input_khong_hop_le.png` | Ca LOI01: n=0, validator từ chối |
| A09 | 4.9 | `09_tong_ket_kiem_thu.png` | Tổng kết: 20 ca, 35 assert, 100% PASS |
| A10 | 4.10 | `10_clone_sach_chay_lai.png` | Clone C + chạy lại (sinh viên tự chụp) |
| A11 | 4.11 | `11_github_repo_commit.png` | Trang GitHub thật (sinh viên tự chụp) |

## Hướng dẫn chụp A10

Sau khi push lên GitHub (commit C), chạy:
```powershell
git clone https://github.com/LongNhat3110/TuLeNhatLong.git kiem_tra_N24DCDT047
cd kiem_tra_N24DCDT047
git rev-parse HEAD
python --version
python demo.py
python test/runtests.py
```
Chụp toàn bộ terminal này lưu thành `10_clone_sach_chay_lai.png`.

## Hướng dẫn chụp A11

Mở trình duyệt, vào trang repo GitHub của bạn tại commit C:
`https://github.com/LongNhat3110/TuLeNhatLong/commit/<SHA_C>`
Chụp màn hình, lưu thành `11_github_repo_commit.png`.
