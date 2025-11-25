from pages.login_page import LoginPage

def test_invalid_password(driver):
    login = LoginPage(driver)
    login.open()

    login.enter_username("student")
    login.enter_password("WrongPass")
    login.click_login()

    error = login.get_error()

    # Better assertion
    assert "invalid" in error.lower(), f"Error message incorrect: {error}"