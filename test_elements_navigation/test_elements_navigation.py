import pytest
from playwright.sync_api import Page, expect


def test_navigate_to_elements_section(page: Page):
    page.goto("https://demoqa.com/")
    print("🌐 Opened DemoQA homepage.")

    # Click on the "Elements" section
    page.get_by_text("Elements").click()
    print("📦 Clicked on 'Elements' section.")

    # Verify "Text Box" appears
    expect(page.get_by_text("Text Box")).to_be_visible()
    print("✅ 'Text Box' is visible on the Elements page.")
