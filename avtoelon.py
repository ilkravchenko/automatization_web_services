import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83')
options.add_argument("--lang=EN")

url = "https://avtoelon.uz/"
driver = webdriver.Chrome(executable_path=r"C:\Users\Админ\Desktop\ITEA\Python Pro\automatization\chromedriver\chromedriver.exe",
                           options=options)
driver.get(url)
time.sleep(2)

sign_up = driver.find_element(By.CSS_SELECTOR, "body > div.site-container > div.site-container__primary > header > div > div > div > div.navigation-header__secondary > ul > li:nth-child(2) > a > span")
sign_up.click()
time.sleep(2)

input_number = driver.find_element(By.CSS_SELECTOR, "#login")
input_number.click()
input_number.send_keys("385953762542")
time.sleep(2)

button_input_number = driver.find_element(By.CSS_SELECTOR, "#signin-form > div.form-item.buttons-group > div > button")
button_input_number.click()
time.sleep(2)

att = 0
while att<3:
    time.sleep(60)
    resend_button = driver.find_element(By.CSS_SELECTOR, "#signin-form > div.form-item.buttons-group > span")
    resend_button.click()
    time.sleep(2)
    att += 1

driver.close()
driver.quit()