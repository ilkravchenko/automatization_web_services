import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36,gzip(gfe)')
options.add_argument("--lang=EN")

url = "https://www.amazon.com/ap/profile/mobilephone?appActionToken=kAy2SQoNJuKy0l0Lx89x0R4IzlYj3D&appAction=CHANGE_MOBILE_PHONE&openid.return_to=ape%3AaHR0cHM6Ly93d3cuYW1hem9uLmNvbS95b3VyLWFjY291bnQ%3D&prevRID=ape%3AS1ZTVjlONzFSMEU1V0g1M0NKUDE%3D&email=ape%3AaWxsaWFrcmF2Y2hlbmtvODA0QGdtYWlsLmNvbQ%3D%3D&workflowState=eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.InUFoz1_Bn8vM9zxg0dGdCfTTUs2ALbOIK_ZJ0a5f7uF4sEpt52D1Q.3Q95ss6E9bDOOVsQ.aL4_4JA9iS2CRIWKUZQ2Vkh63gGTSlhM-w0f5bmjgOwI2PCQJUJ-kyQ4Z7isTTFrl07NpQ2XKY-d1DgE3OoC5wN1hFdCSOeR9Qi6jopbntawm3yAuIvfNhWdWto-OsPi_zpPPb0bMkQfpiFYV4RCaQsxvMIsnYQIQ62t8WHnji5XqmkcU3tQqSki_g1UcKXOUeJCifyarScUWZqwMWi80-V_1ogSAgsYUJejGd-Nedr8-pXalcc2osOC7VW-V04Yq7-_i120hQTjdpLpVkdWhFMERkUTS5gjwICkWq7wsUkjRTEIGTP_Pw.Qxcjw-DR_Q-pUDLkEhMHmg&referringAppAction=CNEP"
driver = webdriver.Chrome(executable_path=r"C:\Users\Админ\Desktop\ITEA\Python Pro\automatization\chromedriver\chromedriver.exe",
                           options=options)
driver.get(url)
time.sleep(2)

input_email = driver.find_element(By.CSS_SELECTOR, "#ap_email")
input_email.click()
input_email.send_keys("illiakravchenko804@gmail.com")
input_email.send_keys(Keys.ENTER)
time.sleep(2)

input_email = driver.find_element(By.CSS_SELECTOR, "#ap_password")
input_email.click()
input_email.send_keys("Zwer.190")
input_email.send_keys(Keys.ENTER)
time.sleep(2)

select_item = 'Croatia'
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#a-autoid-0-announce"))).click()
if select_item == 'Croatia':
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="auth-country-picker_48"]'))).click() #Croatia
    time.sleep(2)
elif select_item == 'Serbia':
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="auth-country-picker_173"]'))).click() #Serbia
    time.sleep(2)

input_phone_number = driver.find_element(By.CSS_SELECTOR, "#ap_phone_number")
input_phone_number.click()
input_phone_number.send_keys("953481019")
input_phone_number.send_keys(Keys.ENTER)
time.sleep(2)

okay_button = driver.find_element(By.CSS_SELECTOR, "#auth-verification-ok-announce")
okay_button.click()
time.sleep(2)

att = 0
while att < 3:
    time.sleep(60)
    resend_button = driver.find_element(By.CSS_SELECTOR, "#auth-resend-code-link")
    resend_button.click()
    time.sleep(2)
    att += 1

driver.close()
driver.quit()