import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_api_vs_ui_user_data():
    # 1. API call
    api_user = requests.get("https://jsonplaceholder.typicode.com/users/1").json()
    expected_name = api_user["name"]
    expected_email = api_user["email"]

    # 2. UI load
    driver = webdriver.Chrome()
    driver.get("file:///C:/Users/Cristi/Desktop/git_excercise/learning-journal/day29/ui_mock/user.html")

    ui_name = driver.find_element(By.ID, "name").text
    ui_email = driver.find_element(By.ID, "email").text

    # 3. Validation
    assert ui_name == expected_name
    assert ui_email == expected_email

    driver.quit()
