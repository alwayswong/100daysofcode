from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# this class is a way to use Enter and other non-mark keys, any key on the keyboard can be replicated like shift or enter

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# this class is a way to use Enter and other non-mark keys, any key on the keyboard can be replicated like shift or enter

chrome_driver_path = "/Applications/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://orteil.dashnet.org/cookieclicker/")


# sign in to a website
cookie = driver.find_element_by_id("bigCookie")
five_min = time.time() + 60

while True:
    cookie.click()

    if time.time() > five_min:
        break


