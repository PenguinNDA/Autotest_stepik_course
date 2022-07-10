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
		BasePage.solve_quiz_and_get_code(self)

	def compare_prices(self):
		self.browser.implicitly_wait(10)
		book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
		book_price_after_add = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
		assert book_price.text == book_price_after_add.text, "Price is not equal"
		print(f"Price {book_price.text} is equal to {book_price_after_add.text}")

	def compare_names(self):
		self.browser.implicitly_wait(10)
		book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
		book_name_after_add = self.browser.find_element(*ProductPageLocators.BOOK_NAME_AFTER_ADD)
		assert book_name.text in book_name_after_add.text, "Names is not equal"
		print(f"Name {book_name.text} is equal to {book_name_after_add.text}")
