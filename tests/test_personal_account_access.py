import pytest
from selenium.webdriver.common.by import By
from constants import Links
from locators import AuthorizationLocators


@pytest.mark.parametrize('run_driver', [Links.main_link], indirect=True)
def test_personal_account_access(driver, run_driver):
    driver.find_element(By.XPATH, AuthorizationLocators.PERSONAL_ACCOUNT_BUTTON).click()
