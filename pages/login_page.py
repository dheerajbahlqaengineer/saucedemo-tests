from playwright.sync_api import Page
from utilities.config_reader import ConfigReader

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_field = page.locator("#user-name")
        self.password_field = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("h3[data-test='error']")

    def navigate_to_url(self):
        self.page.goto(ConfigReader.BASE_URL)
        # Wait for page to load
        self.page.wait_for_load_state('networkidle')

    def login(self, username: str, password: str):
        # Wait for elements to be visible before interacting
        self.username_field.wait_for(state='visible')
        self.password_field.wait_for(state='visible')
        self.login_button.wait_for(state='visible')
        
        self.username_field.clear()
        self.username_field.fill(username)
        self.password_field.clear()
        self.password_field.fill(password)
        self.login_button.click()

    def get_error_message(self):
        self.error_message.wait_for(state='visible')
        return self.error_message.text_content()
