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

url = "https://www.rappi.com.mx/login/phone"
driver = webdriver.Chrome(executable_path=r"C:\Users\Админ\Desktop\ITEA\Python Pro\automatization\chromedriver\chromedriver.exe",
                           options=options)
driver.get(url)
time.sleep(2)

input_phone_number = driver.find_element(By.CSS_SELECTOR, "#__next > div > div.css-1ef0ro2 > div > div.css-1ofqig9 > div > div > input")
input_phone_number.click()
input_phone_number.send_keys("7291222797")
time.sleep(2)

button_sms = driver.find_element(By.CSS_SELECTOR, "#__next > div > div.css-1ef0ro2 > div.chakra-stack.css-6j4m52 > button.chakra-button.css-fw1ipa")
button_sms.click()
time.sleep(2)

try:
    att = 0
    while att < 3:
        time.sleep(60)
        resend_button = driver.find_element(By.CSS_SELECTOR, "#__next > div > div.css-9w3ugv > div > div.css-0 > button")
        resend_button.click()
        resend_button = driver.find_element(By.CSS_SELECTOR, "#chakra-modal-\:r7q\: > footer > div > button.chakra-button.css-cvayf2")
        resend_button.click()
        time.sleep(2)
        att += 1
except:
    pass
finally:
    driver.close()
    driver.quit()