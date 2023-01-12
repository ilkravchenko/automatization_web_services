import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

useragent = UserAgent()
option = webdriver.ChromeOptions()
option.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36,gzip(gfe)')
option.add_argument("--lang=EN")

url = 'https://account.samsung.com/membership/contents/phonenumber/authentication'
driver = webdriver.Chrome(executable_path=r'C:\Users\Админ\Desktop\ITEA\Python Pro\automatization\chromedriver\chromedriver.exe',
                          options=option)
driver.get(url=url)
time.sleep(2)

input_emil = driver.find_element(By.CSS_SELECTOR, "#iptLgnPlnID")
input_emil.click()
input_emil.send_keys("illiakravchenko804@gmail.com")
time.sleep(2)

next_step = driver.find_element(By.CSS_SELECTOR, '#signInButton')
next_step.click()
time.sleep(2)

password = driver.find_element(By.CSS_SELECTOR, "#iptLgnPlnPD")
password.click()
password.send_keys('Zwer.190')
password.send_keys(Keys.ENTER)
time.sleep(2)

if driver.find_element(By.CSS_SELECTOR, "#btnNotNow"):
    not_now_but = driver.find_element(By.CSS_SELECTOR, "#btnNotNow")
    not_now_but.click()
    time.sleep(2)
if driver.find_element(By.CSS_SELECTOR, "body > div.wrapper.ng-scope > main > div > div.under-content > div > button.one-cancel.one-button"):
    not_now_but2 = driver.find_element(By.CSS_SELECTOR, "body > div.wrapper.ng-scope > main > div > div.under-content > div > button.one-cancel.one-button")
    not_now_but2.click()
    time.sleep(5)

language = driver.find_element(By.CSS_SELECTOR, "#locale")
language.click()
time.sleep(2)

engl = driver.find_element(By.CSS_SELECTOR, "#en_GE")
engl.click()
time.sleep(2)

phone_number = driver.find_element(By.CSS_SELECTOR, "#two_step_tab")
phone_number.click()
time.sleep(2)

country = "Croatia (+385)"
select_year = Select(driver.find_element(By.CSS_SELECTOR, '#main > div > phonenumber-wrapper > secure-token-container > input-phonenumber > div > div.iam-forms > form > fieldset > div > select'))
select_year.select_by_visible_text(country)
time.sleep(2)

input_phone = driver.find_element(By.CSS_SELECTOR, "#phoneNumberInput")
input_phone.click()
input_phone.send_keys("953784989")
input_phone.send_keys(Keys.ENTER)
time.sleep(2)

att = 0
while att < 3:
    time.sleep(180)
    resend_button = driver.find_element(By.CSS_SELECTOR, "#main > div > phonenumber-wrapper > secure-token-container > input-phonenumber > div > div:nth-child(3) > form > fieldset > input-container > div > simple-button > div > button")
    resend_button.click()
    time.sleep(2)
    att += 1

driver.close()
driver.quit()