from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


username = ''
password = ''
# get the driver file path
driver_path = ('/Applications/chromedriver')
driver = webdriver.Chrome(driver_path)
driver.get("https://foreupsoftware.com/index.php/booking/20232/4102#/teetimes")

# very helpful link for css syntax
#public = driver.find_element_by_link_text('Oso Creek Public Tee Times')
public = driver.find_element_by_class_name('btn-primary')
public.click()

today = driver.find_element_by_class_name('.active')
print(today.text)
# TODO Check earliest time on upcoming Sunday

# TODO Select it

# TODO Add login credentials and card and select book

print('start')
#time.sleep(60)
print('end')
#driver.close()
