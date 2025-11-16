import pytest
import time
import os
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utilities.config_reader import ConfigReader

class TestSauceDemo:
    """My test suite for SauceDemo login and the product flow."""

    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        # Normal browser window size (standard desktop size)
        page.set_viewport_size({"width": 1366, "height": 768})
        self.login_page = LoginPage(page)
        self.inventory_page = InventoryPage(page)
        self.page = page
        # Ensure test-output directory exists
        os.makedirs("test-output", exist_ok=True)

    def test_successful_login_and_product_display(self):
        """Test Requirement 1a, 1b, 1c, 1d: Successful login and product display."""
        print("TEST_001_NormalBrowserWindow(Successful Login and Product Display)")
        print("STEP 1: Navigating to the login page.")
        self.login_page.navigate_to_url()
        time.sleep(2)
        self.page.screenshot(path="test-output/TEST_001_NormalBrowserWindow_Step1_Login_Page.png", full_page=True)
        
        print("STEP 2: Entering the username and the password.")
        self.login_page.login(ConfigReader.STANDARD_USER, ConfigReader.STANDARD_PASSWORD)
        time.sleep(2)
        self.page.screenshot(path="test-output/TEST_001_NormalBrowserWindow_Step2_Credentials_Entered.png", full_page=True)

        print("STEP 3: Verifying redirect to inventory page. (Requirement 1c)")
        expect(self.page).to_have_url(f"{ConfigReader.BASE_URL}{ConfigReader.INVENTORY_PAGE_ENDPOINT}")
        self.page.screenshot(path="test-output/TEST_001_NormalBrowserWindow_Step3_Redirected_To_Inventory.png", full_page=True)
        print("SUCCESS: Redirect to /inventory.html validated.")

        print("STEP 4: Checking whether the products are being displayed as expected. (Requirement 1d)")
        product_count = self.inventory_page.get_product_count()
        assert product_count > 0, f"Expected at least 1 product, but found {product_count}"
        self.page.screenshot(path="test-output/TEST_001_NormalBrowserWindow_Step4_Products_Displayed.png", full_page=True)
        print(f"SUCCESS: Found {product_count} products on the page. Requirement 1d satisfied.")
        time.sleep(2)

    def test_failed_login_error_message(self):
        """Test Requirement 1e: Incorrect credentials should display an error message."""
        print("TEST_002_NormalBrowserWindow(Invalid Login Error Message)")
        print("STEP 1: Navigating to the login page.")
        self.login_page.navigate_to_url()
        time.sleep(2)
        self.page.screenshot(path="test-output/TEST_002_NormalBrowserWindow_Step1_Login_Page.png", full_page=True)
        
        print("STEP 2: Entering the invalid credentials.")
        self.login_page.login("invalid_user", "wrong_password")
        time.sleep(2)
        self.page.screenshot(path="test-output/TEST_002_NormalBrowserWindow_Step2_Invalid_Credentials_Entered.png", full_page=True)

        print("STEP 3: Verifying the error message. (Requirement 1e)")
        error_text = self.login_page.get_error_message()
        expected_error = "Username and password do not match any user in this service"
        assert expected_error in error_text, f"Expected: '{expected_error}', but got: '{error_text}'"
        self.page.screenshot(path="test-output/TEST_002_NormalBrowserWindow_Step3_Error_Message_Displayed.png", full_page=True)
        print(f"SUCCESS: Error message validated: '{error_text}'. Requirement 1e satisfied.")
        time.sleep(2)

    def test_adding_products_to_cart(self):
        """Test Requirement 2: Adding products to cart and validating the cart count."""
        print("TEST_003_NormalBrowserWindow(Validating Cart Functionality)")
        print("STEP 1: Navigating and logging in.")
        self.login_page.navigate_to_url()
        time.sleep(2)
        self.page.screenshot(path="test-output/TEST_003_NormalBrowserWindow_Step1_Login_Page.png", full_page=True)
        
        self.login_page.login(ConfigReader.STANDARD_USER, ConfigReader.STANDARD_PASSWORD)
        time.sleep(2)
        self.page.screenshot(path="test-output/TEST_003_NormalBrowserWindow_Step2_Logged_In.png", full_page=True)

        print("STEP 2: Adding products to cart.")
        products_to_add = 2
        for i in range(products_to_add):
            print(f"Adding product {i+1} to cart.")
            self.inventory_page.add_product_to_cart_by_index(i)
            time.sleep(2)
            self.page.screenshot(path=f"test-output/TEST_003_NormalBrowserWindow_Step3_Product_{i+1}_Added.png", full_page=True)

        time.sleep(2)
        
        print("STEP 3: Verifying cart count and visibility.")
        self.page.screenshot(path="test-output/TEST_003_NormalBrowserWindow_Step4_Cart_Final_State.png", full_page=True)
        
        # Check if cart badge is visible
        is_visible = self.inventory_page.cart_badge.is_visible()
        print(f"Cart badge visibility: {is_visible}")
        
        # Functional verification
        cart_count = self.inventory_page.get_cart_badge_count()
        assert cart_count == products_to_add, f"Expected {products_to_add} items in cart, but found {cart_count}"
        print(f"SUCCESS: Cart has {cart_count} items as expected. Requirement 2 satisfied.")
        
        if is_visible:
            print("NOTE: Cart badge is properly visible in normal browser window size.")
        time.sleep(2)
