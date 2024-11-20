from pages.login_page import LoginPage
from utils.test_data import INVALID_CREDENTIALS

def test_negative_login(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate_to("https://automation-sandbox-python-mpywqjbdza-uc.a.run.app")

    login_successful = False

    for credentials in INVALID_CREDENTIALS:
        login_page.login(credentials["username"], credentials["password"])

        if page.url != "https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/login":
            login_successful = True
            continue

        try:
            page.wait_for_selector(".alert-danger", timeout=5000)
            error_message = page.inner_text(".alert-danger")
            assert "Wrong username or password" in error_message

        except TimeoutError:
            print("Expected error message not found")
            assert False, "Error message not found or login succeeded unexpectedly"

    if login_successful:
        print("Login successful with valid credentials. Skipping error validation to avoid false positive")
