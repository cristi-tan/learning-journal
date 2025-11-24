from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")

response = requests.get("https://api.com/user/1")
assert response.status_code == 200

def test_login():
    assert login("admin", "1234") == True
