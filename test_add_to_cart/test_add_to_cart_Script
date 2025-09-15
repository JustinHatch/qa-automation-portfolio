import pytest
import re
from playwright.sync_api import Page, expect


def test_add_product_to_cart(page: Page):
    # Step 1: Go to site
    page.goto("https://automationexercise.com")
    expect(page).to_have_title("Automation Exercise")

    # Step 2: Click 'Products'
    page.get_by_role("link", name="Products").click()
    expect(page).to_have_url(re.compile(".*products.*"))

    # Step 3: Hover over first product to reveal overlay
    page.wait_for_selector(".product-image-wrapper")
    product = page.locator(".product-image-wrapper").first
    product.hover()

    # Step 4: Click the visible Add to Cart button inside the overlay
    overlay_add_btn = product.locator(
        ".product-overlay .overlay-content a:has-text('Add to cart')")
    overlay_add_btn.click()

    # Step 5: Click 'View Cart'
    page.wait_for_selector("a:has-text('View Cart')")
    page.locator("a:has-text('View Cart')").click()

    # Step 6: Confirm cart page shows item
    expect(page).to_have_url(re.compile(".*view_cart.*"))
    expect(page.locator(".cart_description")).to_contain_text("Blue Top")

    print("✅ Product added to cart and verified in cart.")
