import pytest
from pages.login_page import LoginPage
from pages.secure_page import SecurePage

valid_login_data = [
    ("student", "Password123"),
]

@pytest.mark.parametrize("username,password", valid_login_data)
def test_valid_login_param(driver, username, password):
    login = LoginPage(driver)
    login.open()
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    secure = SecurePage(driver)
    secure.wait_until_logged_in()

    assert "logged-in-successfully" in secure.current_url()



invalid_login_data = [
    ("student", "WrongPass", "Your password is invalid!"),
    ("wronguser", "Password123", "Your username is invalid!"),
    ("", "Password123", "Your username is invalid!"),
    ("student", "", "Your password is invalid!"),
]

@pytest.mark.parametrize("username,password,expected_error", invalid_login_data)
def test_invalid_login_scenarios(driver, username, password, expected_error):
    login = LoginPage(driver)
    login.open()

    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    error = login.get_error().strip()
    assert expected_error in error


