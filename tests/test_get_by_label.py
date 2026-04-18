import pytest
from playwright.sync_api import Page, expect
from pages.playwright_page import PlaywrightPracticePage


@pytest.fixture
def app(page: Page):
    app = PlaywrightPracticePage(page)
    app.open()
    return app


def test_email(app):
    email = app.label.email()

    email.fill("a@b.com")
    expect(email).to_have_value("a@b.com")


def test_age(app):
    age = app.label.age()

    age.fill("30")
    expect(age).to_have_value("30")


def test_shipping_default(app):
    standard = app.label.shipping_standard()
    express = app.label.shipping_express()

    expect(standard).not_to_be_checked()
    expect(express).not_to_be_checked()


def test_shipping_selection(app):
    standard = app.label.shipping_standard()
    express = app.label.shipping_express()

    standard.check()
    expect(standard).to_be_checked()

    express.check()
    expect(express).to_be_checked()
    expect(standard).not_to_be_checked()


def test_shipping_title(app):
    expect(app.label.shipping_title()).to_contain_text("Shipping Method")