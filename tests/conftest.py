import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver


@pytest.fixture()
def run_driver(driver, request):
    driver.get(request.param)

    yield

    driver.quit()
