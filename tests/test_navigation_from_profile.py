from selenium.webdriver.common.by import By
import pytest
from locators import AuthorizationLocators
from locators import NavigationLocators
from constants import Data
from constants import Links

@pytest.mark.parametrize('run_driver', [Links.main_link], indirect=True)
def test_go_to_constructor(driver, run_driver):
    driver.find_element(By.XPATH, AuthorizationLocators.PERSONAL_ACCOUNT_BUTTON).click()

    driver.find_element(By.XPATH, AuthorizationLocators.EMAIL_FIELD).send_keys(Data.email)
    driver.find_element(By.XPATH, AuthorizationLocators.PASSWORD_FIELD).send_keys(Data.password)
    driver.find_element(By.XPATH, AuthorizationLocators.ENTER_BUTTON).click()

    driver.find_element(By.XPATH, AuthorizationLocators.PERSONAL_ACCOUNT_BUTTON).click()

    driver.find_element(By.XPATH, NavigationLocators.CONSTRUCTOR_BUTTON).click()


@pytest.mark.parametrize('run_driver', [Links.main_link], indirect=True)
def test_go_to_logo(driver, run_driver):
    driver.find_element(By.XPATH, AuthorizationLocators.PERSONAL_ACCOUNT_BUTTON).click()

    driver.find_element(By.XPATH, AuthorizationLocators.EMAIL_FIELD).send_keys(Data.email)
    driver.find_element(By.XPATH, AuthorizationLocators.PASSWORD_FIELD).send_keys(Data.password)
    driver.find_element(By.XPATH, AuthorizationLocators.ENTER_BUTTON).click()

    driver.find_element(By.XPATH, AuthorizationLocators.PERSONAL_ACCOUNT_BUTTON).click()

    driver.find_element(By.XPATH, NavigationLocators.LOGO).click()