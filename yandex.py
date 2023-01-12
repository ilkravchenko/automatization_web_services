import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent

useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 OPR/89.0.4447.83')
options.add_argument("--lang=EN")

url = "https://passport.yandex.ru/auth/restore/login?retpath=https%3A%2F%2Fmusic.yandex.ru%2Fsettings%3Freqid%3D9670278261635931918939096279150089%26from-passport&ncrnd=934&origin=music_button-header"
driver = webdriver.Chrome(executable_path=r"C:\Users\Админ\Desktop\ITEA\Python Pro\automatization\chromedriver\chromedriver.exe",
                           options=options)
driver.get(url)
time.sleep(5)

lang_button = driver.find_element(By.CSS_SELECTOR, "#root > div > div.passp-page > footer > div > div.AuthFooter-mainBlock > span:nth-child(1) > span.Link.Link_pseudo.Link_view_default.AuthFooter-itemCap")
lang_button.click()
time.sleep(2)

eng_lang = driver.find_element(By.CSS_SELECTOR, "#root > div > div.passp-page > footer > div > div.AuthFooter-mainBlock > span:nth-child(1) > span.AuthFooter-langList.AuthFooter-langList_opened > ul > li:nth-child(1) > a")
eng_lang.click()
time.sleep(2)

input_number = driver.find_element(By.CSS_SELECTOR, "#passp-field-phone")
input_number.click()
input_number.send_keys(Keys.BACK_SPACE)
input_number.send_keys("380995327348")
time.sleep(2)

next_button = driver.find_element(By.CSS_SELECTOR, "#passp\:phone\:controls\:next")
next_button.click()
time.sleep(5)

att = 0
while att < 3:
    time.sleep(31)
    resend_button = driver.find_element(By.CSS_SELECTOR, "#UserEntryFlow > form > div > div.PhoneConfirmationCode-controls > button.Button2.Button2_size_l.Button2_view_default.Button2_width_max")
    resend_button.click()
    time.sleep(2)
    att += 1

driver.close()
driver.quit()