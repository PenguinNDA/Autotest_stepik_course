from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):

	def add_to_basket(self):
		self.browser.implicitly_wait(10)
		button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
		print("\nFind button")
		button.click()
		print("\nClick button")
		time.sleep(1)
		BasePage.solve_quiz_and_get_code(self)

	def compare_prices(self):
		self.browser.implicitly_wait(10)
		book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
		book_price_after_add = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_AFTER_ADD)
		print("\nCompare prices")
		assert book_price.text == book_price_after_add.text, "Price is not equal"
		print(f"Price {book_price.text} is equal to {book_price_after_add.text}")

	def compare_names(self):
		self.browser.implicitly_wait(10)
		book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
		book_name_after_add = self.browser.find_element(*ProductPageLocators.BOOK_NAME_AFTER_ADD)
		print("\nCompare names")
		assert book_name.text == book_name_after_add.text, "Names is not equal"
		print(f"Name {book_name.text} is equal to {book_name_after_add.text}")

	def is_book_name_after_add_present(self):
		assert self.is_not_element_present(*ProductPageLocators.BOOK_NAME_AFTER_ADD), "Book name is incorrect"

	def is_book_name_disappeared_after_add(self):
		assert self.is_disappeared(*ProductPageLocators.BOOK_NAME_AFTER_ADD), "Book name is incorrect"
