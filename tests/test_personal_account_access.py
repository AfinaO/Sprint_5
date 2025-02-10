from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_personal_account_access():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    try:

        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, '//*[@id="root"]/div/header/nav/a/p').click()

        time.sleep(2)

    finally:
        driver.quit()