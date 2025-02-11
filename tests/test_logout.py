import pytest
from selenium.webdriver.common.by import By

from locators import AuthorizationLocators
from constants import Links
from constants import Data

@pytest.mark.parametrize('run_driver', [Links.main_link], indirect=True)
def test_logout(driver, run_driver):
    driver.find_element(By.XPATH, AuthorizationLocators.PERSONAL_ACCOUNT_BUTTON).click()

    driver.find_element(By.XPATH, AuthorizationLocators.EMAIL_FIELD).send_keys(Data.email)
    driver.find_element(By.XPATH, AuthorizationLocators.PASSWORD_FIELD).send_keys(Data.password)
    driver.find_element(By.XPATH, AuthorizationLocators.ENTER_BUTTON).click()

    driver.find_element(By.XPATH, AuthorizationLocators.PERSONAL_ACCOUNT_BUTTON).click()

    driver.find_element(By.XPATH, AuthorizationLocators.LOGOUT_BUTTON).click()
