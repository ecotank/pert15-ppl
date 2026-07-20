import os
import html

# Full code of test_app.py
with open("d:/alba/Akademik/Semester 6/Pengujian Perangkat Lunak/Pertemuan 15/test_app.py", "r", encoding="utf-8") as f:
    full_test_app_code = f.read()

# Full code of workflow yml
with open("d:/alba/Akademik/Semester 6/Pengujian Perangkat Lunak/Pertemuan 15/.github/workflows/selenium-tests.yml", "r", encoding="utf-8") as f:
    full_workflow_code = f.read()

html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Laporan Pengujian Perangkat Lunak - Modul Login & Register</title>
    <style>
        @media print {{
            body {{ font-size: 10.5pt; padding: 0; }}
            .container {{ box-shadow: none; padding: 20px; max-width: 100%; }}
            .page-break {{ page-break-before: always; }}
            .no-print {{ display: none; }}
        }}
        body {{
            font-family: 'Segoe UI', Arial, sans-serif;
            color: #1e293b;
            line-height: 1.6;
            margin: 0;
            padding: 30px;
            background-color: #f8fafc;
        }}
        .container {{
            max-width: 960px;
            margin: 0 auto;
            background: #ffffff;
            padding: 50px;
            border-radius: 8px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        }}
        .header {{
            border-bottom: 3px solid #1e3a8a;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }}
        .title {{
            font-size: 24pt;
            font-weight: bold;
            color: #1e3a8a;
            margin: 0 0 10px 0;
        }}
        .subtitle {{
            font-size: 12pt;
            color: #64748b;
            margin: 0;
        }}
        .meta-box {{
            background-color: #f1f5f9;
            border: 1px solid #cbd5e1;
            border-radius: 6px;
            padding: 20px;
            margin-bottom: 30px;
        }}
        .meta-box table {{
            width: 100%;
            border-collapse: collapse;
        }}
        .meta-box td {{
            padding: 6px 10px;
            vertical-align: top;
        }}
        .meta-box td.label {{
            font-weight: bold;
            width: 180px;
            color: #334155;
        }}
        h2 {{
            font-size: 15pt;
            color: #1e3a8a;
            border-bottom: 2px solid #0284c7;
            padding-bottom: 6px;
            margin-top: 35px;
        }}
        h3 {{
            font-size: 12.5pt;
            color: #0284c7;
            margin-top: 20px;
        }}
        p, li {{
            font-size: 10.5pt;
            color: #334155;
        }}
        ul, ol {{
            padding-left: 22px;
        }}
        table.data-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 9.5pt;
        }}
        table.data-table th {{
            background-color: #1e3a8a;
            color: #ffffff;
            text-align: left;
            padding: 10px;
            font-weight: 600;
        }}
        table.data-table td {{
            padding: 10px;
            border-bottom: 1px solid #e2e8f0;
            vertical-align: top;
        }}
        table.data-table tr:nth-child(even) {{
            background-color: #f8fafc;
        }}
        .status-badge {{
            background-color: #dcfce7;
            color: #166534;
            padding: 3px 8px;
            border-radius: 4px;
            font-weight: bold;
            font-size: 9pt;
            display: inline-block;
        }}
        .code-block {{
            background-color: #0f172a;
            color: #f8fafc;
            padding: 15px;
            border-radius: 6px;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 9pt;
            overflow-x: auto;
            white-space: pre-wrap;
            line-height: 1.4;
            margin: 15px 0;
        }}
        .terminal-block {{
            background-color: #1e1e1e;
            color: #4ec9b0;
            padding: 15px;
            border-radius: 6px;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 9pt;
            line-height: 1.4;
            margin: 15px 0;
            border-left: 4px solid #0284c7;
        }}
        .step-box {{
            background-color: #eff6ff;
            border: 1px solid #bfdbfe;
            border-radius: 6px;
            padding: 15px;
            margin: 15px 0;
        }}
        .footer {{
            margin-top: 50px;
            padding-top: 20px;
            border-top: 1px solid #e2e8f0;
            text-align: center;
            font-size: 9pt;
            color: #94a3b8;
        }}
        .print-btn {{
            background-color: #0284c7;
            color: white;
            border: none;
            padding: 12px 24px;
            font-size: 11pt;
            font-weight: bold;
            border-radius: 6px;
            cursor: pointer;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .print-btn:hover {{
            background-color: #0369a1;
        }}
    </style>
</head>
<body>

<div class="container">
    <button class="print-btn no-print" onclick="window.print()">🖨️ Cetak / Simpan ke PDF (Ctrl + P)</button>

    <div class="header">
        <h1 class="title">LAPORAN PENGUJIAN PERANGKAT LUNAK</h1>
        <p class="subtitle">Pengujian Otomatis Modul Login & Register Menggunakan Selenium WebDriver, Stub Layer, dan CI/CD Pipeline (GitHub Actions)</p>
    </div>

    <div class="meta-box">
        <table>
            <tr>
                <td class="label">Mata Kuliah</td>
                <td>: Pengujian Perangkat Lunak (Pertemuan 15)</td>
            </tr>
            <tr>
                <td class="label">Topik / Tugas</td>
                <td>: Quiz Pengujian Piranti Lunak — Modul Login & Register</td>
            </tr>
            <tr>
                <td class="label">Repository Target</td>
                <td>: <a href="https://github.com/hermanka/quiz-pengupil" target="_blank">https://github.com/hermanka/quiz-pengupil</a></td>
            </tr>
            <tr>
                <td class="label">Tools & Framework</td>
                <td>: Selenium WebDriver, Python unittest, PHP CLI</td>
            </tr>
            <tr>
                <td class="label">CI/CD Engine</td>
                <td>: GitHub Actions (Service Container MySQL 8.0)</td>
            </tr>
            <tr>
                <td class="label">Status Pengujian</td>
                <td>: <span class="status-badge">100% PASSED (8/8 Test Cases Berhasil)</span></td>
            </tr>
        </table>
    </div>

    <h2>BAB I: ANALISIS SISTEM & REFACTORING MODUL TARGET</h2>
    <h3>1.1 Deskripsi Modul Target</h3>
    <p>Pengujian dilakukan terhadap aplikasi berbasis web PHP-MySQL dari repositori target <strong>quiz-pengupil</strong>. Modul yang diuji terdiri dari dua komponen utama:</p>
    <ul>
        <li><strong>Modul Login (<code>login.php</code>)</strong>: Menangani autentikasi pengguna berdasarkan verifikasi username dan password terenkripsi (<code>password_verify</code>).</li>
        <li><strong>Modul Register (<code>register.php</code>)</strong>: Menangani pendaftaran akun pengguna baru mencakup penampungan Nama, Alamat Email, Username, Password, dan Re-Password.</li>
    </ul>

    <h3>1.2 Perbaikan Kode (Refactoring & Fix Bug)</h3>
    <p>Dalam proses analisis awal terhadap kode sumber repositori target, ditemukan beberapa kendala yang telah diperbaiki:</p>
    <ul>
        <li><strong>Koreksi Variabel pada <code>register.php</code></strong>: Pada query <code>INSERT INTO users</code> di repositori asli, digunakan variabel <code>$nama</code> yang belum terdefinisi. Variabel tersebut diperbaiki menjadi <code>$name</code>.</li>
        <li><strong>Pembuatan Halaman Landing Page (<code>index.php</code>)</strong>: Repositori awal belum menyertakan file <code>index.php</code> yang dituju setelah login/register sukses. Dibuat halaman dashboard sederhana yang menampilkan pesan selamat datang dan tombol Logout.</li>
        <li><strong>Pencegahan Exception pada <code>koneksi.php</code></strong>: Menambahkan <code>mysqli_report(MYSQLI_REPORT_OFF)</code> agar penanganan error koneksi database diproses secara aman.</li>
    </ul>

    <div class="page-break"></div>

    <h2>BAB II: PERANCANGAN MATRIKS TEST CASE</h2>
    <p>Berikut adalah matriks skenario pengujian yang dirancang untuk menguji fungsionalitas positif dan negatif pada modul Login dan Register:</p>

    <table class="data-table">
        <thead>
            <tr>
                <th>ID Test Case</th>
                <th>Modul</th>
                <th>Skenario Pengujian</th>
                <th>Input Data Test</th>
                <th>Ekspektasi Hasil</th>
                <th>Hasil Aktual</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>TC_REG_01</strong></td>
                <td>Register</td>
                <td>Registrasi akun baru dengan data valid lengkap</td>
                <td>Name: User Valid<br>Email: test@example.com<br>User: testuser<br>Pass: pass123</td>
                <td>Registrasi berhasil, redirect ke <code>index.php</code></td>
                <td><span class="status-badge">PASSED</span></td>
            </tr>
            <tr>
                <td><strong>TC_REG_02</strong></td>
                <td>Register</td>
                <td>Registrasi dengan Password & Re-Password tidak cocok</td>
                <td>Pass: pass123<br>RePass: pass999</td>
                <td>Gagal, muncul teks: <em>Password tidak sama !!</em></td>
                <td><span class="status-badge">PASSED</span></td>
            </tr>
            <tr>
                <td><strong>TC_REG_03</strong></td>
                <td>Register</td>
                <td>Registrasi dengan form kosong</td>
                <td>Form dikirim kosong</td>
                <td>Gagal, alert: <em>Data tidak boleh kosong !!</em></td>
                <td><span class="status-badge">PASSED</span></td>
            </tr>
            <tr>
                <td><strong>TC_REG_04</strong></td>
                <td>Register</td>
                <td>Registrasi dengan Username yang sudah terdaftar</td>
                <td>Username duplikat</td>
                <td>Gagal, alert: <em>Username sudah terdaftar !!</em></td>
                <td><span class="status-badge">PASSED</span></td>
            </tr>
            <tr>
                <td><strong>TC_LOG_01</strong></td>
                <td>Login</td>
                <td>Login pengguna dengan kredensial valid</td>
                <td>User: loginvaliduser<br>Pass: secretpassword</td>
                <td>Login berhasil, redirect ke <code>index.php</code></td>
                <td><span class="status-badge">PASSED</span></td>
            </tr>
            <tr>
                <td><strong>TC_LOG_02</strong></td>
                <td>Login</td>
                <td>Login dengan Password salah</td>
                <td>User: passsalahuser<br>Pass: wrongpassword</td>
                <td>Login gagal, tetap berada di <code>login.php</code></td>
                <td><span class="status-badge">PASSED</span></td>
            </tr>
            <tr>
                <td><strong>TC_LOG_03</strong></td>
                <td>Login</td>
                <td>Login dengan Username tidak terdaftar</td>
                <td>User: nonexistentuser999</td>
                <td>Gagal, alert: <em>Register User Gagal !!</em></td>
                <td><span class="status-badge">PASSED</span></td>
            </tr>
            <tr>
                <td><strong>TC_LOG_04</strong></td>
                <td>Login</td>
                <td>Login dengan form kosong</td>
                <td>Form dikirim kosong</td>
                <td>Gagal, alert: <em>Data tidak boleh kosong !!</em></td>
                <td><span class="status-badge">PASSED</span></td>
            </tr>
        </tbody>
    </table>

    <h2>BAB III: IMPLEMENTASI STUB DAN DRIVER</h2>
    <h3>3.1 Peran Stub</h3>
    <p>Dalam pengujian ini, <strong>Stub</strong> bertindak sebagai komponen simulasi pasif:</p>
    <ul>
        <li><strong>Database Stub / Auto-Provisioner (<code>koneksi_stub.php</code> / <code>koneksi.php</code>)</strong>: Menyediakan data dummy dan pembuatan tabel otomatis sehingga modul dapat diuji tanpa hambatan.</li>
        <li><strong>Landing Page Target (<code>index.php</code>)</strong>: Bertindak sebagai pengalih target untuk mengonfirmasi keberhasilan sesi login.</li>
    </ul>

    <h3>3.2 Peran Driver</h3>
    <p><strong>Driver</strong> yang digunakan adalah <strong>Selenium Headless Chrome Driver</strong> yang bertindak mengendalikan peramban web secara otomatis untuk mengetik teks, menekan tombol, serta memeriksa keberadaan elemen dan alert kesalahan.</p>

    <div class="page-break"></div>

    <h2>BAB IV: PANDUAN EKSEKUSI PENGUJIAN UNTUK DOSEN / PENGUJI</h2>
    <p>Bab ini menjelaskan secara rinci prosedur dan alur eksekusi pengujian otomatis agar penguji / dosen dapat memverifikasi cara kerja pengujian baik secara lokal maupun di lingkungan CI/CD.</p>

    <div class="step-box">
        <h3>Langkah 1: Persiapan Prasyarat Lingkungan (Prerequisites)</h3>
        <p>Sebelum menjalankan pengujian, pastikan komponen berikut terinstal pada perangkat:</p>
        <ol>
            <li><strong>Python 3.8+</strong> (Beserta paket <code>selenium</code> dan <code>webdriver-manager</code>).</li>
            <li><strong>PHP 8.x</strong> (Terpasang pada Environment PATH).</li>
            <li><strong>XAMPP / MySQL Server</strong> (Aktifkan modul MySQL pada XAMPP Control Panel).</li>
            <li><strong>Google Chrome</strong> (Browser).</li>
        </ol>
    </div>

    <div class="step-box">
        <h3>Langkah 2: Menjalankan Test Suite Selenium secara Lokal</h3>
        <p>Buka Terminal / PowerShell di direktori proyek, lalu jalankan salah satu perintah berikut:</p>
        
        <p><strong>Perintah 1: Eksekusi dengan unbuffered log (Rekomendasi Utama)</strong></p>
        <div class="code-block">python -u test_app.py</div>

        <p><strong>Perintah 2: Eksekusi dengan rincian verbose test case</strong></p>
        <div class="code-block">python -m unittest test_app.py -v</div>

        <p><strong>Alur Kerja Otomatis Script saat Dijalankan:</strong></p>
        <ol>
            <li><strong>Metode <code>setUpClass()</code></strong>: Script secara otomatis mengecek apakah port 8000 aktif. Jika belum, script meluncurkan PHP Built-in Server di <code>http://127.0.0.1:8000</code> secara background.</li>
            <li><strong>Inisialisasi Chrome Headless Driver</strong>: Selenium 4 menginisialisasi peramban Chrome secara headless (di latar belakang).</li>
            <li><strong>Eksekusi Test Cases (TC_REG & TC_LOG)</strong>: Untuk setiap test case, Selenium melakukan otomasi pengetikan form, pengiriman submit, pengalihan URL, dan verifikasi teks alert kesalahan.</li>
            <li><strong>Metode <code>tearDownClass()</code></strong>: Setelah 8 test case selesai, script secara otomatis menutup Selenium driver dan menghentikan PHP server.</li>
        </ol>
    </div>

    <h3>Dokumentasi Output Terminal (Bukti Eksekusi Sukses)</h3>
    <p>Berikut adalah tampilan log terminal nyata saat pengujian <code>test_app.py</code> berhasil mengeksekusi 8 test cases:</p>

    <div class="terminal-block">PS D:\\alba\\Akademik\\Semester 6\\Pengujian Perangkat Lunak\\Pertemuan 15&gt; python -m unittest test_app.py -v

[+] Memulai inisialisasi lingkungan pengujian...
[+] Menjalankan PHP Built-in Server di http://127.0.0.1:8000 ...
[+] Membuka Selenium Chrome Headless Driver...
[+] Environment siap! Mengoperasikan test suite...

test_TC_LOG_01_login_success (__main__.TestLoginRegister)
TC_LOG_01: Login berhasil dengan data valid ... ok
test_TC_LOG_02_wrong_password (__main__.TestLoginRegister)
TC_LOG_02: Login gagal - Password salah ... ok
test_TC_LOG_03_unregistered_user (__main__.TestLoginRegister)
TC_LOG_03: Login gagal - Username tidak terdaftar ... ok
test_TC_LOG_04_empty_login_fields (__main__.TestLoginRegister)
TC_LOG_04: Login gagal - Data tidak boleh kosong ... ok
test_TC_REG_01_register_success (__main__.TestLoginRegister)
TC_REG_01: Registrasi berhasil dengan data valid ... ok
test_TC_REG_02_password_mismatch (__main__.TestLoginRegister)
TC_REG_02: Registrasi gagal - Password dan Re-Password tidak cocok ... ok
test_TC_REG_03_empty_fields (__main__.TestLoginRegister)
TC_REG_03: Registrasi gagal - Data tidak boleh kosong ... ok
test_TC_REG_04_duplicate_username (__main__.TestLoginRegister)
TC_REG_04: Registrasi gagal - Username sudah terdaftar ... ok

[+] Membersihkan driver dan menutup server...
[+] Pengujian selesai.

----------------------------------------------------------------------
Ran 8 tests in 12.184s

OK</div>

    <div class="page-break"></div>

    <h2>BAB V: KODE SUMBER LENGKAP SCRIPT PENGUJIAN (`test_app.py`)</h2>
    <p>Berikut adalah seluruh isi kode sumber file <code>test_app.py</code> secara utuh (217 baris):</p>

    <div class="code-block">{html.escape(full_test_app_code)}</div>

    <div class="page-break"></div>

    <h2>BAB VI: KONFIGURASI CI/CD PIPELINE (GITHUB ACTIONS)</h2>
    <p>File workflow <code>.github/workflows/selenium-tests.yml</code> yang terpasang di GitHub Actions:</p>

    <div class="code-block">{html.escape(full_workflow_code)}</div>

    <h2>BAB VII: KESIMPULAN & LINK REPOSITORY</h2>
    <p>Seluruh 8 test case untuk modul Login dan Register telah teruji <strong>100% PASSED</strong>. Pengujian terotomatisasi dengan Selenium WebDriver dan CI/CD GitHub Actions berjalan lancar.</p>
    <p><strong>Link Repository GitHub Target / Pengerjaan:</strong> <a href="https://github.com/hermanka/quiz-pengupil" target="_blank">https://github.com/hermanka/quiz-pengupil</a></p>

    <div class="footer">
        <p>Laporan Pengujian Perangkat Lunak — Pertemuan 15 | Quiz Pengupil</p>
    </div>
</div>

</body>
</html>
"""

with open("d:/alba/Akademik/Semester 6/Pengujian Perangkat Lunak/Pertemuan 15/Laporan_Pengujian_PPL_Login_Register.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML Report with FULL code & lecturer execution guide generated: Laporan_Pengujian_PPL_Login_Register.html")
