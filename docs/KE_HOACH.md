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
- [x] Thiết kế bảng >= 12 ca kiểm độc lập

## GIAI ĐOẠN 2 — Dựng repo và cài đặt

- [x] src/DeTai.jl: kiem_tra_dau_vao, nuoc_di_hop_le, thu_ma, kiem_tra_duong, giai_bai
- [x] demo.jl: 8 ca A01-A08 + chế độ nhập bàn phím
- [x] test/runtests.jl: >= 12 ca có ID, expected viết cứng, in tổng kết
- [x] scripts/trace.jl: in bảng truy vết
- [x] scripts/khao_sat.jl: khảo sát Q1-Q3 (n=1,3,5)
- [x] README.md: điền đủ thông tin
- [ ] Chạy julia --version, demo.jl, runtests.jl, scripts — kiểm tra PASS
- [ ] Ghi log vào docs/logs/

## GIAI ĐOẠN 3 — 11 ảnh bằng chứng A01-A11

- [ ] A01: Ví dụ 1 (n=1)
- [ ] A02: Ví dụ 2 (n=3)
- [ ] A03: Ca tự thiết kế 1
- [ ] A04: Ca tự thiết kế 2
- [ ] A05: Ca biên 1
- [ ] A06: Ca biên 2
- [ ] A07: Ca biên 3
- [ ] A08: Input không hợp lệ
- [ ] A09: Tổng kết kiểm thử >= 12 ca
- [ ] A10: Clone C và chạy lại (sau giai đoạn 4)
- [ ] A11: Tôi tự chụp trang GitHub thật

## GIAI ĐOẠN 4 — Git, commit C và GitHub

- [ ] git init, git add, commit C
- [ ] Lấy SHA C đầy đủ (40 ký tự)
- [ ] Hướng dẫn tạo repo GitHub (tôi tự làm)
- [ ] Tạo permalink tại C
- [ ] Clone C sang thư mục mới → A10

## GIAI ĐOẠN 5 — Báo cáo Word

- [ ] Copy 02_Mau_bao_cao_de_tai_ca_nhan.docx → N24DCDT047_DT042_TuLeNhatLong_BaoCao.docx
- [ ] Điền đủ 5 chương theo thứ tự mẫu
- [ ] Xuất PDF
- [ ] Kiểm từng trang PDF

## GIAI ĐOẠN 6 — Đóng gói 4 tệp nộp

- [ ] N24DCDT047_DT042_TuLeNhatLong_BaoCao.docx
- [ ] N24DCDT047_DT042_TuLeNhatLong_BaoCao.pdf
- [ ] N24DCDT047_DT042_TuLeNhatLong_MaNguon.zip
- [ ] N24DCDT047_DT042_TuLeNhatLong_ThongTinNop.txt (điền sau khi chốt S)

## GIAI ĐOẠN 7 — Kiểm S và tự kiểm cuối

- [ ] Chốt commit S, push, SHA S
- [ ] Clone S → chạy lại
- [ ] Giải nén ZIP → chạy lại
- [ ] Tick toàn bộ checklist
- [ ] Báo cáo cuối: việc đã làm / việc tôi tự làm
