from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators


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

    def register_new_user(self, email, password):
        self.browser.implicitly_wait(10)
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        confirmed_password_field = self.browser.find_element(*LoginPageLocators.CONFIRMED_PASSWORD_FIELD)
        confirmed_password_field.send_keys(password)
        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_CONFIRMED)
        button_register.click()
