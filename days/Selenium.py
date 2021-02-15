from selenium import webdriver
# path to find our driver
chrome_driver_path = "/Applications/chromedriver"
# Chrome driver is a bridge to communicate Selenium code with Chrome browser
driver = webdriver.Chrome(chrome_driver_path)

# get opens a window
driver.get("https://www.python.org/")
# you can search with a ton of different methods including id,name,etc
#event-widget is the name of the class that we are selecting from
# time is the type of CSS that we want to look for within the class
times = driver.find_elements_by_css_selector('.event-widget time')
# you can add multiple filters at the end of the css selector find
names = driver.find_elements_by_css_selector('.event-widget li a')
events = {}
# you need to use a for loop to access the selenium elements
for n in range(len(times)):
    events[n] = {
        "time": times[n].text,
        "name": names[n].text
    }
print(events)
    #print(f'Event {index} is {time.text}')
driver.close()