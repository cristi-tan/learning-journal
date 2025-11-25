from pages.login_page import LoginPage
from pages.secure_page import SecurePage
from utils.logger import get_logger

logger = get_logger("TestLogin")

def test_valid_login(driver):
    logger.info("Starting test_valid_login")
    login = LoginPage(driver)

    login.open()
    login.enter_username("student")
    login.enter_password("Password123")
    login.click_login()

    secure = SecurePage(driver)
    secure.wait_until_logged_in()

    assert "logged-in-successfully" in secure.current_url()
    logger.info("test_valid_login passed")



def test_invalid_password(driver):
    login = LoginPage(driver)
    login.open()

    login.enter_username("student")
    login.enter_password("WrongPass")
    login.click_login()

    error = login.get_error()

    # Better assertion
    assert "invalid" in error.lower(), f"Error message incorrect: {error}"

