import pytest
from selenium.webdriver.common.by import By
from tests.locators import RegistrationPageLocators
from constants import Data
from constants import Links


@pytest.mark.parametrize('run_driver', [Links.register_link], indirect=True)
def test_successful_registration(driver, run_driver):
   # driver.find_element(By.XPATH, RegistrationPageLocators.NAME1).send_keys(Data.username)
    driver.find_element(By.XPATH, RegistrationPageLocators.NAME_FIELD).send_keys(Data.username)
    driver.find_element(By.XPATH, RegistrationPageLocators.EMAIL_FIELD).send_keys(Data.email)
    driver.find_element(By.XPATH, RegistrationPageLocators.PASSWORD_FIELD).send_keys(Data.password)
    driver.find_element(By.XPATH, RegistrationPageLocators.SUBMIT_BUTTON).click()
  #  driver.find_element_by_id().send_keys()

@pytest.mark.parametrize('run_driver', [Links.register_link], indirect=True)
def test_registration_error_for_invalid_password(driver, run_driver):
    driver.find_element(By.XPATH, RegistrationPageLocators.NAME_FIELD).send_keys(Data.username)
    driver.find_element(By.XPATH, RegistrationPageLocators.EMAIL_FIELD).send_keys(Data.email)
    driver.find_element(By.XPATH, RegistrationPageLocators.PASSWORD_FIELD).send_keys(Data.incorrect_password)
    driver.find_element(By.XPATH, RegistrationPageLocators.SUBMIT_BUTTON).click()

    error_message = driver.find_element(By.XPATH, RegistrationPageLocators.ERROR_MESSAGE_PASSWORD)
    assert error_message.is_displayed(), Data.err_msg
