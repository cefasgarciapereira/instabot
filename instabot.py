from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time
import numpy as np
import shutil
import sys

def _find_browser():
    if sys.platform == "win32":
        candidates = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        ]
        return next((p for p in candidates if shutil.os.path.exists(p)), None)
    else:
        candidates = ["google-chrome", "google-chrome-stable", "chromium", "chromium-browser"]
        return next((shutil.which(c) for c in candidates if shutil.which(c)), None)

class InstaBot:
    def __init__(self, username, password, headless=False, auth_code=None):
        self.username = username

        chrome_options = Options()
        browser_path = _find_browser()
        if browser_path:
            chrome_options.binary_location = browser_path

        # Force English so text/aria-label selectors are consistent across all users
        chrome_options.add_argument('--lang=en-US')
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en-US,en'})

        if headless:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://instagram.com")
        sleep(2)

        try:
            self._find_element([("xpath", "//input[@name='email']")]).send_keys(username)
            self._find_element([("xpath", "//input[@name='pass']")]).send_keys(password)
            self._find_element([
                ("xpath", "//button[@type='submit']"),
                ("xpath", "//button[contains(., 'Log in')]"),
                ("xpath", "//div[contains(@aria-label, 'Log')]"),
            ]).click()
            sleep(2)
        except Exception as err:
            print("Error during login: ")
            print(err)

        # 2-factor authentication
        if auth_code:
            try:
                print("Aguardando página de autenticação de 2 fatores...")
                WebDriverWait(self.driver, 15).until(
                    lambda d: "/accounts/login/two_factor" in d.current_url
                )
                self._find_element([
                    ("xpath", "//input[@name='verificationCode']"),
                    ("xpath", "//input[@autocomplete='one-time-code']"),
                    ("xpath", "//input[contains(@aria-label, 'Security')]"),
                    ("xpath", "//input[contains(@aria-label, 'Code')]"),
                ]).send_keys(auth_code)
                sleep(1)
                self._find_element([
                    ("xpath", "//button[@type='submit']"),
                    ("xpath", "//button[contains(., 'Confirm')]"),
                ]).click()
                sleep(10)
                print("Autenticação de 2 fatores concluída.")
            except Exception as err:
                print("Erro na autenticação de 2 fatores: ")
                print(err)

        # close alerts
        not_now_selectors = [
            ("xpath", "//button[contains(text(), 'Not now')]"),
            ("xpath", "//button[contains(text(), 'Not Now')]"),
            ("xpath", "//button[contains(text(), 'Agora não')]"),
        ]
        for i in range(2):
            try:
                self._find_element(not_now_selectors, timeout=5).click()
                sleep(2)
            except Exception:
                if i == 0:
                    print("Failed to skip warnings automatically, you will have 25 seconds to close them.")
                break

    def _find_element(self, selectors, timeout=10):
        """Try multiple selectors in order, returning the first available element within timeout."""
        end_time = time() + timeout
        while time() < end_time:
            for by, value in selectors:
                try:
                    return self.driver.find_element(by, value)
                except NoSuchElementException:
                    continue
            sleep(0.5)
        raise NoSuchElementException(f"None of the selectors matched: {selectors}")

    def navigate_to(self, url):
        self.driver.get(url)
        sleep(2)

    def comment(self, text):
        textarea = self._find_element([
            ("xpath", "//textarea[contains(@placeholder, 'comment')]"),
            ("xpath", "//textarea[contains(@aria-label, 'comment')]"),
            ("xpath", "//textarea[contains(translate(@placeholder, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'comment')]"),
        ])
        textarea.click()
        textarea.send_keys(text)
        sleep(2)
        self._find_element([
            ("xpath", "//div[contains(text(), 'Post')]"),
            ("xpath", "//button[contains(text(), 'Post')]"),
            ("xpath", "//div[@role='button'][contains(., 'Post')]"),
        ]).click()
        sleep(5)

    def generate_tags(self, lst, number_of_friends):
        sub = np.random.choice(lst, number_of_friends, replace=False)
        response = ''
        for s in sub:
            response += s + ' '
        return response
