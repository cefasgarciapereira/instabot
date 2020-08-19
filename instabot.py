from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import numpy as np

class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        sleep(2)
        self.driver.find_element_by_xpath('//div[contains(text(), "Entrar")]').click()
        sleep(5)
        self.driver.find_element_by_xpath('//button[contains(text(), "Agora não")]').click()
        sleep(2)
        self.driver.find_element_by_xpath('//button[contains(text(), "Agora não")]').click()
    
    def navigate_to(self, url):
        self.driver.get(url)
        sleep(2)
    
    def comment(self, text):
        self.driver.find_element_by_class_name('Ypffh').click()
        self.driver.find_element_by_class_name('Ypffh').send_keys(text)
        sleep(2)
        self.driver.find_element_by_xpath('//button[contains(text(), "Publicar")]').click()
    
    def generate_tags(self, lst, number_of_friends):
        sub = np.random.choice(lst,2, replace=False)
        response = ''
        for s in sub:
            response += s+' '
        return response