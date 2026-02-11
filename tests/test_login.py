import pytest
import os

from playwright.sync_api import expect

from src.pages.inventory_page import InventoryPage
from src.pages.login_page import LoginPage
from src.utils.user_names import UserNames

@pytest.mark.usefixtures("setup_browser")
class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, setup_browser):
        self.page = setup_browser

        self.login_page = LoginPage(self.page)
        self.inventory_page = InventoryPage(self.page)

    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "username",
        [
            UserNames.STANDARD_USER.value,
            UserNames.PROBLEM_USER.value,
        ]
    )
    def test_valid_login(self, username):
        self.login_page.login(username, os.getenv("PASSWORD"))
        expect(self.inventory_page.get_inventory_page_title_locator()).to_have_text("Products")

    def test_dd(self):
        print("ff")
