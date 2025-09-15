import pytest
from playwright.sync_api import Page, expect


@pytest.mark.playwright
def test_fill_practice_form(page: Page):
    # Go to the Practice Form page
    page.goto("https://demoqa.com/automation-practice-form")
    print("✅ Opened Practice Form page.")

    # Fill in the form fields
    page.fill("#firstName", "John")
    page.fill("#lastName", "Doe")
    page.fill("#userEmail", "john.doe@example.com")
    page.locator('label[for="gender-radio-1"]').click()
    page.fill("#userNumber", "1234567890")

    # Scroll and submit the form
    page.locator("#submit").scroll_into_view_if_needed()
    page.locator("#submit").click()

    # Assert success modal appears
    modal_title = page.locator("#example-modal-sizes-title-lg")
    expect(modal_title).to_have_text("Thanks for submitting the form")
    print("✅ Form submitted successfully.")
