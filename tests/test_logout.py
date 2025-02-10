from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from locators import AuthorizationLocators

def test_logout():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    try:
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, AuthorizationLocators.PERSONAL_ACCOUNT_BUTTON).click()

        time.sleep(2)

        driver.find_element(By.XPATH, AuthorizationLocators.EMAIL_FIELD).send_keys("olgaprihodko18999@yandex.ru")
        driver.find_element(By.XPATH, AuthorizationLocators.PASSWORD_FIELD).send_keys("123456")
        driver.find_element(By.XPATH, AuthorizationLocators.ENTER_BUTTON).click()

        driver.find_element(By.XPATH, AuthorizationLocators.PERSONAL_ACCOUNT_BUTTON).click()

        time.sleep(2)

        driver.find_element(By.XPATH, AuthorizationLocators.LOGOUT_BUTTON).click()

        time.sleep(2)

    finally:
        driver.quit()