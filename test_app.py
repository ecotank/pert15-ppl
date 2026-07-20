import os
import sys
import time
import socket
import subprocess
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

BASE_URL = "http://127.0.0.1:8000"

class TestLoginRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\n[+] Memulai inisialisasi lingkungan pengujian...", flush=True)
        cls.php_process = None
        
        # Check if PHP server is running on 127.0.0.1:8000
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            res = sock.connect_ex(('127.0.0.1', 8000))
            sock.close()
            if res != 0:
                print("[+] Menjalankan PHP Built-in Server di http://127.0.0.1:8000 ...", flush=True)
                cls.php_process = subprocess.Popen(
                    ["php", "-S", "127.0.0.1:8000"],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                time.sleep(1.5)
            else:
                print("[+] PHP Server sudah aktif di http://127.0.0.1:8000", flush=True)
        except Exception as e:
            print(f"[!] Warning server check: {e}", flush=True)

        print("[+] Membuka Selenium Chrome Headless Driver...", flush=True)
        chrome_options = Options()
        # chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        # Selenium 4 automatically handles chromedriver management natively
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(5)
        print("[+] Environment siap! Mengoperasikan test suite...\n", flush=True)

    @classmethod
    def tearDownClass(cls):
        print("\n[+] Membersihkan driver dan menutup server...", flush=True)
        if hasattr(cls, 'driver') and cls.driver:
            cls.driver.quit()
        if cls.php_process:
            cls.php_process.terminate()
        print("[+] Pengujian selesai.", flush=True)

    def setUp(self):
        # Clear cookies before each test to reset session
        self.driver.get(f"{BASE_URL}/login.php")
        self.driver.delete_all_cookies()

    # ==========================================
    # MODUL REGISTER TEST CASES
    # ==========================================

    def test_TC_REG_01_register_success(self):
        """TC_REG_01: Registrasi berhasil dengan data valid"""
        self.driver.get(f"{BASE_URL}/register.php")
        test_user = f"user_{int(time.time())}"
        
        self.driver.find_element(By.ID, "name").send_keys("Pengguna Test Valid")
        self.driver.find_element(By.ID, "InputEmail").send_keys(f"{test_user}@example.com")
        self.driver.find_element(By.ID, "username").send_keys(test_user)
        self.driver.find_element(By.ID, "InputPassword").send_keys("password123")
        self.driver.find_element(By.ID, "InputRePassword").send_keys("password123")
        
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(1)

        self.assertIn("index.php", self.driver.current_url)
        welcome_elem = self.driver.find_element(By.ID, "welcome-user")
        self.assertEqual(welcome_elem.text, test_user)

    def test_TC_REG_02_password_mismatch(self):
        """TC_REG_02: Registrasi gagal - Password dan Re-Password tidak cocok"""
        self.driver.get(f"{BASE_URL}/register.php")
        
        self.driver.find_element(By.ID, "name").send_keys("User Beda Password")
        self.driver.find_element(By.ID, "InputEmail").send_keys("bedapass@example.com")
        self.driver.find_element(By.ID, "username").send_keys("bedapassuser")
        self.driver.find_element(By.ID, "InputPassword").send_keys("password123")
        self.driver.find_element(By.ID, "InputRePassword").send_keys("password999")
        
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(1)

        error_msg = self.driver.find_element(By.CLASS_NAME, "text-danger").text
        self.assertIn("Password tidak sama", error_msg)

    def test_TC_REG_03_empty_fields(self):
        """TC_REG_03: Registrasi gagal - Data tidak boleh kosong"""
        self.driver.get(f"{BASE_URL}/register.php")
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(1)

        alert = self.driver.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertIn("Data tidak boleh kosong", alert)

    def test_TC_REG_04_duplicate_username(self):
        """TC_REG_04: Registrasi gagal - Username sudah terdaftar"""
        dup_username = "userduplikasi"
        self.driver.get(f"{BASE_URL}/register.php")
        self.driver.find_element(By.ID, "name").send_keys("User Pertama")
        self.driver.find_element(By.ID, "InputEmail").send_keys("dup1@example.com")
        self.driver.find_element(By.ID, "username").send_keys(dup_username)
        self.driver.find_element(By.ID, "InputPassword").send_keys("password123")
        self.driver.find_element(By.ID, "InputRePassword").send_keys("password123")
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(1)

        self.driver.get(f"{BASE_URL}/index.php?action=logout")
        time.sleep(1)

        self.driver.get(f"{BASE_URL}/register.php")
        self.driver.find_element(By.ID, "name").send_keys("User Kedua")
        self.driver.find_element(By.ID, "InputEmail").send_keys("dup2@example.com")
        self.driver.find_element(By.ID, "username").send_keys(dup_username)
        self.driver.find_element(By.ID, "InputPassword").send_keys("password123")
        self.driver.find_element(By.ID, "InputRePassword").send_keys("password123")
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(1)

        alert = self.driver.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertIn("Username sudah terdaftar", alert)

    # ==========================================
    # MODUL LOGIN TEST CASES
    # ==========================================

    def test_TC_LOG_01_login_success(self):
        """TC_LOG_01: Login berhasil dengan data valid"""
        user = "loginvaliduser"
        password = "secretpassword"
        
        self.driver.get(f"{BASE_URL}/register.php")
        self.driver.find_element(By.ID, "name").send_keys("Login Valid")
        self.driver.find_element(By.ID, "InputEmail").send_keys("loginvalid@example.com")
        self.driver.find_element(By.ID, "username").send_keys(user)
        self.driver.find_element(By.ID, "InputPassword").send_keys(password)
        self.driver.find_element(By.ID, "InputRePassword").send_keys(password)
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(1)

        self.driver.get(f"{BASE_URL}/index.php?action=logout")
        time.sleep(1)

        self.driver.get(f"{BASE_URL}/login.php")
        self.driver.find_element(By.ID, "username").send_keys(user)
        self.driver.find_element(By.ID, "InputPassword").send_keys(password)
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(1)

        self.assertIn("index.php", self.driver.current_url)
        welcome_elem = self.driver.find_element(By.ID, "welcome-user")
        self.assertEqual(welcome_elem.text, user)

    def test_TC_LOG_02_wrong_password(self):
        """TC_LOG_02: Login gagal - Password salah"""
        user = "passsalahuser"
        password = "correctpassword"

        self.driver.get(f"{BASE_URL}/register.php")
        self.driver.find_element(By.ID, "name").send_keys("Pass Salah")
        self.driver.find_element(By.ID, "InputEmail").send_keys("passsalah@example.com")
        self.driver.find_element(By.ID, "username").send_keys(user)
        self.driver.find_element(By.ID, "InputPassword").send_keys(password)
        self.driver.find_element(By.ID, "InputRePassword").send_keys(password)
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(1)

        self.driver.get(f"{BASE_URL}/index.php?action=logout")
        time.sleep(1)

        self.driver.get(f"{BASE_URL}/login.php")
        self.driver.find_element(By.ID, "username").send_keys(user)
        self.driver.find_element(By.ID, "InputPassword").send_keys("wrongpassword")
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(1)

        self.assertIn("login.php", self.driver.current_url)

    def test_TC_LOG_03_unregistered_user(self):
        """TC_LOG_03: Login gagal - Username tidak terdaftar"""
        self.driver.get(f"{BASE_URL}/login.php")
        self.driver.find_element(By.ID, "username").send_keys("nonexistentuser999")
        self.driver.find_element(By.ID, "InputPassword").send_keys("anypassword")
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(1)

        alert = self.driver.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertIn("Register User Gagal", alert)

    def test_TC_LOG_04_empty_login_fields(self):
        """TC_LOG_04: Login gagal - Data tidak boleh kosong"""
        self.driver.get(f"{BASE_URL}/login.php")
        self.driver.find_element(By.NAME, "submit").click()
        time.sleep(1)

        alert = self.driver.find_element(By.CLASS_NAME, "alert-danger").text
        self.assertIn("Data tidak boleh kosong", alert)

if __name__ == "__main__":
    unittest.main(verbosity=2)
