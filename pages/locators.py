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
