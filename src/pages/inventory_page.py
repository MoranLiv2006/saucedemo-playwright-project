from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

        self.txt_title = self.page.locator("span[class='title']")
        self.list_of_items = self.page.locator(".inventory_item")

    def get_inventory_page_title_locator(self):
        return self.txt_title

    def get_number_of_items_in_inventory_page(self):
        return self.list_of_items
