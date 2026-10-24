# KẾ HOẠCH — DT042 Tìm đường đi quân mã

## GIAI ĐOẠN 0 — Kiểm kê gói và nhận đề

- [x] Liệt kê toàn bộ gói (phát hiện thư mục lặp; dùng bản ngoài cùng)
- [x] Đọc PHIEN_BAN.txt
- [x] Đọc 00_HUONG_DAN_SINH_VIEN.html (mục DT042)
- [x] Đọc Khung_ma_nguon_ca_nhan.zip (giải nén → thư mục TuLeNhatLong)
- [x] Mở Danh_sach_va_de_giao/91_Phieu_giao_de_tai_INT13185_N03.docx, tìm N24DCDT047
- [x] Khớp: MSSV=N24DCDT047, Họ tên=Từ Lê Nhật Long, Lớp=D24CQDT01-N, Mã đề=DT042
- [x] Tạo docs/PHIEU_CA_NHAN.md (trích nguyên văn đầy đủ phiếu + rubric từ HTML)
- [x] Tạo docs/GHI_CHU_GIAO_TRINH.md (tóm tắt chương 3 / câu 27 / trang in 86, PDF 98)
- [x] Tạo docs/KE_HOACH.md (file này)

## GIAI ĐOẠN 1 — Đặc tả và làm tay

- [x] Viết hợp đồng input/output → docs/BANG_CA_KIEM.md
- [x] Giải tay Ví dụ 1 (n=1) và Ví dụ 2 (n=3)
- [x] Lập bảng truy vết tay cho n=2 (ca nhỏ phù hợp lần vết chuyên biệt)
- [x] Viết giả mã theo tên biến thực tế, nêu bất biến và điều kiện dừng
- [x] Dự đoán độ phức tạp thời gian/bộ nhớ
- [x] Thiết kế bảng >= 12 ca kiểm độc lập (thực tế 20 ca kiểm độc lập)

## GIAI ĐOẠN 2 — Dựng repo và cài đặt (Python 3.14)

- [x] src/DeTai.py: kiem_tra_dau_vao, nuoc_di_hop_le, thu_ma, kiem_tra_duong, giai_bai
- [x] demo.py: 8 ca A01-A08 + chế độ nhập bàn phím (--nhap)
- [x] test/runtests.py: 20 ca có ID, expected viết cứng, 35 assert PASS 100%
- [x] scripts/trace.py: in bảng truy vết
- [x] scripts/khao_sat.py: khảo sát Q1-Q3 (n=1,3,5)
- [x] README.md: điền đủ thông tin cá nhân, đề tài, hướng dẫn chạy
- [x] Chạy python demo.py, runtests.py, scripts — kiểm tra PASS 100%
- [x] Ghi log đầy đủ vào docs/logs/ (demo_all.txt, runtests_output.txt, trace_n2.txt, khao_sat_Q1Q2Q3.txt, clone_sach_chay_lai.txt)

## GIAI ĐOẠN 3 — 11 ảnh bằng chứng A01-A11

- [x] A01: Ví dụ 1 (n=1) -> 01_vi_du_1.png
- [x] A02: Ví dụ 2 (n=3) -> 02_vi_du_2.png
- [x] A03: Ca tự thiết kế 1 (ô lặp) -> 03_tu_thiet_ke_1.png
- [x] A04: Ca tự thiết kế 2 (nước sai) -> 04_tu_thiet_ke_2.png
- [x] A05: Ca biên 1 (n=1 biên dưới) -> 05_bien_1.png
- [x] A06: Ca biên 2 (n=2 bàn nhỏ vô nghiệm) -> 06_bien_2.png
- [x] A07: Ca biên 3 (điểm đầu sai) -> 07_bien_3.png
- [x] A08: Input không hợp lệ (n=0) -> 08_input_khong_hop_le.png
- [x] A09: Tổng kết kiểm thử 20 ca, 35 assert PASS -> 09_tong_ket_kiem_thu.png
- [x] A10: Clone C và chạy lại thành công -> 10_clone_sach_chay_lai.png
- [x] A11: Thông tin kho GitHub thật và commit C -> 11_github_repo_commit.png

## GIAI ĐOẠN 4 — Git, commit C và GitHub

- [x] git init, git add, commit C
- [x] Lấy SHA C đầy đủ (40 ký tự): 2c4f80ece002b45454fbc2461ec5c0b07c26ddb4
- [x] Hướng dẫn tạo repo GitHub: https://github.com/LongNhat3110/TuLeNhatLong
- [x] Tạo permalink tại C cho DeTai.py và runtests.py
- [x] Clone C sang thư mục mới `kiem_tra_N24DCDT047` và chạy lại đạt 100%

## GIAI ĐOẠN 5 — Báo cáo Word và PDF

- [x] Điền 02_Mau_bao_cao_de_tai_ca_nhan.docx → N24DCDT047_DT042_TuLeNhatLong_BaoCao.docx
- [x] Điền đủ 5 chương theo thứ tự mẫu, giữ rubric, chèn 11 ảnh A01-A11
- [x] Xuất PDF đồng bộ: N24DCDT047_DT042_TuLeNhatLong_BaoCao.pdf
- [x] Kiểm tra tài liệu, không còn ngoặc vuông hay hướng dẫn thừa

## GIAI ĐOẠN 6 — Đóng gói 4 tệp nộp

- [x] N24DCDT047_DT042_TuLeNhatLong_BaoCao.docx
- [x] N24DCDT047_DT042_TuLeNhatLong_BaoCao.pdf
- [x] N24DCDT047_DT042_TuLeNhatLong_MaNguon.zip
- [x] N24DCDT047_DT042_TuLeNhatLong_ThongTinNop.txt (điền sau khi chốt S)

## GIAI ĐOẠN 7 — Kiểm S và tự kiểm cuối

- [x] Chốt commit S, lấy SHA S
- [x] Clone S → chạy lại kiểm chứng
- [x] Giải nén ZIP → chạy lại một lần
- [x] Hoàn thành hướng dẫn bảo vệ 5-7 phút tại docs/CAU_HOI_BAO_VE.md
- [x] Báo cáo chi tiết công việc cho sinh viên
