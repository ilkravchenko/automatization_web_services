import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

useragent = UserAgent()
option = webdriver.ChromeOptions()
option.add_argument(f'user-agent={useragent.opera}')
option.add_argument("--lang=EN")

url = 'https://www.instagram.com/accounts/emailsignup/?hl=en'
driver = webdriver.Chrome(executable_path=r'C:\Users\Админ\Desktop\ITEA\Python Pro\automatization\chromedriver\chromedriver.exe',options=option)
driver.get(url=url)

time.sleep(2)

phone_number = driver.find_element(By.CSS_SELECTOR,"#react-root > section > main > div > div > div:nth-child(1) > div.P8adC > form > div:nth-child(4) > div > label > input")
phone_number.click()
phone_number.send_keys('92' + '3324971478')
time.sleep(2)

full_name = driver.find_element(By.CSS_SELECTOR,"#react-root > section > main > div > div > div:nth-child(1) > div.P8adC > form > div:nth-child(5) > div > label > input")
full_name.click()
full_name.send_keys('Illiakakjasf')
time.sleep(2)

user_name = driver.find_element(By.CSS_SELECTOR,"#react-root > section > main > div > div > div:nth-child(1) > div.P8adC > form > div:nth-child(6) > div > label > input")
user_name.click()
user_name.send_keys('Zwer_111111')
time.sleep(2)

password = driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[6]/div/label/input')
password.click()
password.send_keys('Zwer.190')
time.sleep(2)

sign_button = driver.find_element(By.CSS_SELECTOR,"#react-root > section > main > div > div > div:nth-child(1) > div.P8adC > form > div:nth-child(9) > div").click()
time.sleep(5)

select_year = Select(driver.find_element(By.CSS_SELECTOR, '#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_.acqo5._4EzTm.bkEs3.DhRcB > div > div > span > span:nth-child(3) > select'))
select_year.select_by_visible_text('2000')

next_button = driver.find_element(By.CSS_SELECTOR,"#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_.acqo5._4EzTm.lC6p0.g6RW6").click()
time.sleep(2)

e = 0
while e < 3:
    time.sleep(60)
    resend_button = driver.find_element(By.CSS_SELECTOR,'#react-root > section > main > div > div > div:nth-child(1) > div > div > div > div.xUUM0 > button:nth-child(2)')
    resend_button.click()
    time.sleep(2)
    e += 1


driver.close()
driver.quit()