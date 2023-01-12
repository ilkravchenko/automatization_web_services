import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36,gzip(gfe)')
options.add_argument("--lang=EN")

url = "https://member.lazada.com.ph/user/register"
driver = webdriver.Chrome(executable_path=r"C:\Users\Админ\Desktop\ITEA\Python Pro\automatization\chromedriver\chromedriver.exe",
                           options=options)
driver.get(url)
time.sleep(2)

input_phone_number = driver.find_element(By.CSS_SELECTOR, "#container > div > div:nth-child(2) > div > div.mod-login-col1 > div.mod-input.mod-login-input-phone.mod-input-phone > input[type=text]")
input_phone_number.click()
input_phone_number.send_keys("+385953481019")
time.sleep(2)

slider = driver.find_element(By.XPATH,'//*[@id="nc_2_n1z"]')
move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(400, 0).perform()
time.sleep(2)

e = 0
while e < 3:
    time.sleep(60)
    resend_button = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[2]/div/div[1]/div[2]/div[2]/button')
    resend_button.click()
    slider = driver.find_element(By.XPATH, '//*[@id="nc_4_n1z"]')
    move = ActionChains(driver)
    move.click_and_hold(slider).move_by_offset(400, 0).perform()
    time.sleep(2)
    e += 1

driver.close()
driver.quit()