from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
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
    #Initialize the session
    def __init__(self, username, password, headless=False, auth_code=None):
        self.username = username

        chrome_options = Options()
        browser_path = _find_browser()
        if browser_path:
            chrome_options.binary_location = browser_path
        if(headless):
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.get("https://instagram.com")
        sleep(2)
        
        try:
            self.driver.find_element("xpath", "//input[@name = 'email']").send_keys(username)
            self.driver.find_element("xpath", "//input[@name = 'pass']").send_keys(password)
            self.driver.find_element("xpath",  "//div[@aria-label = 'Log In']").click()
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
                self.driver.find_element("xpath", "//input[@aria-label='Security Code']").send_keys(auth_code)
                sleep(1)
                try:
                    self.driver.find_element("xpath", "//button[text()='Confirm']").click()
                except:
                    self.driver.find_element("xpath", "//button[text()='Confirmar']").click()
                sleep(3)
                print("Autenticação de 2 fatores concluída.")
            except Exception as err:
                print("Erro na autenticação de 2 fatores: ")
                print(err)
        
        # close alerts
        try:
            self.driver.find_element("xpath", "//button[text() = 'Agora não']").click()
            sleep(2)
            self.driver.find_element("xpath", "//button[text() = 'Agora não']").click()
        except:
            try:
                self.driver.find_element("xpath", "//button[text() = 'Not now']").click()
                sleep(2)
                self.driver.find_element("xpath", "//button[text() = 'Not now']").click()
            except:
                print("Failed to skip warnings automatically, you will have 25 seconds to close them.")
    
    #Go to specific link
    def navigate_to(self, url):
        self.driver.get(url)
        sleep(2)
    
    #Type and submit a text inside the Ypffh field
    def comment(self, text):
        self.driver.find_element("xpath", "//textarea[@placeholder = 'Add a comment…']").click()
        self.driver.find_element("xpath", "//textarea[@placeholder = 'Add a comment…']").send_keys(text)
        sleep(2)
        self.driver.find_element("xpath", "//div[text() = 'Post']").click()
        sleep(5)
    
    #Generate a string containg tags of friends from a list
    def generate_tags(self, lst, number_of_friends):
        sub = np.random.choice(lst,number_of_friends, replace=False)
        response = ''
        for s in sub:
            response += s+' '
        return response