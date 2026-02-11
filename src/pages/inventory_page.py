from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

        self.txt_title = self.page.locator("span[class='title']")

    def get_inventory_page_title_locator(self):
        return self.txt_title
