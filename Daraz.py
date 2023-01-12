import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from selenium.webdriver.common.action_chains import ActionChains


useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent={useragent.opera}')
options.add_argument("--lang=EN")

url = 'https://member.daraz.pk/user/register?spm=a2a0e.login_signup.0.0.7e607d68ONgC3L&redirect=https%3A%2F%2Fwww.daraz.pk%2F'
driver = webdriver.Chrome(executable_path=r'C:\Users\Админ\Desktop\ITEA\Python Pro\automatization\chromedriver\chromedriver.exe')
driver.get(url=url)

phone_field = driver.find_element(By.CSS_SELECTOR,'#container > div > div:nth-child(2) > div > div.mod-login-col1 > div.mod-input.mod-login-input-phone.mod-input-phone > input[type=text]',)
phone_field.click()
phone_field.send_keys("+" + '380' + '995327348')
time.sleep(1)

slider = driver.find_element(By.XPATH,'//*[@id="nc_2_n1z"]')
move = ActionChains(driver)
move.click_and_hold(slider).move_by_offset(400, 0).perform()
time.sleep(2)

e = 0
while e < 3:
    time.sleep(60)
    resend_button = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[2]/div/div[1]/div[2]/div[2]/button')
    resend_button.click()
    time.sleep(2)
    e += 1

driver.close()
driver.quit()