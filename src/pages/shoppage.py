from selenium.webdriver.common.by import By


class shoppage:
    def __init__(self, driver):
        self.driver = driver

    # CLICK SHOP NAVIAGITION
    def getShopNav(self):
        self.driver.find_element(By.LINK_TEXT, "Shop").click()
