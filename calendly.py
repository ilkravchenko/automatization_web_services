import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={useragent.opera}')
options.add_argument('--disable-blink-features=AutomationControlled')

url = "https://calendly.com/account/settings/workflows"
driver = webdriver.Chrome(executable_path=r"C:\Users\Админ\Desktop\ITEA\Python Pro\automatization\chromedriver\chromedriver.exe",
                           options=options)
driver.get(url)
time.sleep(2)

cookie = driver.find_element(By.CSS_SELECTOR,"#onetrust-close-btn-container > button")
cookie.click()
time.sleep(2)

log_with_google = driver.find_element(By.CSS_SELECTOR, "#root > div > div.Y9VK6TSaKxGk2HX8DX3f.fPcXQvT1mrcA0YISZThr.FmA70NpsbAuaR_c37ncK._wIGHnjRkVD7C1F2RbKS.EAKh2foN0IaULq3NRqLh.qfHxfuxD1MWHXDglESRI > div._2MSKEdrK9HjxfHdebKo.cMkVQH75VpPZg3Rq1L2p > button:nth-child(1)")
log_with_google.click()
time.sleep(1)

input_email = driver.find_element(By.CSS_SELECTOR, "#Email")
input_email.click()
input_email.send_keys("illiakravchenko804@gmail.com")
input_email.send_keys(Keys.ENTER)
time.sleep(1)

input_pass = driver.find_element(By.CSS_SELECTOR, '#password')
input_pass.click()
input_pass.send_keys("Zwer.115")
input_pass.send_keys(Keys.ENTER)
time.sleep(1)

country = 'Croatia'
WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#root > main > div._1Gob46WvdW3ASRPh5SW.ii4d7OZBTuUAmxoX2LYr > div > div > div.cTQqY2Q77_7dOQRbUFX8.mMwWorCmIx14YnikkJL9.Hfy1fqUpVb1P4k3AIPLF.NTKNPZdyyGs0vtjm_MeJ > div > div:nth-child(1) > div.a9JsocrG_UYbI4oDpR0c.d_H97DEvWRBcvOYVRkZa > div > div > div > div > div > div > div > div"))).click()
if country == 'Croatia':
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="iti-item-hr"]/div'))).click() #Croatia
elif country == 'Serbia':
    WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="iti-item-rs"]/div'))).click() #Serbia
time.sleep(1)

input_number = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/main/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div/div/div/div/input")
input_number.click()
input_number.send_keys("953481019")
time.sleep(1)

send_sms = driver.find_element(By.CSS_SELECTOR, "#root > main > div._1Gob46WvdW3ASRPh5SW.ii4d7OZBTuUAmxoX2LYr > div > div > div.cTQqY2Q77_7dOQRbUFX8.mMwWorCmIx14YnikkJL9.Hfy1fqUpVb1P4k3AIPLF.NTKNPZdyyGs0vtjm_MeJ > div > div:nth-child(1) > div.a9JsocrG_UYbI4oDpR0c.d_H97DEvWRBcvOYVRkZa > div > button")
send_sms.click()

att = 0
while att < 3:
    time.sleep(60)
    resend_button = driver.find_element(By.CSS_SELECTOR, "#root > main > div._1Gob46WvdW3ASRPh5SW.ii4d7OZBTuUAmxoX2LYr > div > div > div.cTQqY2Q77_7dOQRbUFX8.mMwWorCmIx14YnikkJL9.Hfy1fqUpVb1P4k3AIPLF.NTKNPZdyyGs0vtjm_MeJ > div > div:nth-child(1) > div.a9JsocrG_UYbI4oDpR0c.d_H97DEvWRBcvOYVRkZa > div.D77CDOpdnUeikFzZorcA.sJ1PYt9yiwyy_Yu_q_AG > button")
    resend_button.click()
    time.sleep(2)
    att += 1

driver.close()
driver.quit()