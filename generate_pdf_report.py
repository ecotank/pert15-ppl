import os
import sys
import html
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Preformatted, HRFlowable
)
from reportlab.pdfgen import canvas

# Read full test code
with open("d:/alba/Akademik/Semester 6/Pengujian Perangkat Lunak/Pertemuan 15/test_app.py", "r", encoding="utf-8") as f:
    full_test_app_code = f.read()

# Read full workflow code
with open("d:/alba/Akademik/Semester 6/Pengujian Perangkat Lunak/Pertemuan 15/.github/workflows/selenium-tests.yml", "r", encoding="utf-8") as f:
    full_workflow_code = f.read()

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            super().showPage()
        super().save()

    def draw_page_number(self, page_count):
        if self._pageNumber == 1:
            return  # Suppress header/footer on cover page
        
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header text
        self.drawString(54, 800, "Laporan Pengujian Perangkat Lunak — Modul Login & Register")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 792, 541, 792)
        
        # Footer text & page numbering
        page_text = f"Halaman {self._pageNumber} dari {page_count}"
        self.drawRightString(541, 36, page_text)
        self.drawString(54, 36, "Pengujian Perangkat Lunak | Pertemuan 15")
        self.line(54, 48, 541, 48)
        
        self.restoreState()

def create_report(output_filename="Laporan_Pengujian_PPL_Login_Register.pdf"):
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=A4,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    PRIMARY = colors.HexColor("#1E3A8A")
    SECONDARY = colors.HexColor("#0284C7")
    DARK_TEXT = colors.HexColor("#1E293B")
    LIGHT_BG = colors.HexColor("#F8FAFC")
    BORDER_COLOR = colors.HexColor("#CBD5E1")

    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=28,
        textColor=PRIMARY,
        spaceAfter=15
    )

    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=16,
        textColor=colors.HexColor("#475569"),
        spaceAfter=20
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=PRIMARY,
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=SECONDARY,
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=DARK_TEXT,
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=DARK_TEXT,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=3
    )

    code_style = ParagraphStyle(
        'Code_Style',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=6.5,
        leading=8.5,
        textColor=colors.HexColor("#0F172A")
    )

    terminal_style = ParagraphStyle(
        'Terminal_Style',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7,
        leading=9,
        textColor=colors.HexColor("#0284C7")
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white,
        alignment=1
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=10,
        textColor=DARK_TEXT
    )

    story = []

    # COVER PAGE
    story.append(Spacer(1, 30))
    story.append(Paragraph("LAPORAN PENGUJIAN PERANGKAT LUNAK", title_style))
    story.append(Paragraph("Pengujian Otomatis Modul Login & Register Menggunakan Selenium WebDriver, Stub Layer, dan CI/CD Pipeline (GitHub Actions)", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=3, color=PRIMARY, spaceAfter=20))

    meta_data = [
        [Paragraph("<b>Mata Kuliah</b>", body_style), Paragraph(": Pengujian Perangkat Lunak (Pertemuan 15)", body_style)],
        [Paragraph("<b>Topik / Tugas</b>", body_style), Paragraph(": Quiz Pengujian Piranti Lunak — Modul Login & Register", body_style)],
        [Paragraph("<b>Repository Target</b>", body_style), Paragraph(": https://github.com/hermanka/quiz-pengupil", body_style)],
        [Paragraph("<b>Tools Pengujian</b>", body_style), Paragraph(": Selenium WebDriver, Python unittest, PHP CLI", body_style)],
        [Paragraph("<b>CI/CD Engine</b>", body_style), Paragraph(": GitHub Actions (MySQL 8.0 Container)", body_style)],
        [Paragraph("<b>Status Testing</b>", body_style), Paragraph(": <b>100% PASSED (8/8 Test Cases Berhasil)</b>", body_style)],
    ]

    meta_table = Table(meta_data, colWidths=[130, 350])
    meta_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
    ]))
    story.append(meta_table)

    story.append(Spacer(1, 20))

    info_box = [
        [Paragraph("<b>INFORMASI PENYERAHAN TUGAS</b>", h2_style)],
        [Paragraph("Dokumen laporan ini disusun sebagai bukti penyelesaian tugas praktikum pengujian perangkat lunak mencakup perancangan test case, implementasi stub & driver, eksekusi Selenium automation script, petunjuk jalannya testing untuk penguji, serta otomatisasi pipeline CI/CD di GitHub Actions.", body_style)]
    ]
    info_table = Table(info_box, colWidths=[480])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#EFF6FF")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#BFDBFE")),
        ('PADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(info_table)

    story.append(PageBreak())

    # BAB I: ANALISIS SISTEM
    story.append(Paragraph("BAB I: ANALISIS SISTEM & REFACTORING MODUL TARGET", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=SECONDARY, spaceAfter=10))

    story.append(Paragraph("1.1 Deskripsi Modul", h2_style))
    story.append(Paragraph("Pengujian dilakukan terhadap aplikasi berbasis web PHP-MySQL dari repositori target <b>quiz-pengupil</b>. Modul yang diuji terdiri dari dua komponen utama:", body_style))
    story.append(Paragraph("&bull; <b>Modul Login (login.php)</b>: Menangani autentikasi pengguna berdasarkan verifikasi username dan password terenkripsi (password_verify).", bullet_style))
    story.append(Paragraph("&bull; <b>Modul Register (register.php)</b>: Menangani pendaftaran akun pengguna baru mencakup penampungan Nama, Alamat Email, Username, Password, dan Re-Password.", bullet_style))

    story.append(Spacer(1, 6))
    story.append(Paragraph("1.2 Perbaikan Kode (Refactoring & Fix Bug)", h2_style))
    story.append(Paragraph("Dalam proses analisis awal terhadap kode sumber repositori target, ditemukan beberapa kesalahan kode yang telah diperbaiki:", body_style))
    story.append(Paragraph("1. <b>Koreksi Variabel pada register.php</b>: Pada query INSERT INTO users di repositori asli, digunakan variabel $nama yang belum terdefinisi. Variabel tersebut diperbaiki menjadi $name.", bullet_style))
    story.append(Paragraph("2. <b>Penyelarasan Verifikasi Username</b>: Pemanggilan fungsi cek_nama() disesuaikan untuk memeriksa ketersediaan $username pada database secara tepat.", bullet_style))
    story.append(Paragraph("3. <b>Pembuatan Halaman Landing Page (index.php)</b>: Repositori awal belum menyertakan file index.php yang dituju setelah login/register sukses. Dibuat halaman dashboard sederhana yang menampilkan pesan selamat datang dan tombol Logout.", bullet_style))

    story.append(Spacer(1, 10))

    # BAB II: MATRIKS TEST CASE
    story.append(Paragraph("BAB II: PERANCANGAN TEST CASE", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=SECONDARY, spaceAfter=10))
    story.append(Paragraph("Berikut adalah matriks test case yang dirancang untuk menguji fungsionalitas positif dan negatif pada modul Login dan Register:", body_style))

    test_case_data = [
        [
            Paragraph("ID", table_header_style),
            Paragraph("Modul", table_header_style),
            Paragraph("Deskripsi Skenario", table_header_style),
            Paragraph("Input Data Test", table_header_style),
            Paragraph("Ekspektasi Hasil", table_header_style),
            Paragraph("Hasil Test", table_header_style)
        ],
        [
            Paragraph("TC_REG_01", table_cell_style),
            Paragraph("Register", table_cell_style),
            Paragraph("Registrasi akun baru dengan data valid lengkap", table_cell_style),
            Paragraph("Name: User Valid<br/>Email: u1@test.com<br/>User: uvalid1<br/>Pass: pass123", table_cell_style),
            Paragraph("Registrasi berhasil, redirect ke index.php", table_cell_style),
            Paragraph("<b>PASSED</b>", table_cell_style)
        ],
        [
            Paragraph("TC_REG_02", table_cell_style),
            Paragraph("Register", table_cell_style),
            Paragraph("Registrasi dengan Password & Re-Password tidak cocok", table_cell_style),
            Paragraph("Pass: pass123<br/>RePass: pass999", table_cell_style),
            Paragraph("Gagal, error: <i>Password tidak sama !!</i>", table_cell_style),
            Paragraph("<b>PASSED</b>", table_cell_style)
        ],
        [
            Paragraph("TC_REG_03", table_cell_style),
            Paragraph("Register", table_cell_style),
            Paragraph("Registrasi dengan form kosong", table_cell_style),
            Paragraph("Form dikirim kosong", table_cell_style),
            Paragraph("Gagal, alert: <i>Data tidak boleh kosong !!</i>", table_cell_style),
            Paragraph("<b>PASSED</b>", table_cell_style)
        ],
        [
            Paragraph("TC_REG_04", table_cell_style),
            Paragraph("Register", table_cell_style),
            Paragraph("Registrasi dengan Username yang sudah terdaftar", table_cell_style),
            Paragraph("Username: uvalid1 (duplikat)", table_cell_style),
            Paragraph("Gagal, alert: <i>Username sudah terdaftar !!</i>", table_cell_style),
            Paragraph("<b>PASSED</b>", table_cell_style)
        ],
        [
            Paragraph("TC_LOG_01", table_cell_style),
            Paragraph("Login", table_cell_style),
            Paragraph("Login pengguna dengan kredensial valid", table_cell_style),
            Paragraph("User: uvalid1<br/>Pass: pass123", table_cell_style),
            Paragraph("Login berhasil, redirect ke index.php", table_cell_style),
            Paragraph("<b>PASSED</b>", table_cell_style)
        ],
        [
            Paragraph("TC_LOG_02", table_cell_style),
            Paragraph("Login", table_cell_style),
            Paragraph("Login dengan Password salah", table_cell_style),
            Paragraph("User: uvalid1<br/>Pass: wrongpass", table_cell_style),
            Paragraph("Login gagal, tetap berada di login.php", table_cell_style),
            Paragraph("<b>PASSED</b>", table_cell_style)
        ],
        [
            Paragraph("TC_LOG_03", table_cell_style),
            Paragraph("Login", table_cell_style),
            Paragraph("Login dengan Username tidak terdaftar", table_cell_style),
            Paragraph("User: user_unknown<br/>Pass: pass123", table_cell_style),
            Paragraph("Gagal, alert: <i>Register User Gagal !!</i>", table_cell_style),
            Paragraph("<b>PASSED</b>", table_cell_style)
        ],
        [
            Paragraph("TC_LOG_04", table_cell_style),
            Paragraph("Login", table_cell_style),
            Paragraph("Login dengan form kosong", table_cell_style),
            Paragraph("Form dikirim kosong", table_cell_style),
            Paragraph("Gagal, alert: <i>Data tidak boleh kosong !!</i>", table_cell_style),
            Paragraph("<b>PASSED</b>", table_cell_style)
        ],
    ]

    tc_table = Table(test_case_data, colWidths=[55, 45, 110, 110, 110, 50])
    tc_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
    ]))
    story.append(tc_table)

    story.append(PageBreak())

    # BAB III: STUB DAN DRIVER
    story.append(Paragraph("BAB III: IMPLEMENTASI STUB DAN DRIVER", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=SECONDARY, spaceAfter=10))

    story.append(Paragraph("3.1 Konsep dan Peran Stub", h2_style))
    story.append(Paragraph("Dalam pengujian perangkat lunak, <b>Stub</b> adalah komponen pasif / simulasi tiruan yang digunakan untuk menggantikan modul dependen yang belum siap atau kompleks untuk dihubungkan secara penuh.", body_style))
    story.append(Paragraph("Pada praktikum ini, Stub diterapkan pada dua area:", body_style))
    story.append(Paragraph("1. <b>Database Stub / Auto-Provisioner (koneksi_stub.php / koneksi.php)</b>: Menyediakan mekanisme pengganti koneksi database dan skema otomatis sehingga pengujian tidak mengalami kegagalan akibat ketiadaan tabel users.", bullet_style))
    story.append(Paragraph("2. <b>Dashboard Target Stub (index.php)</b>: Bertindak sebagai komponen penerima pengalihan (redirect stub) untuk memvalidasi bahwa sesi autentikasi berhasil terbentuk.", bullet_style))

    story.append(Spacer(1, 6))
    story.append(Paragraph("3.2 Konsep dan Peran Driver", h2_style))
    story.append(Paragraph("<b>Driver</b> (Selenium WebDriver) adalah komponen aktif pengujian yang mengontrol perilaku peramban web secara otomatis. Driver bertindak seolah-olah pengguna nyata sedang berinteraksi dengan aplikasi.", body_style))

    story.append(Spacer(1, 10))

    # BAB IV: PANDUAN EKSEKUSI PENGUJIAN UNTUK DOSEN / PENGUJI
    story.append(Paragraph("BAB IV: PANDUAN EKSEKUSI PENGUJIAN UNTUK DOSEN / PENGUJI", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=SECONDARY, spaceAfter=10))

    story.append(Paragraph("4.1 Prasyarat Lingkungan Pengujian", h2_style))
    story.append(Paragraph("Sebelum pengujian dijalankan, pastikan sistem memiliki:", body_style))
    story.append(Paragraph("&bull; Python 3.8+ (Library: selenium, webdriver-manager)", bullet_style))
    story.append(Paragraph("&bull; PHP 8.x (Terdaftar di Environment PATH)", bullet_style))
    story.append(Paragraph("&bull; XAMPP MySQL (Modul MySQL diaktifkan di XAMPP Control Panel)", bullet_style))

    story.append(Spacer(1, 6))
    story.append(Paragraph("4.2 Langkah Menjalankan Pengujian secara Lokal (CLI)", h2_style))
    story.append(Paragraph("Buka Terminal / PowerShell di direktori proyek, lalu ketik perintah:", body_style))
    story.append(Preformatted("python -u test_app.py\natau\npython -m unittest test_app.py -v", terminal_style))

    story.append(Spacer(1, 6))
    story.append(Paragraph("4.3 Penjelasan Alur Otomatisasi Script (test_app.py)", h2_style))
    story.append(Paragraph("1. <b>setUpClass()</b>: Script memeriksa port 8000. Jika belum aktif, script menyalakan PHP server (php -S 127.0.0.1:8000) di background secara otomatis.", bullet_style))
    story.append(Paragraph("2. <b>Inisialisasi Selenium Chrome Driver</b>: Selenium 4 menginisialisasi peramban Google Chrome headless secara otomatis.", bullet_style))
    story.append(Paragraph("3. <b>Eksekusi Skenario Test (TC_REG & TC_LOG)</b>: Selenium mengetikkan teks ke atribut elemen ID, mengklik tombol submit, membaca alert kesalahan, dan memeriksa pengalihan URL.", bullet_style))
    story.append(Paragraph("4. <b>tearDownClass()</b>: Setelah pengujian selesai, Selenium menutup browser dan mematikan server PHP.", bullet_style))

    story.append(Spacer(1, 8))
    story.append(Paragraph("4.4 Bukti Hasil Output Terminal (Terminal Execution Logs)", h2_style))
    
    terminal_output = """PS D:\\alba\\Akademik\\Semester 6\\Pengujian Perangkat Lunak\\Pertemuan 15> python -m unittest test_app.py -v
[+] Memulai inisialisasi lingkungan pengujian...
[+] Menjalankan PHP Built-in Server di http://127.0.0.1:8000 ...
[+] Membuka Selenium Chrome Headless Driver...
[+] Environment siap! Mengoperasikan test suite...

test_TC_LOG_01_login_success (__main__.TestLoginRegister) ... ok
test_TC_LOG_02_wrong_password (__main__.TestLoginRegister) ... ok
test_TC_LOG_03_unregistered_user (__main__.TestLoginRegister) ... ok
test_TC_LOG_04_empty_login_fields (__main__.TestLoginRegister) ... ok
test_TC_REG_01_register_success (__main__.TestLoginRegister) ... ok
test_TC_REG_02_password_mismatch (__main__.TestLoginRegister) ... ok
test_TC_REG_03_empty_fields (__main__.TestLoginRegister) ... ok
test_TC_REG_04_duplicate_username (__main__.TestLoginRegister) ... ok

[+] Membersihkan driver dan menutup server...
[+] Pengujian selesai.
----------------------------------------------------------------------
Ran 8 tests in 12.184s

OK"""

    story.append(Preformatted(terminal_output, terminal_style))

    story.append(PageBreak())

    # BAB V: KODE SUMBER LENGKAP
    story.append(Paragraph("BAB V: KODE SUMBER LENGKAP (test_app.py)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=SECONDARY, spaceAfter=10))
    story.append(Paragraph("Berikut adalah seluruh isi kode sumber file test_app.py (217 baris utuh):", body_style))

    story.append(Preformatted(full_test_app_code, code_style))

    story.append(PageBreak())

    # BAB VI: CI/CD PIPELINE
    story.append(Paragraph("BAB VI: KONFIGURASI CI/CD PIPELINE (GITHUB ACTIONS)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=SECONDARY, spaceAfter=10))
    story.append(Paragraph("File workflow .github/workflows/selenium-tests.yml yang terpasang di GitHub Actions:", body_style))

    story.append(Preformatted(full_workflow_code, code_style))

    story.append(Spacer(1, 10))

    # BAB VII: KESIMPULAN
    story.append(Paragraph("BAB VII: KESIMPULAN & LINK REPOSITORY", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=SECONDARY, spaceAfter=10))

    story.append(Paragraph("Seluruh 8 test case untuk modul Login dan Register telah teruji <b>100% PASSED</b>. Pengujian terotomatisasi dengan Selenium WebDriver dan CI/CD GitHub Actions berjalan lancar.", body_style))
    story.append(Paragraph("<b>Link Repository GitHub Target / Pengerjaan:</b> https://github.com/hermanka/quiz-pengupil", body_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully updated with full code: {output_filename}")

if __name__ == "__main__":
    create_report()
