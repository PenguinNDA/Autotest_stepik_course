from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import pytest
import time


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1'
	page = ProductPage(browser, link)
	page.open()
	page.add_to_basket()
	page.compare_names()
	page.compare_prices()
	time.sleep(3)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1'
	page = ProductPage(browser, link)
	page.open()
	page.add_to_basket()
	assert page.is_not_element_present(*ProductPageLocators.BOOK_NAME_AFTER_ADD)


def test_guest_cant_see_success_message(browser):
	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1'
	page = ProductPage(browser, link)
	page.open()
	assert page.is_not_element_present(*ProductPageLocators.BOOK_NAME_AFTER_ADD)


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1'
	page = ProductPage(browser, link)
	page.open()
	page.add_to_basket()
	assert page.is_disappeared(*ProductPageLocators.BOOK_NAME_AFTER_ADD)


def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()
