##from selenium import webdriver
##from selenium.webdriver.common.keys import Keys
##from selenium.webdriver.common.action_chains import ActionChains
##from selenium.webdriver.common.by import By
##from selenium.webdriver.support.ui import WebDriverWait
##from selenium.webdriver.support import expected_conditions as EC
##import time
##import os, random
##
##PATH = os.getcwd()+"/chromedriver"
##driver = webdriver.Chrome(PATH)
##driver.get("https://www.instagram.com")
##
##time.sleep(3)
##search = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
##search.send_keys("ferr6601")
##time.sleep(0.5)
##password = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
##password.send_keys("shemademecum")
####time.sleep(5)
##search.send_keys(Keys.RETURN)
##
####main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "react-root")))
##time.sleep(random.randint(9, 10))
##driver.get("https://www.instagram.com/direct/inbox/")
##
##try:
##    time.sleep(2)
##    acpt = driver.find_element_by_xpath("//*[contains(@class, 'aOOlW   HoLwm ')]")
##    acpt.click()
##    search = driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div")
##    search.click()
##    while True:
##        message = input("Enter the message")
##        si = driver.find_element_by_tagname("textarea")
##        si.double
##        si.send_keys(message)
##        se.send_keys(Keys.RETURN)
##        if input("press 0 to stop:") == "0":
##            break
##except:
##    driver.quit()



from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


usern = input('name of user >>')
message_ = input("message >>>")

class bot:
    def __init__(self, username, password, user, message):
        self.username = input('enter username')
        self.password = input('enter password')
        self.user = user
        self.message =  message
        self.base_url = 'https://www.instagram.com/'
        self.bot = webdriver.Chrome(os.getcwd()+"/chromedriver")
        self.login()


    def login(self):
        self.bot.get(self.base_url)
        
        enter_username = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)
        self.bot.get("https://www.instagram.com/direct/inbox")
        self.bot.find_element_by_xpath("//*[contains(@class, 'aOOlW   HoLwm ')]").click()
        self.bot.find_element_by_xpath('//a[@class="xWeGp"]/*[name()="svg"][@aria-label="Direct"]').click()
        time.sleep(3)
        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button').click()
        time.sleep(2)
        self.bot.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(self.user)
        time.sleep(2)
        self.bot.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div').click()
        time.sleep(2)
        self.bot.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
        time.sleep(2)
        while True
            message = input('Enter your message')
            self.bot.find_element_by_css_selector('textarea[placeholder="Message..."]').send_keys(message)
            time.sleep(1)
            self.bot.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()

def init():     
    bot('bot_test0', 'abcdefg123456', usern, message_)
    input("DONE")

init()
