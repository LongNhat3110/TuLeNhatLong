# CÂU HỎI VÀ HƯỚNG DẪN BẢO VỆ ĐỒ ÁN (5–7 PHÚT)
## Đề tài DT042: Tìm đường đi của quân mã qua mọi ô
**Sinh viên:** Từ Lê Nhật Long | **MSSV:** N24DCDT047 | **Lớp:** D24CQDT01-N  
**Môn học:** Cấu trúc dữ liệu và giải thuật (INT13185 - Nhóm 03)  
**Giảng viên:** Hồ Nhựt Minh  

---

### 1. Câu hỏi về cấu trúc dữ liệu và mô hình trạng thái
- **Câu hỏi:** Bàn cờ và đường đi được biểu diễn bằng cấu trúc dữ liệu gì trong mã nguồn?
- **Trả lời:**
  - Bàn cờ được biểu diễn bằng ma trận 2 chiều `ban[n][n]` (mảng các danh sách số nguyên). Giá trị `ban[r][c] = 0` nghĩa là ô chưa được thăm; `ban[r][c] = k` ($1 \le k \le n^2$) nghĩa là ô được thăm ở bước thứ $k$.
  - Danh sách đường đi `duong` là danh sách các bộ tọa độ `(r, c)` theo thứ tự bước đi từ $1$ đến $n^2$.
  - 8 độ lệch của quân mã được lưu trong hai hằng số mảng: `DR = [2, 2, -2, -2, 1, 1, -1, -1]` và `DC = [1, -1, 1, -1, 2, -2, 2, -2]`.

---

### 2. Câu hỏi về thuật toán và kỹ thuật quay lui
- **Câu hỏi:** Hàm `thu_ma` hoạt động như thế nào? Điều kiện dừng và cơ chế quay lui (backtracking) là gì?
- **Trả lời:**
  - **Điều kiện dừng (tìm thấy lời giải):** Khi `buoc == n * n`, đã thăm đủ $n^2$ ô trên bàn cờ. Đặt cờ `da_tim[0] = True` và kết thúc đệ quy.
  - **Thử nước đi:** Tại ô `(r, c)` ở bước `buoc`, duyệt qua 8 hướng $k = 0 \dots 7$. Tính tọa độ kế tiếp `(r2, c2) = (r + DR[k], c + DC[k])`.
  - **Kiểm tra hợp lệ:** Gọi `nuoc_di_hop_le(r2, c2, ban, n)` kiểm tra $1 \le r2, c2 \le n$ và `ban[r2-1][c2-1] == 0`.
  - **Ghi nhận & Đệ quy:** Nếu hợp lệ, gán `ban[r2-1][c2-1] = buoc + 1`, thêm `(r2, c2)` vào `duong`, gọi đệ quy `thu_ma(ban, r2, c2, buoc + 1, ...)`.
  - **Quay lui (Backtracking):** Nếu nhánh đó không dẫn tới lời giải (`da_tim[0]` vẫn là `False`), ta rút lui: xóa phần tử cuối khỏi `duong` (`duong.pop()`) và khôi phục trạng thái ô `ban[r2-1][c2-1] = 0`.

---

### 3. Câu hỏi về tính đúng và các bất biến (Invariants)
- **Câu hỏi:** Những bất biến nào được duy trì trong suốt quá trình chạy thuật toán?
- **Trả lời:**
  1. **Bất biến khởi đầu:** Bước 1 luôn bắt đầu tại `(1, 1)` với `ban[0][0] = 1` và `duong = [(1, 1)]`.
  2. **Bất biến duy trì:** Tại mọi bước $k$, độ dài của danh sách `duong` đúng bằng $k$; ma trận `ban` có đúng $k$ ô mang giá trị khác 0 ($1, 2, \dots, k$); mỗi cặp ô liên tiếp $(r_i, c_i)$ và $(r_{i+1}, c_{i+1})$ đều thỏa mãn $|\Delta r| \cdot |\Delta c| = 2$ (tức $\{|\Delta r|, |\Delta c|\} = \{1, 2\}$).
  3. **Bất biến kết thúc:** Nếu tìm thấy, `len(duong) == n * n`, chứa đúng $n^2$ ô phân biệt trong phạm vi $[1, n] \times [1, n]$. Hàm kiểm nghiệm độc lập `kiem_tra_duong(duong, n)` xác nhận toàn bộ các điều kiện này.

---

### 4. Câu hỏi về độ phức tạp thời gian và không gian bộ nhớ
- **Câu hỏi:** Độ phức tạp thuật toán là bao nhiêu?
- **Trả lời:**
  - **Thời gian:** Trong trường hợp xấu nhất, cây tìm kiếm có hệ số phân nhánh tối đa là 8, độ sâu tối đa $N = n^2$, nên độ phức tạp cận trên thô là $O(8^{n^2})$. Tuy nhiên, nhờ kiểm tra biên và ô đã thăm (cắt nhánh mạnh), không gian trạng thái thực tế nhỏ hơn rất nhiều.
  - **Bộ nhớ:** $O(n^2)$ cho ma trận bàn cờ $n \times n$, danh sách đường đi $n^2$ phần tử, và ngăn xếp đệ quy có độ sâu tối đa $n^2$.

---

### 5. Câu hỏi về các trường hợp vô nghiệm và phân biệt lỗi
- **Câu hỏi:** Tại sao với $n = 2, 3, 4$ thuật toán trả về `None` (không có đường đi)? Đó có phải lỗi chương trình không?
- **Trả lời:**
  - Đây **không phải lỗi chương trình**, mà là kết quả toán học chính xác ("bài toán hợp lệ nhưng không có nghiệm"):
    - Với $n = 2$: Từ `(1, 1)`, tất cả 8 nước đi của quân mã đều nhảy ra ngoài phạm vi bàn cờ $2 \times 2$.
    - Với $n = 3$: Ô trung tâm $(2, 2)$ trên bàn $3 \times 3$ bị cô lập (không quân mã nào từ ô khác có thể nhảy vào nó), do đó không thể duyệt qua mọi ô.
    - Với $n = 4$: Đã được chứng minh bằng lý thuyết đồ thị không tồn tại open knight's tour bắt đầu từ góc `(1, 1)`.
  - Chương trình phân biệt rõ:
    - Input sai ($n \le 0, n > 5$): Validator `kiem_tra_dau_vao` ném ngoại lệ `ValueError` từ chối ngay trước khi chạy.
    - Input hợp lệ nhưng vô nghiệm ($n = 2, 3, 4$): Thuật toán chạy vét cạn toàn bộ không gian trạng thái và trả về `None`.

---

### 6. Thao tác chạy demo và kiểm thử trực tiếp khi bảo vệ
- **Chạy ca ví dụ 1:**
  ```powershell
  python demo.py --ca=1
  ```
- **Chạy ca ví dụ 2:**
  ```powershell
  python demo.py --ca=2
  ```
- **Chạy bộ kiểm thử tự động 20 ca (35 assert):**
  ```powershell
  python test/runtests.py
  ```
- **Chế độ nhập từ bàn phím khi giảng viên yêu cầu:**
  ```powershell
  python demo.py --nhap
  ```
  Nhập $n = 1 \dots 5$ theo yêu cầu của thầy.
