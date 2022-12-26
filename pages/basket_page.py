from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

PRICE_FOR_BOOK = 26.99


class BasketPage(BasePage):

    def is_not_goods_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

    def is_goods_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def compare_text_in_empty_basket(self):
        self.browser.implicitly_wait(10)
        empty_basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT)
        assert empty_basket_text.text == "Ваша корзина пуста", "Names is not equal"
        print(f"Name {empty_basket_text.text} is equal to 'Ваша корзина пуста'")

    def is_not_goods_in_basket(self):
        assert self.is_not_goods_present(*BasketPageLocators.NO_GOODS_IN_BAKSET), "We have some goods in basket"

    def is_good_in_basket(self):
        assert self.is_goods_present(*BasketPageLocators.NO_GOODS_IN_BAKSET), "We don't have goods in basket"

    def should_be_basket_url(self):
        assert "/basket" in self.browser.current_url, "URL is incorrect!"

    def press_remove_button_in_basket_page(self):
        button_remove = self.browser.find_element(*BasketPageLocators.REMOVE_BUTTON)
        button_remove.click()

    def send_number_of_goods_to_count_field(self, number):
        count_field = self.browser.find_element(*BasketPageLocators.COUNT_FIELD)
        count_field.clear()
        count_field.send_keys(number)

    def click_to_update_button(self):
        update_button = self.browser.find_element(*BasketPageLocators.UPDATE_BUTTON)
        update_button.click()

    @staticmethod
    def choose_randomly_our_goods():
        list_of_goods = [2, 3, 4, 5]
        number_of_goods = random.choice(list_of_goods)
        return number_of_goods

    def our_price_is_correct(self):
        assert str(PRICE_FOR_BOOK) \
               in self.browser.find_element(*BasketPageLocators.PRICE_FOR_GOOD).text, "Our price is incorrect "

    def our_sum_is_correct(self, number_of_goods):
        assert str(number_of_goods * PRICE_FOR_BOOK) \
               in self.browser.find_element(*BasketPageLocators.SUM_FOR_GOODS).text, "Sum of our goods is incorrect"
