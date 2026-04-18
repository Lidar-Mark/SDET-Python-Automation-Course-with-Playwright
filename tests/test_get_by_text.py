import pytest
from playwright.sync_api import Page, expect
from pages.playwright_page import PlaywrightPracticePage
from utils.logger import get_logger

log = get_logger(__name__)


@pytest.fixture
def app(page: Page):
    app = PlaywrightPracticePage(page)
    app.open()
    return app


def test_paragraph_highlight(app):
    log.info("Paragraph highlight test")

    para = app.text.paragraph("This paragraph contains some important")

    expect(para.locator("strong")).to_have_text("important")


def test_paragraph_colored_span(app):
    log.info("Colored span test")

    span = app.text.paragraph_span("Another paragraph with")

    expect(span).to_have_css("color", "rgb(255, 0, 0)")


@pytest.mark.parametrize("text", ["List item 1", "List item 2"])
def test_list_items(app, text):
    log.info(f"List item test: {text}")

    item = app.text.list_item(text)

    expect(item).to_be_visible()