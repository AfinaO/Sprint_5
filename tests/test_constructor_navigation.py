from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#from locators import AuthorizationLocators
from locators import NavigationLocators

def test_go_to_bulki():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    try:
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, NavigationLocators.FILLINGS_BUTTON).click()

        time.sleep(2)

        driver.find_element(By.XPATH, NavigationLocators.BULKI_BUTTON).click()

        time.sleep(2)

    finally:
        driver.quit()

def test_go_to_sauses():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    try:
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, NavigationLocators.SAUSES_BUTTON).click()

        time.sleep(2)

    finally:
        driver.quit()


def test_go_to_fillings():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    try:
        driver.get("https://stellarburgers.nomoreparties.site/")

        driver.find_element(By.XPATH, NavigationLocators.FILLINGS_BUTTON).click()

        time.sleep(2)

    finally:
        driver.quit()