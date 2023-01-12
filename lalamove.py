import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36,gzip(gfe)')
options.add_argument("--lang=EN")

url = "https://web.lalamove.com/register"
driver = webdriver.Chrome(executable_path=r"C:\Users\Админ\Desktop\ITEA\Python Pro\automatization\chromedriver\chromedriver.exe",
                           options=options)
driver.get(url)
time.sleep(2)

select_item = 'Croatia'
WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#downshift-0-input"))).click()
if select_item == 'Croatia':
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="downshift-0-item-6"]'))).click() #Croatia


name = driver.find_element(By.CSS_SELECTOR,"#🚐 > div:nth-child(1) > div > div.Container-sc-1y5phmm-1.dwZejX > div.Card-sc-1y0eaxi-0.Container__ResponsiveCard-sc-1y5phmm-0.kqkTTe.iKwxNs > form > div:nth-child(1) > div:nth-child(1) > div > input")
name.click()
name.send_keys('asdaf')
time.sleep(2)

surname = driver.find_element(By.CSS_SELECTOR,"#🚐 > div:nth-child(1) > div > div.Container-sc-1y5phmm-1.dwZejX > div.Card-sc-1y0eaxi-0.Container__ResponsiveCard-sc-1y5phmm-0.kqkTTe.iKwxNs > form > div:nth-child(1) > div:nth-child(2) > div > input")
surname.click()
surname.send_keys('asdasd')
time.sleep(2)

password = driver.find_element(By.XPATH,'#🚐 > div:nth-child(1) > div > div.Container-sc-1y5phmm-1.dwZejX > div.Card-sc-1y0eaxi-0.Container__ResponsiveCard-sc-1y5phmm-0.kqkTTe.iKwxNs > form > div:nth-child(4) > div > div > input')
password.click()
password.send_keys('Zwer.190')
time.sleep(2)

input_email = driver.find_element(By.CSS_SELECTOR, "#🚐 > div:nth-child(1) > div > div.Container-sc-1y5phmm-1.dwZejX > div.Card-sc-1y0eaxi-0.Container__ResponsiveCard-sc-1y5phmm-0.kqkTTe.iKwxNs > form > div:nth-child(2) > div > div > input")
input_email.click()
input_email.send_keys('illiakravchenko804@gmail.com')
time.sleep(2)

input_phone_number = driver.find_element(By.CSS_SELECTOR, "#🚐 > div:nth-child(1) > div > div.Container-sc-1y5phmm-1.dwZejX > div.Card-sc-1y0eaxi-0.Container__ResponsiveCard-sc-1y5phmm-0.kqkTTe.iKwxNs > form > div:nth-child(3) > div > div.Input__Wrapper-sc-30lp73-0.kPCqhR.PhoneInput__StyledInput-sc-1t229ov-2.gSSEmE > div > input")
input_phone_number.click()
input_phone_number.send_keys("9953153534")
time.sleep(2)

next_button = driver.find_element(By.CSS_SELECTOR,"#🚐 > div:nth-child(1) > div > div.Container-sc-1y5phmm-1.dwZejX > div.Card-sc-1y0eaxi-0.Container__ResponsiveCard-sc-1y5phmm-0.kqkTTe.iKwxNs > form > button").click()
time.sleep(2)

e = 0
while e < 3:
    time.sleep(60)
    resend_button = driver.find_element(By.CSS_SELECTOR,'#🚐 > div:nth-child(1) > div > div.Container-sc-1y5phmm-1.dwZejX > div.Card-sc-1y0eaxi-0.Container__ResponsiveCard-sc-1y5phmm-0.styles__StyledResponsiveCard-sc-19ck6sl-0.kqkTTe.iKwxNs.jlfEWM > button.style__Base-sc-1jbzg3h-0.Button__StyledButton-sc-7kpwz0-3.dtqTlb.eSbRUe.ResendCountdown__StyledButton-sc-1cx28l6-0.eTchUi')
    resend_button.click()
    time.sleep(2)
    e += 1

driver.close()
driver.quit()