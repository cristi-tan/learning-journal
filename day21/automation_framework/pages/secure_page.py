from pages.base_page import BasePage

class SecurePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def current_url(self):
        return self.driver.current_url

    def wait_until_logged_in(self):
        self.wait_for_url("logged-in-successfully")

