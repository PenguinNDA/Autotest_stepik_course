from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
