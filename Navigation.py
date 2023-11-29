import time

from selenium import webdriver

# visit rahul shetty academy page
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
time.sleep(2)


# visit google page
driver.get("https://www.google.com/")
print(driver.title)
time.sleep(2)

# navigate to rahul shetty page (back)
driver.back()
print(driver.title)
time.sleep(2)

# navigate to google page (forward)
driver.forward()
print(driver.title)
time.sleep(2)

