from selenium import webdriver
import os
from time import sleep
from dotenv import load_dotenv
load_dotenv()
import datetime
from datetime import datetime, timedelta

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

def yesterday_url():
    today = datetime.now()
    yesterday = today + timedelta(days=-1)
    if yesterday.day < 10:
        day = '0' + str(yesterday.day)
    else:
        day = str(yesterday.day)
    if yesterday.month < 10:
        month = '0' + str(yesterday.month)
    else:
        month = str(yesterday.month)
    if yesterday.day < 10:
        day_now = '0' + str(today.day)
    else:
        day_now = str(yesterday.day)
    if yesterday.month < 10:
        month_now = '0' + str(today.month)
    else:
        month_now = str(today.month)
    yesterday_for_url = day + '-' + month + '-' + str(yesterday.year) + '_' + day_now + '-' + month_now + '-' + str(today.year)
    url = os.getenv('url_first_part') + yesterday_for_url +os.getenv('url_second_part')
    return str(url)

driver.get(yesterday_url())
# get and format data
sum = driver.find_elements_by_class_name('_1876')
print(sum[2].text)
summa = sum[2].text[0:-2]
final_sum = summa.replace(' ', '')
driver.close()
