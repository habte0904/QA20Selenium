import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# =============================
# = dynamic dropdown ==========
# =============================

dy = driver.find_element(By.XPATH, "//input[@id='autocomplete']")
dy.send_keys("eth")


dy.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
dy.send_keys(Keys.ARROW_DOWN)
time.sleep(2)
dy.send_keys(Keys.ENTER)

time.sleep(2)






