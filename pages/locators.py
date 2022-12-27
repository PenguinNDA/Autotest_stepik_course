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
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".alertinner .btn-info:first-child")
    PRICE_WITHOUT_TAX = (By.XPATH, "//table/tbody/tr[3]/td")
    PRICE_WITH_TAX = (By.XPATH, "//table/tbody/tr[4]/td")
    UPC_FIELD = (By.XPATH, "//table/tbody/tr[1]/th")
    PRODUCT_TYPE_FIELD = (By.XPATH, "//table/tbody/tr[2]/th")
    PRICE_WITH_TAX_FIELD = (By.XPATH, "//table/tbody/tr[3]/th")
    PRICE_WITHOUT_TAX_FIELD = (By.XPATH, "//table/tbody/tr[4]/th")
    TAX_FIELD = (By.XPATH, "//table/tbody/tr[5]/th")
    AVAILABILITY_FIELD = (By.XPATH, "//table/tbody/tr[6]/th")
    NUMBER_OF_REVIEWS_FIELD = (By.XPATH, "//table/tbody/tr[7]/th")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.XPATH, '//*[@id="content_inner"]/p/text()')
    NO_GOODS_IN_BAKSET = (By.CSS_SELECTOR, ".basket-items")
    REMOVE_BUTTON = (By.XPATH, "//*[@class='inline']")
    COUNT_FIELD = (By.CSS_SELECTOR, ".checkout-quantity .form-control")
    UPDATE_BUTTON = (By.CSS_SELECTOR, ".checkout-quantity .btn")
    SUM_FOR_GOODS = (By.XPATH, "//*[@id='basket_formset']/div/div/div[5]/p")
    PRICE_FOR_GOOD = (By.XPATH, '//*[@id="basket_formset"]/div/div/div[4]/p')


class LoginPageLocators:
    EMAIL_ADDRESS_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    CONFIRMED_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    BUTTON_CONFIRMED = (By.CSS_SELECTOR, '#register_form .btn')


class Links:
    LOGIN_LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    START_LINK = "http://selenium1py.pythonanywhere.com/"
    CODERS_AT_WORK_BOOK_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer1"
    CITY_AND_STARS_BOOK_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    PUSSYFOOT_BOOK_LINK = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-age-of-the-pussyfoot_89/"
