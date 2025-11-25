from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = get_logger(self.__class__.__name__)

    def wait_for_visibility(self, locator):
        self.logger.info(f"Waiting for visibility of element: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        self.logger.info(f"Waiting for element to be clickable: {locator}")
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.logger.info(f"Clicking on element: {locator}")
        self.wait_for_clickable(locator).click()

    def type(self, locator, text):
        self.logger.info(f"Typing into element {locator}: '{text}'")
        self.wait_for_visibility(locator).send_keys(text)

    def wait_for_url(self, text):
        self.logger.info(f"Waiting for URL to contain: '{text}'")
        return self.wait.until(EC.url_contains(text))
