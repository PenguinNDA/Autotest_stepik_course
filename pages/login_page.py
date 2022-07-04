from .base_page import BasePage
from .locators import MainPageLocators


class LoginPage(BasePage):
    def should_see_login_page(self):
        self.should_be_login_url()

    def should_see_login_form(self):
        self.should_be_login_form()

    def should_see_register_form(self):
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login" in self.browser.current_url, "URL is incorrect!"

    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.REGISTER_FORM), "Register form not found"
