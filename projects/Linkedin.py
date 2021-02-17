from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

username = 'blah'
password = 'blahblah'
num = '1234567890'
# get the driver file path
driver_path = ('/Applications/chromedriver')
driver = webdriver.Chrome(driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=92000001&keywords=python%20developer&location=Remote&sortBy=R")
signin = driver.find_element_by_xpath('/html/body/header/nav/div/a[2]').click()
#
time.sleep(3)

username_field = driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
print('username done')
password_field = driver.find_element_by_xpath('//*[@id="password"]').send_keys(password, Keys.ENTER)
print('pw done')

time.sleep(3)
apply = driver.find_element_by_css_selector('.jobs-s-apply').click()
time.sleep(3)

phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys('')
else:
    driver.close()

submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()