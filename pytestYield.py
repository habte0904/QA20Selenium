import pytest
from selenium import webdriver


@pytest.yield_fixture()
def setup():
    print("Before method")
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    print(driver.title)
    yield
    print("After method")
    driver.close()


def testM1(setup):
    print("Hello world")


def testM2():
    print("welcome to craft class")
