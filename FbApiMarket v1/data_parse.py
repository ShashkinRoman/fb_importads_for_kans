from selenium import webdriver
import os
from time import sleep
from dotenv import load_dotenv
load_dotenv()

# def w_xpath(*args):
#     return WebDriverWait(driver(), 10).until(
#         EC.presence_of_element_located((By.XPATH, *args)))
#
# def w_id(*args):
#     return WebDriverWait(driver(), 10).until(
#         EC.presence_of_element_located((By.ID, *args)))

driver = webdriver.Chrome(os.getenv('chromedriver'))
driver.get("https://www.facebook.com/ads/manager/accounts/")
# search and input login
login = driver.find_element_by_id('email')
# login.click()
login.send_keys(os.getenv('login'))
# search and input pass
password = driver.find_element_by_id('pass')
password.send_keys(os.getenv('pass'))
# search and click button login
login_button = driver.find_element_by_id('loginbutton')
login_button.click()
sleep(5)
driver.get(os.getenv('url_ads_account'))
# select yesterday
sum = driver.find_element_by_xpath('//*[@id="ads_pe_container"]/div[2]/div[3]/div[2]/div[1]/div[3]/div/div/div/div/div/div/div/div/div[1]/div[6]/div/div/div[1]/div/div[3]/table/tbody/tr/td[5]/div/div/div/span[1]')
print(sum.text)
summa = sum.text[0:-2]
final_sum = summa.replace(' ', '')
driver.close()
