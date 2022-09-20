from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
import numpy as np

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
            #self.driver = webdriver.Chrome(executable_path="./chromedriver")
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element("xpath","/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input").send_keys(username)
        self.driver.find_element("xpath","/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input").send_keys(password)
        sleep(2)
        self.driver.find_element("xpath",'/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
        sleep(2)
        try:
            # wait for 2 factor authetication
            two_factor_authentication = self.driver.find_element("xpath",'/html/body/div[1]/section/main/div/div/div[1]/div[2]/div')
            print("two factor?")
            print(two_factor_authentication)
            if(two_factor_authentication):
                print("Insira o código de autenticação de 2 fatores (pausa de 20 segundos)")
                sleep(20)
        except Exception:
            pass
        self.driver.find_element("xpath",'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button').click()
        self.driver.find_element("xpath",'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
    
    #Go to specific link
    def navigate_to(self, url):
        self.driver.get(url)
        sleep(2)
    
    #Type and submit a text inside the Ypffh field
    def comment(self, text):
        self.driver.find_element('xpath','/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea').click()
        self.driver.find_element('xpath','/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea').send_keys(text)
        sleep(2)
        self.driver.find_element('xpath','/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button').click()
        sleep(5)
    
    #Generate a string containg tags of friends from a list
    def generate_tags(self, lst, number_of_friends):
        sub = np.random.choice(lst,number_of_friends, replace=False)
        response = ''
        for s in sub:
            response += s+' '
        return response