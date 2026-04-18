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
def role_section(page_loaded: Page):
    return page_loaded.locator("#role-locators")


def test_primary_action_button(role_section):
    log.info("Primary Action button test")

    btn = role_section.get_by_role("button", name="Primary Action")

    btn.click()
    expect(btn).to_be_visible()
    expect(btn).to_be_enabled()


def test_toggle_button(role_section):
    log.info("Toggle button test")

    toggle = role_section.get_by_role("button", name="Toggle Button")

    expect(toggle).to_have_attribute("aria-pressed", "false")

    toggle.click()

    # behavior not implemented on site
    expect(toggle).to_have_attribute("aria-pressed", "false")


def test_div_button(role_section):
    log.info("Div button test")

    div_btn = role_section.get_by_role("button", name="Div with button role")

    expect(div_btn).to_be_visible()
    expect(div_btn).to_have_attribute("tabindex", "0")


def test_username_input(role_section):
    log.info("Username input test")

    username = role_section.get_by_role("textbox", name="Username")

    username.fill("John Doe")

    expect(username).to_have_value("John Doe")


def test_checkbox(role_section):
    log.info("Checkbox test")

    checkbox = role_section.get_by_role("checkbox", name="Accept terms")

    checkbox.check()
    expect(checkbox).to_be_checked()

    checkbox.uncheck()
    expect(checkbox).not_to_be_checked()


@pytest.mark.parametrize(
    "name",
    ["Home", "Products", "Contact"],
)
def test_links_visible(role_section, name):
    log.info(f"Link visibility test: {name}")

    link = role_section.get_by_role("link", name=name)

    expect(link).to_be_visible()


def test_home_link(role_section):
    log.info("Home link href test")

    home = role_section.get_by_role("link", name="Home")

    expect(home).to_have_attribute("href", "#")
    expect(home).to_be_enabled()


def test_menu_items(role_section):
    log.info("Menu items test")

    items = role_section.get_by_role("menuitem")

    expect(items).to_have_count(3)

    for i, name in enumerate(["Home", "Products", "Contact"]):
        expect(items.nth(i)).to_contain_text(name)


def test_alert(role_section):
    log.info("Alert test")

    alert = role_section.get_by_role("alert")

    expect(alert).to_be_visible()
    expect(alert).to_contain_text("important alert message")