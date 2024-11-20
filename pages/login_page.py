from pages.base_page import BasePage

class LoginPage(BasePage):
    def login(self, username, password):
        self.wait_for_element("input[name='username']", timeout=20000)
        self.fill_field("input[name='username']", username)

        self.wait_for_element("input[name='password']", timeout=20000)
        self.fill_field("input[name='password']", password)

        self.wait_for_element("button[type='submit']", timeout=20000)
        self.click("button[type='submit']")

    def validate_logout_button(self):
        logout_button = self.page.locator("a.btn.btn-outline-info[href='/logout']")
        assert logout_button.is_visible(), "Logout button is not visible after login."
        print("Logout button is visible on the page.")