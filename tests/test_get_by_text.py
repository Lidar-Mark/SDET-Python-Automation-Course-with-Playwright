import pytest
from playwright.sync_api import Page, expect
from utils.logger import get_logger

log = get_logger(__name__)

BASE_URL = "https://testautomationpractice.blogspot.com/p/playwrightpractice.html"


@pytest.fixture
def page_loaded(page: Page):
    page.goto(BASE_URL)
    return page


@pytest.fixture
def text_section(page_loaded: Page):
    return page_loaded.locator("#text-locators")


def test_paragraph_highlight(text_section):
    log.info("Paragraph highlight test")

    para = text_section.get_by_text(
        "This paragraph contains some important",
        exact=False,
    )

    expect(para.locator("strong")).to_have_text("important")


def test_paragraph_colored_span(text_section):
    log.info("Colored span test")

    para = text_section.get_by_text("Another paragraph with", exact=False)

    span = para.locator("span")

    expect(span).to_have_css("color", "rgb(255, 0, 0)")


@pytest.mark.parametrize("text", ["List item 1", "List item 2"])
def test_list_items(text_section, text):
    log.info(f"List item test: {text}")

    item = text_section.locator("li", has_text=text)

    expect(item).to_be_visible()


def test_submit_button_behavior(page_loaded: Page):
    log.info("Submit button behavior test")

    card = page_loaded.locator(".card")

    submit = card.get_by_role("button", name="Submit Form")

    expect(submit).to_be_enabled()

    submit.click()

    result = card.locator("p").filter(has_text="Click the button above to")

    expect(result).to_be_visible()