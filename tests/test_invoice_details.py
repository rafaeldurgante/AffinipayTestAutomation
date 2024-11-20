from pages.invoice_page import InvoicePage
from pages.login_page import LoginPage
from utils.test_data import VALID_CREDENTIALS, INVOICE_DETAILS

def test_invoice_details(browser):
    page = browser.new_page()
    login_page = LoginPage(page)

    login_page.navigate_to("https://automation-sandbox-python-mpywqjbdza-uc.a.run.app")
    login_page.login(VALID_CREDENTIALS["username"], VALID_CREDENTIALS["password"])

    with page.expect_popup() as new_page_info:
        page.locator("a[href='/invoice/0']").click()

    new_page = new_page_info.value
    new_page.wait_for_url("https://automation-sandbox-python-mpywqjbdza-uc.a.run.app/invoice/0", timeout=30000)

    xpath_selector = "xpath=/html/body/section/div/header/h2"
    new_page.wait_for_selector(xpath_selector, state="visible", timeout=30000)
    assert new_page.is_visible(xpath_selector), "Page title is not visible!"

    invoice_page = InvoicePage(new_page)
    invoice_page.validate_invoice_details(INVOICE_DETAILS)

    print("All invoice details validated successfully.")
