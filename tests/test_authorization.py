from selenium import webdriver
from locators import AuthorizationLocators
from selenium.webdriver.common.by import By
import time

def test_login_button():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    try:
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, AuthorizationLocators.LOGIN_BUTTON).click()

        time.sleep(2)

        driver.find_element(By.XPATH, AuthorizationLocators.EMAIL_FIELD).send_keys("olgaprihodko18999@yandex.ru")
        driver.find_element(By.XPATH, AuthorizationLocators.PASSWORD_FIELD).send_keys("123456")
        driver.find_element(By.XPATH, AuthorizationLocators.ENTER_BUTTON).click()

        time.sleep(2)

    finally:
        driver.quit()


def test_personal_account_button():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    try:
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, AuthorizationLocators.PERSONAL_ACCOUNT_BUTTON).click()

        time.sleep(2)

        driver.find_element(By.XPATH, AuthorizationLocators.EMAIL_FIELD).send_keys("olgaprihodko18999@yandex.ru")
        driver.find_element(By.XPATH, AuthorizationLocators.PASSWORD_FIELD).send_keys("123456")
        driver.find_element(By.XPATH, AuthorizationLocators.ENTER_BUTTON).click()

        time.sleep(2)

    finally:
        driver.quit()


def test_registration_button():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    try:
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(By.XPATH, AuthorizationLocators.REGISTER_BUTTON).click()

        time.sleep(2)

        driver.find_element(By.XPATH, AuthorizationLocators.EMAIL_FIELD).send_keys("olgaprihodko18999@yandex.ru")
        driver.find_element(By.XPATH, AuthorizationLocators.PASSWORD_FIELD).send_keys("123456")
        driver.find_element(By.XPATH, AuthorizationLocators.ENTER_BUTTON).click()

    finally:
        driver.quit()


def test_password_recovery_button():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    try:
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        driver.find_element(By.XPATH, AuthorizationLocators.RECOVERY_BUTTON).click()

        time.sleep(2)

        driver.find_element(By.XPATH, AuthorizationLocators.EMAIL_FIELD).send_keys("olgaprihodko18999@yandex.ru")
        driver.find_element(By.XPATH, AuthorizationLocators.PASSWORD_FIELD).send_keys("123456")
        driver.find_element(By.XPATH, AuthorizationLocators.ENTER_BUTTON).click()

        time.sleep(2)

    finally:
        driver.quit()