import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.ui
def test_successful_login(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    
    assert inventory_page.is_loaded()
    assert "inventory.html" in page.url

@pytest.mark.ui
@pytest.mark.negative
def test_locked_out_user_login(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")
    
    assert "Epic sadface" in login_page.get_error_text()

@pytest.mark.ui
@pytest.mark.datadriven
@pytest.mark.parametrize("username,password,expected_error", [
    ("", "secret_sauce", "Username is required"),
    ("standard_user", "", "Password is required"),
    ("invalid_user", "wrong_password", "Username and password do not match"),
])
def test_login_negative_data_driven(page, username, password, expected_error):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(username, password)
    
    assert expected_error in login_page.get_error_text()

@pytest.mark.ui
def test_add_item_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page.add_first_item_to_cart()
    assert inventory_page.get_cart_count() == "1"

@pytest.mark.ui
def test_logout(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    
    page.locator("#react-burger-menu-btn").click()
    page.locator("#logout_sidebar_link").click()
    
    assert page.locator("#login-button").is_visible()
