from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.inventory_container = page.locator(".inventory_list")
        self.add_to_cart_btn = page.locator("button[data-test^='add-to-cart']")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def is_loaded(self) -> bool:
        return self.inventory_container.is_visible()

    def add_first_item_to_cart(self):
        self.add_to_cart_btn.first.click()

    def get_cart_count(self) -> str:
        return self.cart_badge.inner_text()
