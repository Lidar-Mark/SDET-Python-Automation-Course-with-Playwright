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
def label_section(page_loaded: Page):
    return page_loaded.locator("#label-locators")


def test_email_input(label_section):
    log.info("Email input test")

    email = label_section.get_by_label("Email Address")

    email.fill("a@b.com")

    expect(email).to_have_value("a@b.com")


def test_age_input(label_section):
    log.info("Age input test")

    age = label_section.get_by_label("Age")

    age.fill("30")

    expect(age).to_have_value("30")


def test_shipping_radio_default_state(label_section):
    log.info("Shipping radio default state test")

    standard = label_section.locator("input[value='standard']")
    express = label_section.locator("input[value='express']")

    expect(standard).not_to_be_checked()
    expect(express).not_to_be_checked()


def test_shipping_radio_selection(label_section):
    log.info("Shipping radio selection test")

    standard = label_section.locator("input[value='standard']")
    express = label_section.locator("input[value='express']")

    standard.check()
    expect(standard).to_be_checked()
    expect(express).not_to_be_checked()

    express.check()
    expect(express).to_be_checked()
    expect(standard).not_to_be_checked()


def test_shipping_fieldset_visible(label_section):
    log.info("Shipping fieldset visibility test")

    expect(label_section.get_by_text("Shipping Method")).to_be_visible()