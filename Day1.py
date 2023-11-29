# import webdriver
import time
from selenium import webdriver


# create webdriver object
driver = webdriver.Chrome()

# visit website
driver.get("https://www.google.com/")

# read title of the page
print(driver.title)
time.sleep(2)

# To check url
print(driver.current_url)
time.sleep(1)


# page source
print(driver.page_source)
time.sleep(1)


driver.close()


