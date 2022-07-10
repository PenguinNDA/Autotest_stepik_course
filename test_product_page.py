from .pages.product_page import ProductPage
import pytest

link_ = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
pages_list = [f'{link_}?promo=offer{i}' for i in range(10)]
pages_list[7] = pytest.param(pages_list[7], marks=pytest.mark.xfail)


@pytest.mark.parametrize('link', pages_list)
def test_guest_can_add_product_to_basket(browser, link):
	page = ProductPage(browser, link)
	page.open()
	page.add_to_basket()
	page.compare_names()
	page.compare_prices()
