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

url = "https://www.coinbase.com/ru/"
driver = webdriver.Chrome(executable_path=r"C:\Users\Админ\Desktop\ITEA\Python Pro\automatization\chromedriver\chromedriver.exe",
                           options=options)
driver.get(url)
time.sleep(2)

list_button = driver.find_element(By.CSS_SELECTOR, "#root > div.Layout__Container-tuminz-0.fEqNcg > header > div > div.MobileNav__MenuToggleWrapper-sc-1dz0vq9-3.jFbRQb > div")
list_button.click()
time.sleep(2)

escape_button = driver.find_element(By.CSS_SELECTOR, "#root > div.CookieBannerContent__Container-sc-1kwlvwg-6.gICreR > div.CookieBannerContent__CTA-sc-1kwlvwg-3.jbjozz > button.Button-sc-1l1z0u6-0.iaBuWF")
escape_button.click()
time.sleep(2)

sign_in = driver.find_element(By.CSS_SELECTOR, "#global-nav-mobile-dropdown > div.MobileMenu__ButtonWrapper-prdh9l-6.hWmowb > span:nth-child(2) > button")
sign_in.click()
time.sleep(2)

cookie_button = driver.find_element(By.CSS_SELECTOR, "#root > div > div.b1oya23n > div > div > button")
cookie_button.click()
time.sleep(2)

input_email = driver.find_element(By.CSS_SELECTOR, "#Email")
input_email.click()
input_email.send_keys('illiakravchenko804@gmail.com')
time.sleep(2)

button_input_email = driver.find_element(By.CSS_SELECTOR, "#root > div > div.cds-flex-f1g67tkn.cds-center-ca5ylan.cds-column-ci8mx7v.cds-space-between-s1vbz1.cds-background-b85wjan.cds-2-_rro7jr.cds-2-_1gzxkm.cds-10-_t4vl43 > div > div > div > div > form > div.cds-flex-f1g67tkn.cds-column-ci8mx7v.cds-2-_1xqs9y8.cds-3-_9w3lns > ul > li > button")
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
WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > div > div > div > div > div > div.Flex-l69ttv-0.FullScreenLayout__Layout-sc-1tmcond-0.fjlpfW.deaJcH > div > div.cds-flex-f1g67tkn.cds-center-ca5ylan.cds-column-ci8mx7v.cds-background-b85wjan.cds-hidden-h1op4l4w.cds-compact-cy3f2yl.cds-bordered-b17mbjy1.cds-3-_64wlqa > div > div > div:nth-child(1) > div > div > div > div.SelectList__Select-sc-16qxoki-8.iwBWeq > div.SelectList__Selector-sc-16qxoki-10.iRJpyz > div"))).click()
if select_item == 'Croatia':
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div/div/div/div[3]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div[2]/div[57]/div'))).click() #Croatia
elif select_item == 'Serbia':
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div/div/div/div[3]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div[2]/div[189]/div'))).click() #Serbia

input_phone_number = driver.find_element(By.CSS_SELECTOR, "#AddPhoneNumberForm_phoneNumberFieldID")
input_phone_number.click()
input_phone_number.send_keys("953762542")
time.sleep(2)

button_input_phone = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div > div > div > div.Flex-l69ttv-0.FullScreenLayout__Layout-sc-1tmcond-0.fjlpfW.deaJcH > div > div.cds-flex-f1g67tkn.cds-center-ca5ylan.cds-column-ci8mx7v.cds-background-b85wjan.cds-hidden-h1op4l4w.cds-compact-cy3f2yl.cds-bordered-b17mbjy1.cds-3-_64wlqa > div > div > button")
button_input_phone.click()
time.sleep(2)

att = 0
while att < 3:
    time.sleep(60)
    resend_button = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div > div > div > div.Flex-l69ttv-0.FullScreenLayout__Layout-sc-1tmcond-0.fjlpfW.deaJcH > div > div.cds-flex-f1g67tkn.cds-center-ca5ylan.cds-column-ci8mx7v.cds-background-b85wjan.cds-hidden-h1op4l4w.cds-compact-cy3f2yl.cds-bordered-b17mbjy1.cds-3-_64wlqa > div > div > div > form > div.Flex-l69ttv-0.VerifyPhoneNumberForm__ActionsContainer-u4m8sa-4.cKNnNO.kxmSCJ > div.Flex-l69ttv-0.erJaoG > span > a")
    resend_button.click()
    time.sleep(2)
    att += 1

driver.close()
driver.quit()