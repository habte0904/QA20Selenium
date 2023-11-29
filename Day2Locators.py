import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

# Id locator
# driver.find_element(By.ID, 'email').send_keys("qa20@gmail.com")
# driver.find_element(By.CLASS_NAME, 'inputtext').send_keys("HelloQA20@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("cssSelector@gmail.com")
driver.find_element(By.XPATH, "//input[@id='email']").send_keys('xpath@gmail.com')
time.sleep(2)
driver.find_element(By.ID, 'pass').send_keys("qa20321")
time.sleep(2)


# Name Locator
# driver.find_element(By.NAME, 'login').click()

# driver.find_element(By.LINK_TEXT, 'Forgot password?').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'Forgot').click()
time.sleep(3)
