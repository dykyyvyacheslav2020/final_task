from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner ")


class BasketCostLocators:
    BASKET_COST = (By.CSS_SELECTOR, "div.alert:nth-child(3)>div.alertinner")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_PAGE = (By.CSS_SELECTOR, "span.btn-group")


class ProductNotPresentInBasketLocators:
    PRODUCT_NOT_PRESENT_IN_BASKET = (By.CSS_SELECTOR, "div.basket-items>div.row")


class BasketIsEmptyLocators:
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")


class ButtonBasketLocators:
    BUTTON_BASKET = (By.CLASS_NAME, "btn-add-to-basket")


class CorrectProductNameLocator:
    NAME_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6:nth-child(2) > h1:nth-child(1)")
    NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)")


class CorrectBasketPriceLocator:
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert:nth-child(3)>.alertinner>p>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>p.price_color")


class RegistrationLocator:
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email.form-control")
    REGISTRATION_PASSWORD_1 = (By.CSS_SELECTOR, "input#id_registration-password1.form-control")
    REGISTRATION_PASSWORD_2 = (By.CSS_SELECTOR, "input#id_registration-password2.form-control")
    BUTTON_REGISTRATION = (By.XPATH, "//button[@value='Register']")
