from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "submit")
        self.error_message = (By.ID, "error")

    def open(self):
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def enter_username(self, username):
        self.type(self.username_input, username)

    def enter_password(self, password):
        self.type(self.password_input, password)

    def click_login(self):
        self.click(self.login_button)

    def get_error(self):
        return self.wait_for_visibility(self.error_message).text

