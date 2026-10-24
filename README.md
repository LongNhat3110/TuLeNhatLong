# DT042 — Tìm đường đi của quân mã qua mọi ô

## Thông tin và căn cứ

| Trường | Giá trị |
|---|---|
| Họ tên | Từ Lê Nhật Long |
| MSSV | N24DCDT047 |
| Lớp | D24CQDT01-N |
| Mã đề | DT042 |
| Tên đề | Tìm đường đi của quân mã qua mọi ô |
| Môn học | INT13185 — Cấu trúc dữ liệu và giải thuật, Nhóm 03 |
| Giảng viên | Hồ Nhựt Minh |
| Giáo trình | Giao-trinh-Cau-truc-du-lieu-va-Giai-thuat-INT1306.pdf |
| Căn cứ | Chương 3, Bài tập câu 27 — Bài toán mã đi tuần; trang in 86; trang PDF 98 |
| Ngôn ngữ | Python 3 |
| Phiên bản | Python 3.14.5 |
| GitHub | [ĐIỀN sau khi push — LongNhat3110/TuLeNhatLong] |
| SHA C | ghi trong docs/logs và báo cáo |

## Hợp đồng input/output

| Tham số | Kiểu | Ràng buộc |
|---|---|---|
| n | int | 1 ≤ n ≤ 5, điểm đầu cố định (1,1) |

- **Kết quả tìm được:** `list[(int,int)]` — n² tọa độ theo thứ tự thăm
- **Không tìm được:** `None` (bài toán hợp lệ nhưng không có nghiệm)
- **Validator từ chối:** `ValueError` khi n < 1 hoặc n > 5 hoặc không phải int

## Lệnh chạy

```powershell
python --version

# Ví dụ 1 (n=1)
python demo.py --ca=1

# Ví dụ 2 (n=3)
python demo.py --ca=2

# Chạy tất cả ca demo A01-A08
python demo.py

# Nhập dữ liệu từ bàn phím
python demo.py --nhap

# Bộ kiểm thử (20 ca, 35 assert)
python test/runtests.py

# Bảng truy vết tay (n=2)
python scripts/trace.py

# Khảo sát Q1-Q3 (n=1,3,5)
python scripts/khao_sat.py
```

## Kết quả kiểm thử (thực chạy)

```
Số ca kiểm độc lập   : 20 ca
Số phép kiểm (assert): 35
  PASS               : 35
  FAIL               : 0
KẾT QUẢ: TẤT CẢ PASS ✓
```

## Cấu trúc thư mục

```
TuLeNhatLong/
├── .gitignore
├── README.md
├── demo.py                    # Demo A01-A08 + nhập bàn phím
├── src/
│   └── DeTai.py               # Module chính: kiem_tra_dau_vao, nuoc_di_hop_le,
│                              #   thu_ma, kiem_tra_duong, giai_bai
├── test/
│   └── runtests.py            # 20 ca kiểm độc lập, 35 assert, 100% PASS
├── scripts/
│   ├── trace.py               # Bảng truy vết tay (n=2)
│   └── khao_sat.py            # Khảo sát Q1/Q2/Q3 (n=1,3,5)
└── docs/
    ├── PHIEU_CA_NHAN.md        # Phiếu cá nhân đầy đủ (DT042)
    ├── GHI_CHU_GIAO_TRINH.md  # Tóm tắt lý thuyết chương 3 / câu 27
    ├── KE_HOACH.md             # Checklist 7 giai đoạn
    ├── BANG_CA_KIEM.md         # Bảng 20 ca kiểm (ID, input, expected, cách tính)
    ├── anh_ket_qua/            # 11 ảnh bằng chứng A01-A11
    │   └── README.md
    └── logs/                  # Log thực chạy (demo, runtests, trace, khao_sat)
```

## Clone và chạy lại

```powershell
git clone https://github.com/LongNhat3110/TuLeNhatLong.git kiem_tra_N24DCDT047
cd kiem_tra_N24DCDT047
git rev-parse HEAD
python --version
python demo.py
python test/runtests.py
```

## Quy ước nộp

4 tệp nộp trên Classroom:
- `N24DCDT047_DT042_TuLeNhatLong_BaoCao.docx`
- `N24DCDT047_DT042_TuLeNhatLong_BaoCao.pdf`
- `N24DCDT047_DT042_TuLeNhatLong_MaNguon.zip`
- `N24DCDT047_DT042_TuLeNhatLong_ThongTinNop.txt` (nộp rời, điền sau khi chốt S)
