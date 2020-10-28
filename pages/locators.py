from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    PRODUCT_NAME = (By.CLASS_NAME, "alertinner ")

class BasketCostLocators:
    BASKET_COST = (By.CSS_SELECTOR, "div.alert:nth-child(3)>div.alertinner")
