from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Find username field
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("student")

    # Find password field
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Password123")

    # Click login
    login_button = driver.find_element(By.ID, "submit")
    login_button.click()

    time.sleep(2)  # wait for page load

    # Assertion
    expected_url = "https://practicetestautomation.com/logged-in-successfully/"
    assert driver.current_url == expected_url

    driver.quit()

def test_invalid_password():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.ID, "username").send_keys("student")
    driver.find_element(By.ID, "password").send_keys("WrongPass")
    driver.find_element(By.ID, "submit").click()

    time.sleep(2)

    error = driver.find_element(By.ID, "error").text
    assert error == "Your password is invalid!"

    driver.quit()

