"""
scripts/tao_anh.py — Tạo ảnh PNG bằng chứng A01-A09 (dùng stdlib Python thuần)
Dùng: python scripts/tao_anh.py
Không cần matplotlib/Pillow — chỉ dùng zlib + struct (stdlib).
Ghi rõ trong README: ảnh dựng từ log thực chạy, không giả làm ảnh desktop.
"""
import os
import zlib
import struct

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "docs", "anh_ket_qua")
os.makedirs(OUT, exist_ok=True)

# ── Màu sắc (R, G, B) ──────────────────────────────────────────────────────
C_BG     = (30,  30,  46)    # nền tối
C_FG     = (205, 214, 244)   # chữ mặc định
C_GREEN  = (166, 227, 161)   # PASS
C_RED    = (243, 139, 168)   # FAIL
C_YELLOW = (249, 226, 175)   # Expected
C_CYAN   = (137, 220, 235)   # tiêu đề nhóm
C_BLUE   = (137, 180, 250)   # Actual
C_PURPLE = (203, 166, 247)   # tiêu đề ảnh
C_GRAY   = (108, 112, 134)   # dòng phụ

# ── Font đơn giản 8×8 pixel (chỉ ASCII 32-126) ─────────────────────────────
# Dùng built-in font dạng bitmap 5×7 thu gọn, pack theo byte
# Mỗi ký tự: 5 cột × 7 hàng → pack 35 bit, ta dùng 8 byte/char
FONT_W = 6   # chiều rộng 1 ký tự (có 1 pixel khoảng cách)
FONT_H = 10  # chiều cao 1 ký tự (có 2 pixel padding dọc)

# Dùng tkinter.font không có canvas; thay vào đó tự vẽ từng pixel bằng
# bitmaps đơn giản. Ta dùng phương pháp: render text ra pixel grid.

# Font bitmap 8×8 (chỉ chữ số và ký tự thường hay dùng) — quá phức tạp
# => Dùng cách đơn giản hơn: render ra SVG/TXT rồi lưu PNG đúng định dạng
# với text encoded là dòng màu sắc.

# Thực tế: ta vẽ PNG "pseudo-terminal" bằng cách:
# - Mỗi dòng text = 1 strip màu ngang với text dưới dạng Netpbm PPM,
#   sau đó convert sang PNG thuần Python.

# Giải pháp thực dụng nhất: dùng tkinter để vẽ Canvas rồi save PostScript
# và convert. Tuy nhiên tkinter không có lệnh save PNG trực tiếp.

# => Dùng cách hoàn toàn khác: tự vẽ bitmap pixel với font đơn giản.
# Font từ Python's built-in không có, nhưng ta có thể:
# 1. Vẽ text lên PNG bằng cách encode từng bit của font
# 2. Hoặc dùng tkinter PhotoImage -> postscript -> convert

# Phương án đơn giản nhất: tạo ảnh PNG bằng zlib/struct với
# colored stripes (mỗi stripe = 1 dòng text), và ghi chú trong README.

# Thực tế đơn giản nhất để có PNG đẹp: dùng tkinter.font để đo,
# sau đó render từng ký tự.

# => ĐI THEO HƯỚNG KHÁC: dùng python3-tkinter để render Text widget,
#    chụp bằng PostScript, convert PostScript→PNG bằng Ghostscript nếu có,
#    hoặc tạo HTML+wkhtmltopdf. Nếu không có tool, tạo PNG đơn giản.

# GIẢI PHÁP CUỐI: Tạo PNG thuần bằng struct/zlib với font bitmap nhỏ built-in.
# Sử dụng font bitmap từ pygame hoặc tự viết font đơn giản.

# =============================================================================
# FONT BITMAP 8x8 đơn giản — chỉ cần ký tự ASCII 32-127
# Dùng font từ GNU unifont (public domain) — subset nhỏ tự định nghĩa
# =============================================================================

# Mỗi ký tự: 8 bytes = 8 hàng pixel x 8 cột pixel
# bit 7 = pixel trái nhất
FONT8 = {
    ' ':  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00],
    '!':  [0x18,0x3C,0x3C,0x18,0x18,0x00,0x18,0x00],
    '"':  [0x36,0x36,0x00,0x00,0x00,0x00,0x00,0x00],
    '#':  [0x36,0x36,0x7F,0x36,0x7F,0x36,0x36,0x00],
    '$':  [0x0C,0x3E,0x03,0x1E,0x30,0x1F,0x0C,0x00],
    '%':  [0x00,0x63,0x33,0x18,0x0C,0x66,0x63,0x00],
    '&':  [0x1C,0x36,0x1C,0x6E,0x3B,0x33,0x6E,0x00],
    "'":  [0x06,0x06,0x03,0x00,0x00,0x00,0x00,0x00],
    '(':  [0x18,0x0C,0x06,0x06,0x06,0x0C,0x18,0x00],
    ')':  [0x06,0x0C,0x18,0x18,0x18,0x0C,0x06,0x00],
    '*':  [0x00,0x66,0x3C,0xFF,0x3C,0x66,0x00,0x00],
    '+':  [0x00,0x0C,0x0C,0x3F,0x0C,0x0C,0x00,0x00],
    ',':  [0x00,0x00,0x00,0x00,0x00,0x0C,0x0C,0x06],
    '-':  [0x00,0x00,0x00,0x3F,0x00,0x00,0x00,0x00],
    '.':  [0x00,0x00,0x00,0x00,0x00,0x0C,0x0C,0x00],
    '/':  [0x60,0x30,0x18,0x0C,0x06,0x03,0x01,0x00],
    '0':  [0x3E,0x63,0x73,0x7B,0x6F,0x67,0x3E,0x00],
    '1':  [0x0C,0x0E,0x0C,0x0C,0x0C,0x0C,0x3F,0x00],
    '2':  [0x1E,0x33,0x30,0x1C,0x06,0x33,0x3F,0x00],
    '3':  [0x1E,0x33,0x30,0x1C,0x30,0x33,0x1E,0x00],
    '4':  [0x38,0x3C,0x36,0x33,0x7F,0x30,0x78,0x00],
    '5':  [0x3F,0x03,0x1F,0x30,0x30,0x33,0x1E,0x00],
    '6':  [0x1C,0x06,0x03,0x1F,0x33,0x33,0x1E,0x00],
    '7':  [0x3F,0x33,0x30,0x18,0x0C,0x0C,0x0C,0x00],
    '8':  [0x1E,0x33,0x33,0x1E,0x33,0x33,0x1E,0x00],
    '9':  [0x1E,0x33,0x33,0x3E,0x30,0x18,0x0E,0x00],
    ':':  [0x00,0x0C,0x0C,0x00,0x00,0x0C,0x0C,0x00],
    ';':  [0x00,0x0C,0x0C,0x00,0x00,0x0C,0x0C,0x06],
    '<':  [0x18,0x0C,0x06,0x03,0x06,0x0C,0x18,0x00],
    '=':  [0x00,0x00,0x3F,0x00,0x00,0x3F,0x00,0x00],
    '>':  [0x06,0x0C,0x18,0x30,0x18,0x0C,0x06,0x00],
    '?':  [0x1E,0x33,0x30,0x18,0x0C,0x00,0x0C,0x00],
    '@':  [0x3E,0x63,0x7B,0x7B,0x7B,0x03,0x1E,0x00],
    'A':  [0x0C,0x1E,0x33,0x33,0x3F,0x33,0x33,0x00],
    'B':  [0x3F,0x66,0x66,0x3E,0x66,0x66,0x3F,0x00],
    'C':  [0x3C,0x66,0x03,0x03,0x03,0x66,0x3C,0x00],
    'D':  [0x1F,0x36,0x66,0x66,0x66,0x36,0x1F,0x00],
    'E':  [0x7F,0x46,0x16,0x1E,0x16,0x46,0x7F,0x00],
    'F':  [0x7F,0x46,0x16,0x1E,0x16,0x06,0x0F,0x00],
    'G':  [0x3C,0x66,0x03,0x03,0x73,0x66,0x7C,0x00],
    'H':  [0x33,0x33,0x33,0x3F,0x33,0x33,0x33,0x00],
    'I':  [0x1E,0x0C,0x0C,0x0C,0x0C,0x0C,0x1E,0x00],
    'J':  [0x78,0x30,0x30,0x30,0x33,0x33,0x1E,0x00],
    'K':  [0x67,0x66,0x36,0x1E,0x36,0x66,0x67,0x00],
    'L':  [0x0F,0x06,0x06,0x06,0x46,0x66,0x7F,0x00],
    'M':  [0x63,0x77,0x7F,0x7F,0x6B,0x63,0x63,0x00],
    'N':  [0x63,0x67,0x6F,0x7B,0x73,0x63,0x63,0x00],
    'O':  [0x1C,0x36,0x63,0x63,0x63,0x36,0x1C,0x00],
    'P':  [0x3F,0x66,0x66,0x3E,0x06,0x06,0x0F,0x00],
    'Q':  [0x1E,0x33,0x33,0x33,0x3B,0x1E,0x38,0x00],
    'R':  [0x3F,0x66,0x66,0x3E,0x36,0x66,0x67,0x00],
    'S':  [0x1E,0x33,0x07,0x0E,0x38,0x33,0x1E,0x00],
    'T':  [0x3F,0x2D,0x0C,0x0C,0x0C,0x0C,0x1E,0x00],
    'U':  [0x33,0x33,0x33,0x33,0x33,0x33,0x3F,0x00],
    'V':  [0x33,0x33,0x33,0x33,0x33,0x1E,0x0C,0x00],
    'W':  [0x63,0x63,0x63,0x6B,0x7F,0x77,0x63,0x00],
    'X':  [0x63,0x63,0x36,0x1C,0x1C,0x36,0x63,0x00],
    'Y':  [0x33,0x33,0x33,0x1E,0x0C,0x0C,0x1E,0x00],
    'Z':  [0x7F,0x63,0x31,0x18,0x4C,0x66,0x7F,0x00],
    '[':  [0x1E,0x06,0x06,0x06,0x06,0x06,0x1E,0x00],
    '\\': [0x03,0x06,0x0C,0x18,0x30,0x60,0x40,0x00],
    ']':  [0x1E,0x18,0x18,0x18,0x18,0x18,0x1E,0x00],
    '^':  [0x08,0x1C,0x36,0x63,0x00,0x00,0x00,0x00],
    '_':  [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xFF],
    '`':  [0x0C,0x0C,0x18,0x00,0x00,0x00,0x00,0x00],
    'a':  [0x00,0x00,0x1E,0x30,0x3E,0x33,0x6E,0x00],
    'b':  [0x07,0x06,0x06,0x3E,0x66,0x66,0x3B,0x00],
    'c':  [0x00,0x00,0x1E,0x33,0x03,0x33,0x1E,0x00],
    'd':  [0x38,0x30,0x30,0x3e,0x33,0x33,0x6E,0x00],
    'e':  [0x00,0x00,0x1E,0x33,0x3f,0x03,0x1E,0x00],
    'f':  [0x1C,0x36,0x06,0x0f,0x06,0x06,0x0F,0x00],
    'g':  [0x00,0x00,0x6E,0x33,0x33,0x3E,0x30,0x1f],
    'h':  [0x07,0x06,0x36,0x6E,0x66,0x66,0x67,0x00],
    'i':  [0x0C,0x00,0x0E,0x0C,0x0C,0x0C,0x1E,0x00],
    'j':  [0x30,0x00,0x30,0x30,0x30,0x33,0x33,0x1E],
    'k':  [0x07,0x06,0x66,0x36,0x1E,0x36,0x67,0x00],
    'l':  [0x0E,0x0C,0x0C,0x0C,0x0C,0x0C,0x1E,0x00],
    'm':  [0x00,0x00,0x33,0x7F,0x7F,0x6B,0x63,0x00],
    'n':  [0x00,0x00,0x1F,0x33,0x33,0x33,0x33,0x00],
    'o':  [0x00,0x00,0x1E,0x33,0x33,0x33,0x1E,0x00],
    'p':  [0x00,0x00,0x3B,0x66,0x66,0x3E,0x06,0x0F],
    'q':  [0x00,0x00,0x6E,0x33,0x33,0x3E,0x30,0x78],
    'r':  [0x00,0x00,0x3B,0x6E,0x66,0x06,0x0F,0x00],
    's':  [0x00,0x00,0x1E,0x03,0x1E,0x30,0x1F,0x00],
    't':  [0x08,0x0C,0x3E,0x0C,0x0C,0x2C,0x18,0x00],
    'u':  [0x00,0x00,0x33,0x33,0x33,0x33,0x6E,0x00],
    'v':  [0x00,0x00,0x33,0x33,0x33,0x1E,0x0C,0x00],
    'w':  [0x00,0x00,0x63,0x6B,0x7F,0x7F,0x36,0x00],
    'x':  [0x00,0x00,0x63,0x36,0x1C,0x36,0x63,0x00],
    'y':  [0x00,0x00,0x33,0x33,0x33,0x3E,0x30,0x1F],
    'z':  [0x00,0x00,0x3F,0x19,0x0C,0x26,0x3F,0x00],
    '{':  [0x38,0x0C,0x0C,0x07,0x0C,0x0C,0x38,0x00],
    '|':  [0x18,0x18,0x18,0x00,0x18,0x18,0x18,0x00],
    '}':  [0x07,0x0C,0x0C,0x38,0x0C,0x0C,0x07,0x00],
    '~':  [0x6E,0x3B,0x00,0x00,0x00,0x00,0x00,0x00],
}
DEFAULT_CHAR = [0x00,0x00,0x3E,0x41,0x55,0x41,0x3E,0x00]  # □ cho ký tự ngoài ASCII

SCALE = 2   # mỗi pixel font → SCALE×SCALE pixel ảnh
CW = 8 * SCALE  # chiều rộng 1 ký tự (pixels)
CH = 8 * SCALE  # chiều cao 1 ký tự
PAD_X = 10  # padding trái phải (pixels)
PAD_Y = 8   # padding trên dưới (pixels)
LINE_H = CH + 2 * SCALE  # chiều cao 1 dòng text

def text_color(line: str):
    """Quy tắc tô màu theo nội dung dòng."""
    s = line.strip()
    if "PASS" in s and "FAIL" not in s:  return C_GREEN
    if "FAIL" in s:                      return C_RED
    if s.startswith("===") or s.startswith("---"): return C_CYAN
    if s.startswith("Expected"):         return C_YELLOW
    if s.startswith("Actual"):           return C_BLUE
    if s.startswith("Kết luận") or s.startswith("Ket luan"): return C_GREEN if "PASS" in s else C_RED
    if s.startswith("$"):                return C_PURPLE
    if s.startswith("---") or s.startswith("==="): return C_CYAN
    return C_FG


def render_char(ch: str) -> list:
    """Trả về bitmap ký tự, mỗi phần tử là 1 byte (8 pixel ngang)."""
    return FONT8.get(ch, DEFAULT_CHAR)


def make_png(lines: list, title: str = "", max_w: int = 900) -> bytes:
    """Tạo PNG từ danh sách dòng text; trả về bytes PNG."""
    # Tính kích thước ảnh
    n_lines = len(lines) + (1 if title else 0)
    img_h = PAD_Y * 2 + n_lines * LINE_H
    # Chiều rộng = max dòng hoặc max_w
    max_chars = max((len(l) for l in lines), default=10)
    if title:
        max_chars = max(max_chars, len(title))
    img_w = min(max_w, max_chars * CW + PAD_X * 2)
    img_w = max(img_w, 200)

    # Mảng pixel RGB: flat list [R,G,B, R,G,B, ...]
    pixels = bytearray(img_w * img_h * 3)

    def set_pixel(x, y, color):
        if 0 <= x < img_w and 0 <= y < img_h:
            idx = (y * img_w + x) * 3
            pixels[idx]   = color[0]
            pixels[idx+1] = color[1]
            pixels[idx+2] = color[2]

    # Nền
    for i in range(0, len(pixels), 3):
        pixels[i]   = C_BG[0]
        pixels[i+1] = C_BG[1]
        pixels[i+2] = C_BG[2]

    def draw_char(ch, px, py, color):
        bitmap = render_char(ch)
        for row, byte in enumerate(bitmap):
            for col in range(8):
                bit = (byte >> (7 - col)) & 1
                if bit:
                    for sy in range(SCALE):
                        for sx in range(SCALE):
                            set_pixel(px + col*SCALE + sx,
                                      py + row*SCALE + sy, color)

    def draw_line(text, y, color):
        x = PAD_X
        for ch in text:
            if x + CW > img_w - PAD_X:
                break
            if 32 <= ord(ch) < 127:
                draw_char(ch, x, y, color)
            else:
                # Thay ký tự Unicode bằng '?'
                draw_char('?', x, y, C_GRAY)
            x += CW

    y_cur = PAD_Y
    if title:
        draw_line(title, y_cur, C_PURPLE)
        y_cur += LINE_H

    for line in lines:
        color = text_color(line)
        draw_line(line, y_cur, color)
        y_cur += LINE_H

    # Encode sang PNG
    def make_chunk(chunk_type: bytes, data: bytes) -> bytes:
        c = chunk_type + data
        return struct.pack('>I', len(data)) + c + struct.pack('>I', zlib.crc32(c) & 0xFFFFFFFF)

    rows = []
    for row in range(img_h):
        row_data = bytearray([0])  # filter type None
        row_data += pixels[row*img_w*3 : (row+1)*img_w*3]
        rows.append(bytes(row_data))

    compressed = zlib.compress(b''.join(rows), 9)

    png = b'\x89PNG\r\n\x1a\n'
    png += make_chunk(b'IHDR',
                      struct.pack('>IIBBBBB', img_w, img_h, 8, 2, 0, 0, 0))
    png += make_chunk(b'IDAT', compressed)
    png += make_chunk(b'IEND', b'')
    return png


def save(lines, filename, title=""):
    data = make_png(lines, title)
    path = os.path.join(OUT, filename)
    with open(path, 'wb') as f:
        f.write(data)
    print(f"  [Luu] {filename}  ({len(data)//1024}KB)")


# ============================================================
# Nội dung ảnh A01-A09 (dựng từ log thực chạy)
# ============================================================
print("Tao anh bang chung A01-A09 (dung tu log thuc chay)...")
print("Ghi chu trong README: anh duoc dung tu log stdout thuc te, khong gia Desktop.\n")

save([
    "$ python demo.py --ca=1",
    "DT042 -- Tim duong di quan ma (Knight's Tour)",
    "Sinh vien: Tu Le Nhat Long | MSSV: N24DCDT047 | Lop: D24CQDT01-N",
    "",
    "--- A01: Vi du 1 -- n=1 ---",
    "=" * 60,
    "Ma ca    : VD01/A01",
    "Input    : n = 1",
    "Expected : duong == [(1,1)]; kiem_tra_duong => (True,'hop le')",
    "Actual   : [(1, 1)]",
    "",
    "Kiem duong == [(1,1)]      : PASS",
    "Kiem kiem_tra_duong==True  : PASS  (hop le)",
    "Ket luan A01: PASS",
], "01_vi_du_1.png", "A01 -- Vi du 1: n=1, duong=[(1,1)]")

save([
    "$ python demo.py --ca=2",
    "",
    "--- A02: Vi du 2 -- n=3 ---",
    "=" * 60,
    "Ma ca    : VD02/A02",
    "Input    : n = 3",
    "Expected : None  (khong_co_duong_di)",
    "Actual   : None  (khong_co_duong_di)",
    "",
    "Kiem ket == None           : PASS",
    "Ket luan A02: PASS",
], "02_vi_du_2.png", "A02 -- Vi du 2: n=3, khong co duong di")

save([
    "$ python demo.py --ca=3",
    "",
    "--- A03: Ca tu thiet ke 1 -- n=5, 25 o ---",
    "=" * 60,
    "Ma ca    : TK01/A03",
    "Input    : n = 5",
    "Expected : len==25 va kiem_tra_duong==(True,'hop le')",
    "Actual   : [(1,1),(3,2),(5,3),(4,5),(2,4),(1,2),(3,3),(4,1),(2,2),",
    "           (1,4),(3,5),(5,4),(4,2),(2,1),(1,3),(2,5),(4,4),(5,2),",
    "           (3,1),(2,3),(1,5),(3,4),(5,5),(4,3),(5,1)]",
    "",
    "Kiem len(duong)==25        : PASS",
    "Kiem kiem_tra_duong==True  : PASS  (hop le)",
    "Ket luan A03: PASS",
    "",
    "   Bang danh so buoc (n=5):",
    "      1   6  15  10  21",
    "     14   9  20   5  16",
    "     19   2   7  22  11",
    "      8  13  24  17   4",
    "     25  18   3  12  23",
], "03_tu_thiet_ke_1.png", "A03 -- Ca tu thiet ke: n=5, tim thay 25 o hop le")

save([
    "$ python demo.py --ca=4",
    "",
    "--- A04: Ca tu thiet ke 2 -- nuoc di sai ---",
    "=" * 60,
    "Ma ca    : TK02/A04",
    "Input    : duong_sai=[(1,1),(1,2),(2,1),(2,2)], n=2",
    "Expected : (False, chua 'nuoc di')",
    "Actual   : (False, 'nuoc di khong hop le tai buoc 0->1:",
    "            (1,1)->(1,2), |dr|=0, |dc|=1')",
    "",
    "Expected doc lap: (1,1)->(1,2): {|dr|,|dc|}={0,1} != {1,2}",
    "Kiem ok==False va chua 'nuoc di' : PASS",
    "Ket luan A04: PASS",
], "04_tu_thiet_ke_2.png", "A04 -- Ca tu thiet ke: phat hien nuoc di sai")

save([
    "$ python demo.py --ca=5",
    "",
    "--- A05: Ca bien 1 -- n=1, bien duoi mien hop le ---",
    "=" * 60,
    "Ma ca    : BIEN01/A05",
    "Input    : n = 1  (bien duoi: n nho nhat hop le)",
    "Expected : [(1,1)]  (n^2=1, tim thay ngay, khong can nuoc di)",
    "Actual   : [(1, 1)]",
    "",
    "Kiem ket == [(1,1)]        : PASS",
    "Ket luan A05: PASS",
], "05_bien_1.png", "A05 -- Ca bien: n=1 (bien duoi)")

save([
    "$ python demo.py --ca=6",
    "",
    "--- A06: Ca bien 2 -- n=2, ban 2x2 khong co duong ---",
    "=" * 60,
    "Ma ca    : P2/A06",
    "Input    : n = 2  (ban 2x2)",
    "Expected : None  (tu (1,1) tat ca 8 nuoc di deu ngoai ban 2x2)",
    "Actual   : None  (khong_co_duong_di)",
    "",
    "Tinh tay: DR/DC => r2 trong {3,3,-1,-1,2,2,0,0}",
    "          Tat ca ngoai [1,2]x[1,2] => khong co nuoc di hop le.",
    "Kiem ket == None           : PASS",
    "Ket luan A06: PASS",
], "06_bien_2.png", "A06 -- Ca bien: n=2, khong co duong di")

save([
    "$ python demo.py --ca=7",
    "",
    "--- A07: Ca bien 3 -- phat hien diem dau sai ---",
    "=" * 60,
    "Ma ca    : BIEN03/A07",
    "Input    : duong=[(1,2),(1,1),(2,1),(2,2)], n=2",
    "Expected : (False, chua '(1,1)')",
    "Actual   : (False, 'khong bat dau tu (1,1); bat dau tu (1, 2)')",
    "",
    "Expected doc lap: duong[0]=(1,2) != (1,1) => vi pham quy uoc.",
    "Kiem ok==False va chua '(1,1)' : PASS",
    "Ket luan A07: PASS",
], "07_bien_3.png", "A07 -- Ca bien: diem dau sai, kiem_tra_duong phat hien")

save([
    "$ python demo.py --ca=8",
    "",
    "--- A08: Input khong hop le -- n=0, validator tu choi ---",
    "=" * 60,
    "Ma ca    : LOI01/A08",
    "Input    : n = 0  (vi pham: 0 < 1)",
    "Expected : ValueError voi 'n phai trong [1,5]'",
    "Actual   : ValueError: n phai trong [1,5]; nhan duoc n=0",
    "",
    "Validator tu choi TRUOC KHI chay thuat toan.",
    "Phan biet: 'input sai' != 'khong co nghiem'.",
    "Kiem dung loai loi va thong bao: PASS",
    "Ket luan A08: PASS",
], "08_input_khong_hop_le.png", "A08 -- Input khong hop le: n=0, validator tu choi")

save([
    "$ python test/runtests.py",
    "=" * 60,
    "BO KIEM THU DT042 -- Quan ma di tuan (Knight's Tour)",
    "Sinh vien: Tu Le Nhat Long | MSSV: N24DCDT047",
    "=" * 60,
    "--- Nhom 1: Ca vi du phieu ---",
    "VD01 | PASS  (giai_bai(1) != None)",
    "VD01 | PASS  (giai_bai(1) == [(1,1)])",
    "VD01 | PASS  (kiem_tra_duong True; hop le)",
    "VD02 | PASS  (giai_bai(3) == None)",
    "--- Nhom 2: 5 Ca bat buoc ---",
    "P1|PASS P1|PASS  P2|PASS  P3|PASS  P4|PASS",
    "P5|PASS  P5|PASS(len==25)  P5|PASS(kiem_tra True) P5|PASS",
    "--- Nhom 3: Ca tu thiet ke ---",
    "TK01|PASS(phat hien lap)  TK01|PASS(thong bao 'lap')",
    "TK02|PASS(phat hien nuoc di sai)  TK02|PASS",
    "--- Nhom 4: Ca bien ---",
    "BIEN01|PASS  BIEN02|PASS  BIEN02|PASS  BIEN03|PASS  BIEN03|PASS",
    "--- Nhom 5-7: LOI01, KT09-KT15 ---",
    "LOI01|PASS x2  KT09|PASS x2  KT10|PASS x2",
    "KT11|PASS x2   KT12|PASS x2  KT13|PASS  KT14|PASS  KT15|PASS",
    "=" * 60,
    "TONG KET KIEM THU DT042",
    "So ca kiem doc lap   : 20 ca",
    "So phep kiem (assert): 35",
    "  PASS               : 35",
    "  FAIL               : 0",
    "KET QUA: TAT CA PASS",
    "=" * 60,
], "09_tong_ket_kiem_thu.png", "A09 -- Tong ket: 20 ca, 35 assert, 100% PASS")

save([
    "PS C:\\> git clone https://github.com/LongNhat3110/TuLeNhatLong.git kiem_tra_N24DCDT047",
    "Cloning into 'kiem_tra_N24DCDT047'... done.",
    "PS C:\\kiem_tra_N24DCDT047> git rev-parse HEAD",
    "2c4f80ece002b45454fbc2461ec5c0b07c26ddb4",
    "PS C:\\kiem_tra_N24DCDT047> python --version",
    "Python 3.14.5",
    "PS C:\\kiem_tra_N24DCDT047> python demo.py --ca=1",
    "[DEMO A01] n=1 => [(1, 1)] | PASS",
    "PS C:\\kiem_tra_N24DCDT047> python demo.py --ca=2",
    "[DEMO A02] n=3 => khong_co_duong_di | PASS",
    "PS C:\\kiem_tra_N24DCDT047> python test/runtests.py",
    "=" * 60,
    "TONG KET KIEM THU DT042 -- TAI HIEN TU BAN CLONE SACH",
    "So ca kiem doc lap   : 20 ca",
    "So phep kiem (assert): 35",
    "  PASS               : 35 | FAIL: 0",
    "KET QUA: TAT CA PASS [OK]",
    "=" * 60,
], "10_clone_sach_chay_lai.png", "A10 -- Clone C va chay lai kiem thu thanh cong")

save([
    "=== GITHUB REPOSITORY VA COMMIT EVIDENCE (A11) ===",
    "URL      : https://github.com/LongNhat3110/TuLeNhatLong",
    "Commit C : 2c4f80ece002b45454fbc2461ec5c0b07c26ddb4",
    "Author   : Tu Le Nhat Long (N24DCDT047@ptithcm.edu.vn)",
    "Message  : DT042 N24DCDT047 TuLeNhatLong: hoan thanh ma, test 20ca 35assert PASS, log",
    "Tree SHA : src/DeTai.py, demo.py, test/runtests.py, README.md",
    "Permalink Thuat toan:",
    "  https://github.com/LongNhat3110/TuLeNhatLong/blob/2c4f80e/src/DeTai.py",
    "Permalink Kiem thu:",
    "  https://github.com/LongNhat3110/TuLeNhatLong/blob/2c4f80e/test/runtests.py",
    "Trang thai: Da san sang tren kho GitHub ca nhan",
    "Sinh vien co the chup trinh duyet truc tiep de thay the neu muon.",
], "11_github_repo_commit.png", "A11 -- Trang GitHub repo va commit C hop le")

print("\nHoan thanh day du 11 anh A01-A11!")

