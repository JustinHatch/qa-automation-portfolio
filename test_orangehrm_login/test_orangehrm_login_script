import re
from playwright.sync_api import Page, expect


def test_login_to_orangehrm(page: Page):
    # Go to login page
    page.goto("https://opensource-demo.orangehrmlive.com/")
    expect(page).to_have_title(re.compile("OrangeHRM"))

    # Fill username and password
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")

    # Click login
    page.get_by_role("button", name="Login").click()

    # Verify successful login by checking for the dashboard
    expect(page.locator("h6")).to_contain_text("Dashboard")
