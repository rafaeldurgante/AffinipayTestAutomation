from playwright.sync_api import Page

class InvoicePage:
    def __init__(self, page: Page):
        self.page = page

    def get_field_text(self, xpath):
        element = self.page.wait_for_selector(f"xpath={xpath}", state="visible", timeout=10000)
        text = element.text_content().strip()

        if ":" in text:
            text = text.split(": ", 1)[1]

        if "Invoice #" in text:
            text = text.split('Invoice #')[1].split()[0]

        return text


    def validate_invoice_details(self, expected_details: dict):
        """Validates the invoice details based on the provided dictionary."""
        # Map the XPath selectors to the fields.
        selectors = {
            "HotelName": "/html/body/section/div/h4",
            "InvoiceDate": "/html/body/section/div/ul/li[1]",
            "DueDate": "/html/body/section/div/ul/li[2]",
            "InvoiceNumber": "//h6[contains(text(),'Invoice #')]",
            "BookingCode": "/html/body/section/div/table[1]/tbody/tr[1]/td[2]",
            "CustomerDetails": "/html/body/section/div/div",
            "Room": "/html/body/section/div/table[1]/tbody/tr[2]/td[2]",
            "CheckIn": "/html/body/section/div/table[1]/tbody/tr[5]/td[2]",
            "CheckOut": "/html/body/section/div/table[1]/tbody/tr[6]/td[2]",
            "TotalStayCount": "/html/body/section/div/table[1]/tbody/tr[3]/td[2]",
            "TotalStayAmount": "/html/body/section/div/table[1]/tbody/tr[4]/td[2]",
            "DepositNow": "/html/body/section/div/table[2]/tbody/tr/td[1]",
            "Tax&VAT": "/html/body/section/div/table[2]/tbody/tr/td[2]",
            "TotalAmount": "/html/body/section/div/table[2]/tbody/tr/td[3]",
        }

        for key, expected_value in expected_details.items():
            xpath = selectors.get(key)
            if not xpath:
                raise KeyError(f"XPath to '{key}' not defined.")

            actual_value = self.get_field_text(xpath)
            assert actual_value == expected_value, (
                f"Validation Error of '{key}': Expected '{expected_value}', "
                f"but found '{actual_value}'."
            )
