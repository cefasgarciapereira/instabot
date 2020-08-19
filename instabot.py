from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
import numpy as np

class InstaBot:
    #Initialize the session
    def __init__(self, username, password):
        self.username = username
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(username)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(password)
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div').click()
        sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    
    #Go to specific link
    def navigate_to(self, url):
        self.driver.get(url)
        sleep(2)
    
    #Type and submit a text inside the Ypffh field
    def comment(self, text):
        self.driver.find_element_by_class_name('Ypffh').click()
        self.driver.find_element_by_class_name('Ypffh').send_keys(text)
        sleep(2)
        self.driver.find_element_by_xpath('//button[contains(text(), "Publicar")]').click()
        sleep(5)
    
    #Generate a string containg tags of friends from a list
    def generate_tags(self, lst, number_of_friends):
        sub = np.random.choice(lst,number_of_friends, replace=False)
        response = ''
        for s in sub:
            response += s+' '
        return response