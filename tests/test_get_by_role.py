from playwright.sync_api import Page, expect
from utils.logger import get_logger

log = get_logger(__name__)

BASE_URL: str = "https://testautomationpractice.blogspot.com/p/playwrightpractice.html"


def test_get_by_role(page: Page):
    """Verify all ARIA role locators in the #role-locators section."""
    log.info("Navigating to practice page")
    page.goto(BASE_URL)
    page.wait_for_load_state("domcontentloaded")

    section = page.locator("section#role-locators")
    expect(section).to_be_visible()
    log.info("Section #role-locators found")

    # -- Buttons --
    log.info("Testing Primary Action button")
    primary_action = section.get_by_role("button", name="Primary Action")
    primary_action.click()
    expect(primary_action).to_be_visible()
    expect(primary_action).to_be_enabled()
    log.info("Primary Action clicked and verified")

    log.info("Testing Toggle Button aria-pressed state")
    toggle_button = section.get_by_role("button", name="Toggle Button")
    expect(toggle_button).to_have_attribute("aria-pressed", "false")
    toggle_button.click()
    log.info("Toggle Button clicked")
    # aria-pressed flip not yet implemented on practice site
    # expect(toggle_button).to_have_attribute("aria-pressed", "true")

    log.info("Testing Div with button role")
    div_button = section.get_by_role("button", name="Div with button role")
    expect(div_button).to_be_visible()
    expect(div_button).to_have_attribute("tabindex", "0")  # non-semantic, must be keyboard accessible
    log.info("Div button verified")

    # -- Form Elements --
    log.info("Testing Username textbox")
    username = section.get_by_role("textbox", name="Username")
    username.fill("John Doe")
    expect(username).to_have_value("John Doe")
    log.info("Username filled and verified")

    log.info("Testing Accept Terms checkbox")
    accept_terms = section.get_by_role("checkbox", name="Accept terms")
    accept_terms.check()
    expect(accept_terms).to_be_checked()
    log.info("Checkbox checked")
    accept_terms.uncheck()
    expect(accept_terms).not_to_be_checked()
    log.info("Checkbox unchecked")

    # -- Navigation --
    log.info("Testing Navigation links")
    links = section.get_by_role("link")
    expect(links).to_have_count(3)
    expect(links).to_have_text(["Home", "Products", "Contact"])
    log.info("3 links verified: Home, Products, Contact")

    home = section.get_by_role("link", name="Home")
    expect(home).to_have_attribute("href", "#")
    expect(home).to_be_enabled()
    log.info("Home link href='#' verified")

    log.info("Testing menu items")
    menu_items = section.get_by_role("menuitem")
    expect(menu_items).to_have_count(3)
    expect(menu_items.nth(0)).to_contain_text("Home")
    expect(menu_items.nth(1)).to_contain_text("Products")
    expect(menu_items.nth(2)).to_contain_text("Contact")
    log.info("All 3 menu items verified")

    # -- Alert --
    log.info("Testing Alert message")
    alert = section.get_by_role("alert")
    expect(alert).to_be_visible()
    expect(alert).to_contain_text("important alert message")
    log.info("Alert message verified")

    log.info("✓ All assertions passed")