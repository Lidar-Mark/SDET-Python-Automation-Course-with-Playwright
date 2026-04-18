from playwright.sync_api import Page


class PlaywrightPracticePage:
    URL = "https://testautomationpractice.blogspot.com/p/playwrightpractice.html#"

    def __init__(self, page: Page):
        self.page = page
        self.text = TextSection(page)
        self.role = RoleSection(page)
        self.label = LabelSection(page)


    def open(self):
        self.page.goto(self.URL)


class RoleSection:
    def __init__(self, page: Page):
        self.root = page.locator("#role-locators")

    def buttons(self):
        return {
            "primary": self.root.get_by_role("button", name="Primary Action"),
            "toggle": self.root.get_by_role("button", name="Toggle Button"),
            "div": self.root.get_by_role("button", name="Div with button role"),
        }

    def username(self):
        return self.root.get_by_role("textbox", name="Username")

    def accept_terms(self):
        return self.root.get_by_role("checkbox", name="Accept terms")

    def navigation(self):
        return {
            "home": self.root.get_by_role("link", name="Home"),
            "products": self.root.get_by_role("link", name="Products"),
            "contact": self.root.get_by_role("link", name="Contact"),
        }

    def alert(self):
        return self.root.get_by_role("alert")


class TextSection:
    def __init__(self, page: Page):
        self.root = page.locator("#text-locators")

    def paragraph(self, text):
        return self.root.get_by_text(text, exact=False)

    def list_item(self, text):
        return self.root.locator("li", has_text=text)

    def paragraph_span(self, text):
        return self.paragraph(text).locator("span")

    def paragraph_strong(self, text):
        return self.paragraph(text).locator("strong")
    

class LabelSection:
    def __init__(self, page: Page):
        self.root = page.locator("#label-locators")

    def email(self):
        return self.root.get_by_label("Email Address")

    def age(self):
        return self.root.get_by_label("Age")

    def shipping_standard(self):
        return self.root.locator("input[value='standard']")

    def shipping_express(self):
        return self.root.locator("input[value='express']")

    def shipping_title(self):
        return self.root.get_by_text("Shipping Method")