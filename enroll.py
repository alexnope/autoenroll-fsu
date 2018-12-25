from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

username = input('Username: ')
password = input('Password: ')

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)    
#login section
driver.get("http://www.my.fsu.edu")
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('fsu-login-button').click()

#Click on student center
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[1]/ul/li[2]/a/div'))).click()



