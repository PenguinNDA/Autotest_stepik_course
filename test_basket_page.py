import pytest
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
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

    @pytest.mark.xfail
    def test_remove_book_from_basket_page(self, browser):  # Remove button doesn't work for now
        link = Links.PUSSYFOOT_BOOK_LINK
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_without_math()
        page.from_product_page_go_to_bakset()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.press_remove_button_in_basket_page()
        basket_page.is_not_goods_in_basket()

    def test_empty_basket_after_delete_goods(self, browser):
        link = Links.PUSSYFOOT_BOOK_LINK
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_without_math()
        page.from_product_page_go_to_bakset()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.send_number_of_goods_to_count_field(0)
        basket_page.click_to_update_button()
        basket_page.is_not_goods_in_basket()

    @pytest.mark.new
    def test_check_price_for_multiple_goods_in_basket(self, browser):
        link = Links.PUSSYFOOT_BOOK_LINK
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_without_math()
        page.from_product_page_go_to_bakset()
        basket_page = BasketPage(browser, browser.current_url)
        number_of_goods = BasketPage.choose_randomly_our_goods()
        basket_page.send_number_of_goods_to_count_field(number_of_goods)
        basket_page.click_to_update_button()
        basket_page.our_price_is_correct()
        basket_page.our_sum_is_correct(number_of_goods)

    @pytest.mark.new
    def test_check_price_for_one_good_in_basket(self, browser):
        link = Links.PUSSYFOOT_BOOK_LINK
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket_without_math()
        page.from_product_page_go_to_bakset()
        basket_page = BasketPage(browser, browser.current_url)
        number_of_goods = BasketPage.choose_randomly_our_goods()
        basket_page.send_number_of_goods_to_count_field(number_of_goods)
        basket_page.click_to_update_button()
        basket_page.our_sum_is_correct(number_of_goods)
