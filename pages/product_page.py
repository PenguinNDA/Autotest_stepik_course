from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.implicitly_wait(10)
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        print("\nFind button")
        button.click()
        print("\nClick button")
        self.browser.implicitly_wait(10)
        BasePage.solve_quiz_and_get_code(self)

    def add_to_basket_without_math(self):
        self.browser.implicitly_wait(10)
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        print("\nFind button")
        button.click()
        print("\nClick button")
        self.browser.implicitly_wait(10)

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

    def from_product_page_go_to_bakset(self):  # use 'view basket' button after add good
        self.browser.implicitly_wait(10)
        button = self.browser.find_element(*ProductPageLocators.VIEW_BASKET_BUTTON)
        print("\nFind button")
        button.click()
        print("\nClick button")

    def check_price_without_tax(self):
        self.browser.implicitly_wait(5)
        assert str(19.99) in str(self.browser.find_element(*ProductPageLocators.PRICE_WITHOUT_TAX).text), \
            "Price is incorrect"
        print(
            f"Price {19.99} is not equal {str(self.browser.find_element(*ProductPageLocators.PRICE_WITHOUT_TAX).text)} "
            f"is incorrect")

    def check_price_with_tax(self):
        self.browser.implicitly_wait(5)
        assert str(19.99) in str(self.browser.find_element(*ProductPageLocators.PRICE_WITH_TAX).text), \
            "Price is incorrect"
        print(
            f"Price {19.99} is not equal {str(self.browser.find_element(*ProductPageLocators.PRICE_WITH_TAX).text)} "
            f"is incorrect")

    def check_upc_field(self):
        self.browser.implicitly_wait(5)
        assert str("UPC") in str(self.browser.find_element(*ProductPageLocators.UPC_FIELD).text), \
            "Field 'UPC' not found"
        print(
            f"Field {'UPC'} is not equal {str(self.browser.find_element(*ProductPageLocators.UPC_FIELD).text)} "
            f"is incorrect")

    def check_product_type_field(self):
        assert str("Product Type") in str(self.browser.find_element(*ProductPageLocators.PRODUCT_TYPE_FIELD).text), \
            "Field 'Product Type' not found"
        print(
            f"Field {'Product Type'} is not equal "
            f"{str(self.browser.find_element(*ProductPageLocators.PRODUCT_TYPE_FIELD).text)}")

    def check_price_with_tax_field(self):
        assert str("Price (excl. tax)") in str(self.browser.find_element(*ProductPageLocators.PRICE_WITH_TAX_FIELD).text), \
            "Field 'Price (excl. tax)' not found"
        print(
            f"Field {'Price (excl. tax)'} is not equal "
            f"{str(self.browser.find_element(*ProductPageLocators.PRICE_WITH_TAX_FIELD).text)}")

    def check_price_without_tax_field(self):
        assert str("Price (incl. tax)") in str(self.browser.find_element(*ProductPageLocators.PRICE_WITHOUT_TAX_FIELD).text), \
            "Field 'Price (incl. tax)' not found"
        print(
            f"Field {'Price (incl. tax)'} is not equal "
            f"{str(self.browser.find_element(*ProductPageLocators.PRICE_WITHOUT_TAX_FIELD).text)}")

    def check_tax_field(self):
        assert str("Tax") in str(self.browser.find_element(*ProductPageLocators.TAX_FIELD).text), \
            "Field 'Tax' not found"
        print(
            f"Field {'Tax'} is not equal "
            f"{str(self.browser.find_element(*ProductPageLocators.TAX_FIELD).text)}")

    def check_availability_field(self):
        assert str("Availability") in str(self.browser.find_element(*ProductPageLocators.AVAILABILITY_FIELD).text), \
            "Field 'Availability' not found"
        print(
            f"Field {'Availability'} is not equal "
            f"{str(self.browser.find_element(*ProductPageLocators.AVAILABILITY_FIELD).text)}")

    def check_number_of_reviews_filed(self):
        assert str("Number of reviews") in str(self.browser.find_element(*ProductPageLocators.NUMBER_OF_REVIEWS_FIELD).text), \
            "Field 'Number of reviews' not found"
        print(
            f"Field {'Number of reviews'} is not equal "
            f"{str(self.browser.find_element(*ProductPageLocators.NUMBER_OF_REVIEWS_FIELD).text)}")
