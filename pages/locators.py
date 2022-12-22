from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")
    BASKET_PAGE_LINK = (By.CSS_SELECTOR, ".btn-group :first-child")


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_NAME_AFTER_ADD = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    BOOK_PRICE_AFTER_ADD = (By.CSS_SELECTOR, ".alert-info .alertinner strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '//*[@id="content_inner"]/p/text()')
    NO_GOODS_IN_BAKSET = (By.CSS_SELECTOR, ".basket-items")


class LoginPageLocators:
    EMAIL_ADDRESS_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRMED_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    BUTTON_CONFIRMED = (By.CSS_SELECTOR, '#register_form .btn')
