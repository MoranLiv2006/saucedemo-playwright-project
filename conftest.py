import pytest
import os

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

from src.pages.inventory_page import InventoryPage
from src.pages.login_page import LoginPage

load_dotenv()

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser(playwright_instance):
    headless = os.getenv("HEADLESS", "true").lower() == "true"
    browser = playwright_instance.chromium.launch(headless=headless)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def setup_browser(browser):
    context = browser.new_context()
    page = context.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto(os.getenv("BASE_URL"))
    yield page
    context.close()

#
# @pytest.fixture()
# def login_page(setup_browser):
#     return LoginPage(setup_browser)
#
#
# @pytest.fixture()
# def inventory_page(setup_browser):
#     return InventoryPage(setup_browser)
