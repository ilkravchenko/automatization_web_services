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

input_phone_number = driver.find_element(By.CSS_SELECTOR, "#main > div > div.vtexOX > div > div > div > form > div > div.yXry6s > div.qvdx4B > div.yup5K8 > input")
input_phone_number.click()
input_phone_number.send_keys("7291222797")
time.sleep(2)

button_input_phone = driver.find_element(By.CSS_SELECTOR, "#main > div > div.vtexOX > div > div > div > form > div > div.yXry6s > button")
button_input_phone.click()
time.sleep(2)

button_method = driver.find_element(By.CSS_SELECTOR, "#modal > aside > div._68lNMv.undefined > div > div.Kp5gjr.zfb33O > button:nth-child(2)")
button_method.click()
time.sleep(2)

button_sms = driver.find_element(By.CSS_SELECTOR, "#main > div > div.vtexOX > div > div > div > div.J1i6cp > div.yXry6s.B-fiUo > div > button:nth-child(3)")
button_sms.click()
time.sleep(2)

try:
    att = 0
    while att < 3:
        time.sleep(60)
        resend_button = driver.find_element(By.CSS_SELECTOR, "#main > div > div.vtexOX > div > div > div > form > div > div.yXry6s.B-fiUo > div.P2H6vF > div:nth-child(2) > span:nth-child(1)")
        resend_button.click()
        time.sleep(2)
        att += 1
except:
    pass
finally:
    driver.close()
    driver.quit()