import pytest

from src.pages.inventory_page import InventoryPage
from src.pages.login_page import LoginPage


@pytest.fixture()
def login_page(setup_browser):
    return LoginPage(setup_browser)


@pytest.fixture()
def inventory_page(setup_browser):
    return InventoryPage(setup_browser)
