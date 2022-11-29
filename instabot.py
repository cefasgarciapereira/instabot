from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
import numpy as np
import sys

class InstaBot:
    #Initialize the session
    def __init__(self, username, password, headless=False):
        self.username = username
        
        if(headless):
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="./chromedriver")
        else:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.driver.get("https://instagram.com")
        sleep(2)
        
        try:
            self.driver.find_element("xpath", "//input[@name = 'username']").send_keys(username)
            self.driver.find_element("xpath", "//input[@name = 'password']").send_keys(password)
            self.driver.find_element("xpath", "//button[@type = 'submit']").click()
            sleep(2)
        except Exception as err:
            print("Error during login: ")
            print(err)
        
        # 2-factor authentication
        try:
            # wait for 2 factor authetication
            two_factor_authentication = self.driver.find_element("xpath", "//input[@name = 'verificationCode']")
            if(bool(two_factor_authentication)):
                print("Insira o código de autenticação de 2 fatores (pausa de 20 segundos)")
                sleep(20)
        except Exception as err:
            print("No field was identified for 2-factor authentication: ")
            print(err)
            sleep(20)
            pass
        
        # close alerts
        try:
            self.driver.find_element("xpath", "//button[text() = 'Agora não']").click()
            sleep(2)
            self.driver.find_element("xpath", "//button[text() = 'Agora não']").click()
        except:
            print("Failed to skip warnings automatically, you will have 25 seconds to close them.")
    
    #Go to specific link
    def navigate_to(self, url):
        self.driver.get(url)
        sleep(2)
    
    #Type and submit a text inside the Ypffh field
    def comment(self, text):
        self.driver.find_element("xpath", "//textarea[@placeholder = 'Adicione um comentário...']").click()
        self.driver.find_element("xpath", "//textarea[@placeholder = 'Adicione um comentário...']").send_keys(text)
        sleep(2)
        self.driver.find_element("xpath", "//button[@type = 'submit']").click()
        sleep(5)
    
    #Generate a string containg tags of friends from a list
    def generate_tags(self, lst, number_of_friends):
        sub = np.random.choice(lst,number_of_friends, replace=False)
        response = ''
        for s in sub:
            response += s+' '
        return response