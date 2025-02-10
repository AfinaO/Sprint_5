from selenium import webdriver
from selenium.webdriver.common.by import By
from tests.locators import RegistrationPageLocators
import time

def test_successful_registration():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    try:
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(By.CSS_SELECTOR, RegistrationPageLocators.NAME_FIELD).send_keys("Ольга")
        driver.find_element(By.CSS_SELECTOR, RegistrationPageLocators.EMAIL_FIELD).send_keys("olgaprihodko18999@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, RegistrationPageLocators.PASSWORD_FIELD).send_keys("123456")
        driver.find_element(By.CSS_SELECTOR, RegistrationPageLocators.SUBMIT_BUTTON).click()

        time.sleep(2)

    finally:
        driver.quit()


def test_registration_error_for_invalid_password():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    try:
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(By.CSS_SELECTOR, RegistrationPageLocators.NAME_FIELD).send_keys("Ольга")
        driver.find_element(By.CSS_SELECTOR, RegistrationPageLocators.EMAIL_FIELD).send_keys("olgaprihodko18999@yandex.ru")
        driver.find_element(By.CSS_SELECTOR, RegistrationPageLocators.PASSWORD_FIELD).send_keys("123")
        driver.find_element(By.CSS_SELECTOR, RegistrationPageLocators.SUBMIT_BUTTON).click()

        error_message = driver.find_element(By.CSS_SELECTOR, RegistrationPageLocators.ERROR_MESSAGE_PASSWORD)
        assert error_message.is_displayed(), "Ошибка: сообщение об ошибке не отображается"

        time.sleep(2)

    finally:
        driver.quit()