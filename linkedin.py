import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import Select

useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83')
options.add_argument("--lang=EN")

url = "https://www.linkedin.com/psettings/phone/add?li_theme=light&openInMobileMode=true"
driver = webdriver.Chrome(executable_path=r"C:\Users\Админ\Desktop\ITEA\Python Pro\automatization\chromedriver\chromedriver.exe",
                           options=options)
driver.get(url)
time.sleep(2)

sign_in_button = driver.find_element(By.CSS_SELECTOR, "body > div.page.page--is-mercado-theme-enabled > main > p.main__sign-in-container > a")
sign_in_button.click()
time.sleep(2)

input_email = driver.find_element(By.CSS_SELECTOR, "#username")
input_email.click()
input_email.send_keys("illiakravchenko804@gmail.com")
time.sleep(2)

input_pass = driver.find_element(By.CSS_SELECTOR, "#password")
input_pass.click()
input_pass.send_keys("Zwer.190")
time.sleep(2)

sign_in_button = driver.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button")
sign_in_button.click()
time.sleep(5)

country = "Croatia"
select_country = Select(driver.find_element(By.CSS_SELECTOR, '#country-select'))
select_country.select_by_visible_text(country)
time.sleep(2)

phone_number = driver.find_element(By.CSS_SELECTOR, "#add-phone-number")
phone_number.click()
phone_number.send_keys("953784989")
time.sleep(2)

password = driver.find_element(By.CSS_SELECTOR, "#enter-password")
password.click()
password.send_keys("Zwer.190")
time.sleep(2)

send_code = driver.find_element(By.CSS_SELECTOR, "#phone-add-content > form > button")
send_code.click()
time.sleep(2000)

att = 0
while att < 2:
    time.sleep(60)
    cancel_button = driver.find_element(By.CSS_SELECTOR, '#pagekey-psettings-add-phone-number-from-mobile > div > section > form > div > button')
    cancel_button.click()
    time.sleep(2)
    resend_button = driver.find_element(By.CSS_SELECTOR, '#phone-add-content > form > button')
    resend_button.click()
    time.sleep(2)
    att += 1

driver.close()
driver.quit()