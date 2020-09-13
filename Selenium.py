from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

username = input('Enter Username')
password = input('Enter Password')

PATH = "/home/nikhil/Desktop/Programs/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get('https://app.corsalite.com/v1/#')
search = driver.find_element_by_name('email')
search.send_keys(username)
search1 = driver.find_element_by_name('password')
search1.send_keys(password)
search.send_keys(Keys.RETURN)
driver.switch_to.alert.accept()
time.sleep(5)
driver.get('https://app.corsalite.com/v1/examination/exam/0/0/0/0/4090909')
print(driver.page_source())
