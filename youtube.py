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

url = "https://www.youtube.com/verify?pli=1&skip_registered_account_check=true"
driver = webdriver.Chrome(executable_path=r"C:\Users\Админ\Desktop\ITEA\Python Pro\automatization\chromedriver\chromedriver.exe",
                           options=options)
driver.get(url)
time.sleep(2000)

input_email = driver.find_element(By.CSS_SELECTOR, "#identifierId")
input_email.click()
input_email.send_keys('illiakravchenko804@gmail.com')
time.sleep(2)

button_input_email = driver.find_element(By.CSS_SELECTOR, "#identifierNext > div > button")
button_input_email.click()
time.sleep(2)

input_pass = driver.find_element(By.CSS_SELECTOR, "#Password")
input_pass.click()
input_pass.send_keys('Zwer.190')
time.sleep(2)

button_input_pass = driver.find_element(By.CSS_SELECTOR, "#root > div > div.cds-flex-f1g67tkn.cds-center-ca5ylan.cds-column-ci8mx7v.cds-space-between-s1vbz1.cds-background-b85wjan.cds-2-_rro7jr.cds-2-_1gzxkm.cds-10-_t4vl43 > div > div > div > div.cds-flex-f1g67tkn.cds-center-czxavit.cds-pill-pbuu10h.cds-bordered-b17mbjy1.cds-5-_h5hy70.cds-5-_7ojgr9.cds-5-_1w9a5m > form > div:nth-child(6) > button")
button_input_pass.click()
time.sleep(25)

select_item = 'Croatia'
WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#container > div.input-wrapper.style-scope.tp-yt-paper-input-container"))).click()
if select_item == 'Croatia':
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,'#contentWrapper > div > tp-yt-paper-listbox > tp-yt-paper-item.style-scope.ytv-input-select-renderer.iron-selected'))).click() #Croatia
elif select_item == 'Serbia':
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,'#contentWrapper > div > tp-yt-paper-listbox > tp-yt-paper-item:nth-child(190)'))).click() #Serbia

input_phone_number = driver.find_element(By.CSS_SELECTOR, "#input-1 > input")
input_phone_number.click()
input_phone_number.send_keys("953762542")
time.sleep(2)

button_input_phone = driver.find_element(By.CSS_SELECTOR, "#send-code-button > yt-button-renderer")
button_input_phone.click()
time.sleep(2)

att = 0
while att < 3:
    time.sleep(60)
    back_button = driver.find_element(By.XPATH, "//*[@id='button']")
    back_button.click()
    resend_button = driver.find_element(By.XPATH, "#button")
    resend_button.click()
    time.sleep(2)
    att += 1

driver.close()
driver.quit()