from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.locators import Links
import pytest
import time


@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.compare_names()
    page.compare_prices()
    time.sleep(3)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = Links.CODERS_AT_WORK_BOOK_LINK
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_book_name_after_add_present()


def test_guest_cant_see_success_message(browser):
    link = Links.CODERS_AT_WORK_BOOK_LINK
    page = ProductPage(browser, link)
    page.open()
    page.is_book_name_after_add_present()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = Links.CODERS_AT_WORK_BOOK_LINK
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.is_book_name_disappeared_after_add()


@pytest.mark.login_guest
class TestLoginFromProductPage:

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = Links.CITY_AND_STARS_BOOK_LINK
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = Links.CITY_AND_STARS_BOOK_LINK
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = Links.CITY_AND_STARS_BOOK_LINK
    page = ProductPage(browser, link)  # Initialize page object
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_not_goods_in_basket()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup_for_user_tests(self, browser):
        link = Links.LOGIN_LINK
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = Links.CODERS_AT_WORK_BOOK_LINK
        page = ProductPage(browser, link)
        page.open()
        page.is_book_name_after_add_present()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = Links.CODERS_AT_WORK_BOOK_LINK
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.compare_names()
        page.compare_prices()


def test_check_price_without_tax_at_book_page(browser):
    link = Links.CODERS_AT_WORK_BOOK_LINK
    page = ProductPage(browser, link)
    page.open()
    page.check_price_without_tax()


def test_check_price_with_tax_at_book_page(browser):
    link = Links.CODERS_AT_WORK_BOOK_LINK
    page = ProductPage(browser, link)
    page.open()
    page.check_price_with_tax()
