# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path


@pytest.fixture
def driver():
    # Optional: configure Chrome options (e.g. headless in CI)
    options = Options()
    # options.add_argument("--headless=new")  # uncomment for headless

    # Option A: use chromedriver in PATH (Chrome 115+ with Selenium Manager)
    driver = webdriver.Chrome(options=options)

    # Option B (if needed): point to local driver explicitly
    # project_root = Path(__file__).parent
    # driver_path = project_root / "drivers" / "chromedriver.exe"
    # driver = webdriver.Chrome(executable_path=str(driver_path), options=options)

    driver.maximize_window()
    yield driver      # give the driver to the test

    # Teardown
    driver.quit()
