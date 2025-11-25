from pathlib import Path
from selenium.webdriver.common.by import By
from utils.api_client import APIClient


client = APIClient()


def test_api_vs_ui_user_data(driver):
    # 1. API: get user #1
    api_response = client.get("/users/1")
    assert api_response.status_code == 200

    api_user = api_response.json()
    expected_name = api_user["name"]
    expected_email = api_user["email"]

    # 2. UI: open local mock page
    project_root = Path(__file__).parent.parent
    html_path = project_root / "ui_mock" / "user.html"
    driver.get(f"file:///{html_path.as_posix()}")

    ui_name = driver.find_element(By.ID, "name").text
    ui_email = driver.find_element(By.ID, "email").text

    # 3. Consistency checks
    assert ui_name == expected_name, f"Name mismatch: UI='{ui_name}', API='{expected_name}'"
    assert ui_email == expected_email, f"Email mismatch: UI='{ui_email}', API='{expected_email}'"
