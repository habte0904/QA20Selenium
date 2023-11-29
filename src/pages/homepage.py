from selenium.webdriver.common.by import By


class homepage:
    def __init__(self, driver):
        self.driver = driver

    # RETURN NAME
    def getName(self):
        return self.driver.find_element(By.XPATH, "(//input[@name='name'])[1]")

    # RETURN EMAIL
    def getEmail(self):
        return self.driver.find_element(By.XPATH, "//input[@name='email']")

    # RETURN PASSWORD
    def getPassword(self):
        return self.driver.find_element(By.XPATH, "//input[@type='password']")

