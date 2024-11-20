from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str):
        """Navigates to the specified URL."""
        self.page.goto(url)

    def fill_field(self, selector: str, value: str):
        """
        Fills a field in the form. Waits for the element to be visible before filling.
        Allows using 'name' as an alternative selector if necessary.
        """
        self.wait_for_element(selector)
        self.page.fill(selector, value)

    def click(self, selector: str):
        """
        Clicks on an element. Waits for the element to be clickable before performing the action.
        """
        self.wait_for_element(selector)
        self.page.click(selector)

    def get_text(self, selector: str) -> str:
        """
        Retrieves the inner text of an element.
        """
        self.wait_for_element(selector)
        return self.page.inner_text(selector)

    def wait_for_element(self, selector: str, timeout: int = 10000):
        """
        Waits until the element is available in the DOM.
        """
        self.page.wait_for_selector(selector, state="visible", timeout=20000)
