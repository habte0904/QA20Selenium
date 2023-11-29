import pytest

@pytest.fixture()
def setup():
    print("This method is executed before every method")

def testMethod1(setup):
    print("from method 1")

def testMethod2(setup):
    print("from method 2")

