import pytest
import os

from playwright.sync_api import expect

from src.utils.user_names import UserNames


@pytest.mark.usefixtures("setup_browser")
class TestInventory:

    def perform_login(self, login_page):
        login_page.login(UserNames.STANDARD_USER.value, os.getenv("PASSWORD"))

    def test_verify_number_of_items(self, login_page, inventory_page):
        self.perform_login(login_page)
        expect(inventory_page.get_inventory_page_title_locator()).to_have_text("Products")
        expect(inventory_page.get_number_of_items_in_inventory_page()).to_have_count(6)


