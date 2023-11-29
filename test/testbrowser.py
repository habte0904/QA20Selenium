import time

from selenium import webdriver

from src.pages.homepage import homepage
from src.pages.shoppage import shoppage
from src.resource.data import data

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# used to read data from fixture
d = data()


# call homepage by creating homepage object
hp = homepage(driver)
time.sleep(2)
hp.getName().send_keys(d.username)
time.sleep(2)
hp.getEmail().send_keys(d.email)
time.sleep(2)
hp.getPassword().send_keys(d.password)
time.sleep(2)


# SHOP PAGE MOVE
shop = shoppage(driver)
shop.getShopNav()
time.sleep(3)

