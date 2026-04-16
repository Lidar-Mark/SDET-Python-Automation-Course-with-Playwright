"""
POM = Page Object Model.

get_by_alt_text() is a method in Playwright that allows you to locate an element based on its alt attribute. 
                  The alt attribute is commonly used in HTML to provide alternative text for images, which is displayed if the image cannot be loaded.

get_by_text() is a method in Playwright that allows you to locate an element based on its visible text content.

"""




from playwright.sync_api import Page, expect


URL: str = "https://demoqa.com/"

def test_get_by_alt_test(page: Page):

    page.goto(URL)
    page.wait_for_timeout(5000)
    alt = page.get_by_alt_text("Selenium Online Training")
    expect(alt).to_be_visible()


def test_get_by_text(page: Page):
    page.goto(URL)
    page.wait_for_timeout(5000)
    text = page.get_by_text(" TOOLSQA.COM | ALL RIGHTS RESERVED.")
    expect(text).to_be_visible()

