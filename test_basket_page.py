import pytest
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.locators import Links


class TestBasketPage:

    def test_guest_can_forward_from_product_to_basket_page(self, browser):
        link = Links.PUSSYFOOT_BOOK_LINK
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_without_math()
        page.from_product_page_go_to_bakset()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_url()
