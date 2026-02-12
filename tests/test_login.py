import os

import pytest
from playwright.sync_api import expect

from src.utils.user_names import UserNames


@pytest.mark.usefixtures("setup_browser")
class TestLogin:

    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "username",
        [
            UserNames.STANDARD_USER.value,
            UserNames.PROBLEM_USER.value,
        ]
    )
    def test_valid_login(self, username, login_page, inventory_page):
        login_page.login(username, os.getenv("PASSWORD"))
        expect(inventory_page.get_inventory_page_title_locator()).to_have_text("Products")

    def test_dd(self):
        print("ff")
