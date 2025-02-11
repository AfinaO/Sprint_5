import pytest
from locators import AuthorizationLocators
from selenium.webdriver.common.by import By
from constants import Links
from constants import Data

@pytest.mark.parametrize('run_driver', [Links.main_link], indirect=True)
def test_login_button(driver, run_driver):
    driver.find_element(By.XPATH, AuthorizationLocators.LOGIN_BUTTON).click()

    driver.find_element(By.XPATH, AuthorizationLocators.EMAIL_FIELD).send_keys(Data.email)
    driver.find_element(By.XPATH, AuthorizationLocators.PASSWORD_FIELD).send_keys(Data.password)
    driver.find_element(By.XPATH, AuthorizationLocators.ENTER_BUTTON).click()


@pytest.mark.parametrize('run_driver', [Links.main_link], indirect=True)
def test_personal_account_button(driver, run_driver):
    driver.find_element(By.XPATH, AuthorizationLocators.PERSONAL_ACCOUNT_BUTTON).click()

    driver.find_element(By.XPATH, AuthorizationLocators.EMAIL_FIELD).send_keys(Data.email)
    driver.find_element(By.XPATH, AuthorizationLocators.PASSWORD_FIELD).send_keys(Data.password)
    driver.find_element(By.XPATH, AuthorizationLocators.ENTER_BUTTON).click()

@pytest.mark.parametrize('run_driver', [Links.register_link], indirect=True)
def test_registration_button(driver, run_driver):
    driver.find_element(By.XPATH, AuthorizationLocators.REGISTER_BUTTON).click()

    driver.find_element(By.XPATH, AuthorizationLocators.EMAIL_FIELD).send_keys(Data.email)
    driver.find_element(By.XPATH, AuthorizationLocators.PASSWORD_FIELD).send_keys(Data.password)
    driver.find_element(By.XPATH, AuthorizationLocators.ENTER_BUTTON).click()

@pytest.mark.parametrize('run_driver', [Links.forgot_link], indirect=True)
def test_password_recovery_button(driver, run_driver):
    driver.find_element(By.XPATH, AuthorizationLocators.RECOVERY_BUTTON).click()

    driver.find_element(By.XPATH, AuthorizationLocators.EMAIL_FIELD).send_keys(Data.email)
    driver.find_element(By.XPATH, AuthorizationLocators.PASSWORD_FIELD).send_keys(Data.password)
    driver.find_element(By.XPATH, AuthorizationLocators.ENTER_BUTTON).click()