from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from locators import AuthorizationLocators
from locators import NavigationLocators

def test_go_to_constructor():
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

        driver.find_element(By.XPATH, NavigationLocators.CONSTRUCTOR_BUTTON).click()

        time.sleep(2)

    finally:
        driver.quit()

def test_go_to_logo():
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

        driver.find_element(By.XPATH, NavigationLocators.LOGO).click()

        time.sleep(2)

    finally:
        driver.quit()
