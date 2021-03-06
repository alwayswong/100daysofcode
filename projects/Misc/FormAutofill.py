from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# this class is a way to use Enter and other non-mark keys, any key on the keyboard can be replicated like shift or enter

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# this class is a way to use Enter and other non-mark keys, any key on the keyboard can be replicated like shift or enter

chrome_driver_path = "/Applications/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")

# sign in to a website
first = driver.find_element_by_name("fName")
first.send_keys("Tom")

last = driver.find_element_by_name("lName")
last.send_keys("Adams")

email = driver.find_element_by_name("email")
email.send_keys("ta@gmail.com")
email.send_keys((Keys.ENTER))
#driver.close()





# chrome_driver_path = "/Applications/chromedriver"
# driver = webdriver.Chrome(chrome_driver_path)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# #count = driver.find_element_by_id('articlecount')
# count = driver.find_element_by_css_selector('#articlecount a')
# #count.click()
# #print(count.text)
# everything = driver.find_element_by_link_text("The arts")
# #everything.click() -- click allows you to click on whatever element you just found
#
# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys((Keys.ENTER))
#driver.close()