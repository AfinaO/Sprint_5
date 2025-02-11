import pytest
from selenium import webdriver


@pytest.fixture()
def get_driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://stellarburgers.nomoreparties.site/")
    return driver
  #  yield

 #   driver.implicitly_wait(10)
 #   driver.quit()

@pytest.fixture()
def close_driver(get_driver):
    get_driver.implicitly_wait(10)
    get_driver.quit()