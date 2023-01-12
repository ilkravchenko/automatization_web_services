import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent

useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83')
options.add_argument("--proxy-server=193.251.151.82:3128")
options.add_argument("--lang=EN")

url = "https://web.icq.com"
driver = webdriver.Chrome(executable_path=r"C:\Users\Админ\Desktop\ITEA\Python Pro\automatization\chromedriver\chromedriver.exe",
                           options=options)
driver.get(url)
time.sleep(5)

next_button = driver.find_element(By.CSS_SELECTOR, "#root > div > div > div.im-welcome-screen__box > div > button")
next_button.click()
time.sleep(2)

input_number = driver.find_element(By.CSS_SELECTOR, "#root > div > div.imAuthForm.im-auth-formwrap > div > form > div > input")
input_number.click()
input_number.clear()
input_number.send_keys("+385953784989")
time.sleep(2)

input_number_button = driver.find_element(By.CSS_SELECTOR, "#root > div > div.imAuthForm.im-auth-formwrap > div > form > button")
input_number_button.click()
time.sleep(2)

att = 0
while att<3:
    time.sleep(60)
    resend_button = driver.find_element(By.CSS_SELECTOR, "#root > div > div.imAuthForm.im-auth-formwrap > div > button")
    resend_button.click()
    time.sleep(2)
    att += 1

driver.close()
driver.quit()