from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .locators import BasketCostLocators


class AddProductToBasket(BasePage):
    def add_to_basket(self):
        button_basket = self.browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        button_basket.click()

    def should_be_adding_message_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), 'Adding message to basket is not presented'

    def should_be_correct_product_name(self):
        x = (self.browser.find_element(By.CSS_SELECTOR, "div.col-sm-6:nth-child(2) > h1:nth-child(1)")).text
        y = (self.browser.find_element(By.CSS_SELECTOR,
                                       "div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)")).text
        assert x == y, 'Product name in basket is not correct'

    def should_be_message_with_basket_cost(self):
        assert self.is_element_present(*BasketCostLocators.BASKET_COST), 'Message with basket cost is not presented'

    def should_be_correct_basket_price(self):
        a = (self.browser.find_element(By.CSS_SELECTOR, "div.alert:nth-child(3)>.alertinner>p>strong")).text
        b = (self.browser.find_element(By.CSS_SELECTOR, ".product_main>p.price_color")).text
        assert a == b, 'Price of basket is not equal with price of good'