import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkbox1 = driver.find_element(By.XPATH,  "//input[@id='checkBoxOption1']")
checkbox2 = driver.find_element(By.XPATH, "//input[@id='checkBoxOption2']")
checkbox3 = driver.find_element(By.XPATH, "//input[@id='checkBoxOption3']")

print(checkbox1.is_selected())
print(checkbox2.is_selected())
print(checkbox3.is_selected())

# select
checkbox1.click()
time.sleep(2)
checkbox2.click()
time.sleep(2)
checkbox3.click()
time.sleep(2)

print("After selected!")
print(checkbox1.is_selected())
print(checkbox2.is_selected())
print(checkbox3.is_selected())

# unselect
checkbox1.click()
time.sleep(2)
checkbox2.click()
time.sleep(2)
checkbox3.click()
time.sleep(2)

print("After unselected!")
print(checkbox1.is_selected())
print(checkbox2.is_selected())
print(checkbox3.is_selected())


