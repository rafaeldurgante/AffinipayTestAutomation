from pages.login_page import LoginPage
from utils.test_data import VALID_CREDENTIALS

def test_login_success(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    login_page.navigate_to("https://automation-sandbox-python-mpywqjbdza-uc.a.run.app")
    login_page.login(VALID_CREDENTIALS["username"], VALID_CREDENTIALS["password"])

    title = page.title()
    print("Page title after login:", title)

    assert "Automation Example" in title
    login_page.validate_logout_button()