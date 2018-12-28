from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

classes = []
response = ''
print('Please input the class codes of the classes you want and type stop to stop.')
while True:
    response = input('Class code: ')
    if response == 'done':
        break
    classes.append(response)

username = input('Username: ')
password = input('Password: ')

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)    
#login section
driver.get("http://www.my.fsu.edu")
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_id('fsu-login-button').click()
while True:
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[1]/ul/li[2]/a/div'))).click()
    except:
        print('Invalid username or password.')
        username = input('Username: ')
        password = input('Password: ')
        user = driver.find_element_by_id('username')
        user.clear()
        user.send_keys(username)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_id('fsu-login-button').click()
        continue
    else:
        break


#Click on student center
wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/div/div[3]/div[1]/div/div[1]/div[2]/div/a/img'))).click()

#Choose spring 2019
iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME,'iframe')))
driver.switch_to.frame(iframe)
time.sleep(2)
wait.until(EC.element_to_be_clickable((By.ID,'SSR_DUMMY_RECV1$sels$1$$0'))).click()
wait.until(EC.element_to_be_clickable((By.ID,'DERIVED_SSS_SCT_SSR_PB_GO'))).click()

#370,1816,1842
#Searches for the class nbr to add to your cart ADD AN OPTION TO make sure if class isn't repeated
for classnbr in classes:
    wait.until(EC.presence_of_element_located((By.ID,'DERIVED_REGFRM1_CLASS_NBR'))).send_keys(classnbr)
    wait.until(EC.element_to_be_clickable((By.ID,'DERIVED_REGFRM1_SSR_PB_ADDTOLIST2$9$'))).click()
    #Click on next to add to cart
    wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/div[5]/table/tbody/tr/td/div/table/tbody/tr[9]/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td[3]/div/a'))).click()

while True:
    #click on proceed step 2 or 3
    try:
        wait.until(EC.element_to_be_clickable((By.ID, 'win0divDERIVED_REGFRM1_LINK_ADD_ENRL$82$'))).click()
        #click finish enrolling
        wait.until(EC.element_to_be_clickable((By.ID, 'win0divDERIVED_REGFRM1_SSR_PB_SUBMIT'))).click()
        #click add another class
        wait.until(EC.element_to_be_clickable((By.ID, 'win0divDERIVED_REGFRM1_SSR_LINK_STARTOVER'))).click()
    except:
        break

