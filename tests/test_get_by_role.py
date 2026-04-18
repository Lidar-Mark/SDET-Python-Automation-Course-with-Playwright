import pytest
from playwright.sync_api import Page, expect
from pages.playwright_page import PlaywrightPracticePage


@pytest.fixture
def app(page: Page):
    app = PlaywrightPracticePage(page)
    app.open()
    return app


def test_buttons(app):
    buttons = app.role.buttons()

    expect(buttons["primary"]).to_contain_text("Primary Action")
    expect(buttons["toggle"]).to_contain_text("Toggle Button")
    expect(buttons["div"]).to_contain_text("Div with button role")


def test_username(app):
    username = app.role.username()

    username.fill("John Doe")
    expect(username).to_have_value("John Doe")


def test_accept_terms(app):
    checkbox = app.role.accept_terms()

    checkbox.check()
    expect(checkbox).to_be_checked()

    checkbox.uncheck()
    expect(checkbox).not_to_be_checked()


def test_navigation(app):
    nav = app.role.navigation()

    expect(nav["home"]).to_have_attribute("href", "#")
    expect(nav["products"]).to_have_attribute("href", "#")
    expect(nav["contact"]).to_have_attribute("href", "#")


def test_alert(app):
    alert = app.role.alert()

    expect(alert).to_contain_text("important")