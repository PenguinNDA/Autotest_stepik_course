from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import BasketPageLocators


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                          # Initialize page object
    page.open()                                             # open link
    page.go_to_login_page()                                 # go to login page
    login_page = LoginPage(browser, browser.current_url)    # initialize login page
    login_page.should_see_login_page()                      # Check login page is really login page
    login_page.should_see_login_form()                      # Try to find login form
    login_page.should_see_register_form()                   # Try to find registration form


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                          # Initialize page object
    page.open()
    page.go_to_basket_page()
    basketPage = BasketPage(browser, browser.current_url)
    assert basketPage.is_not_goods_present(*BasketPageLocators.NO_GOODS_IN_BAKSET), "We have some goods in basket"
