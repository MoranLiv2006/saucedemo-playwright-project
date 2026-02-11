from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.txt_username = self.page.locator("#user-name")
        self.txt_password = self.page.locator("#password")
        self.btn_login = self.page.locator("#login-button")

    def login(self, username: str, password: str):
        self.txt_username.fill(username)
        self.txt_password.fill(password)
        self.btn_login.click()