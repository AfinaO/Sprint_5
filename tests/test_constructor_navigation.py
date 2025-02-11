import pytest
from selenium.webdriver.common.by import By
from locators import NavigationLocators
from constants import Links

@pytest.mark.parametrize('run_driver', [Links.main_link], indirect=True)
def test_go_to_bulki(driver, run_driver):
    driver.find_element(By.XPATH, NavigationLocators.FILLINGS_BUTTON).click()
    driver.find_element(By.XPATH, NavigationLocators.BULKI_BUTTON).click()


@pytest.mark.parametrize('run_driver', [Links.main_link], indirect=True)
def test_go_to_sauses(driver, run_driver):
    driver.find_element(By.XPATH, NavigationLocators.SAUSES_BUTTON).click()


@pytest.mark.parametrize('run_driver', [Links.main_link], indirect=True)
def test_go_to_fillings(driver, run_driver):
    driver.find_element(By.XPATH, NavigationLocators.FILLINGS_BUTTON).click()
