from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketCostLocators
from .locators import ButtonBasketLocators
from .locators import CorrectProductNameLocator
from .locators import CorrectBasketPriceLocator


class AddProductToBasket(BasePage):
    def add_to_basket(self):
        button_basket = self.browser.find_element(*ButtonBasketLocators.BUTTON_BASKET)
        button_basket.click()

    def should_be_adding_message_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Adding message to basket is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_message_is_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should be disappeared"

    def should_be_correct_product_name(self):
        name_product = (self.browser.find_element(*CorrectProductNameLocator.NAME_PRODUCT)).text
        name_product_in_basket = (self.browser.find_element(*CorrectProductNameLocator.NAME_PRODUCT_IN_BASKET)).text
        assert name_product == name_product_in_basket, 'Product name in basket is not correct'

    def should_be_message_with_basket_cost(self):
        assert self.is_element_present(*BasketCostLocators.BASKET_COST), 'Message with basket cost is not presented'

    def should_be_correct_basket_price(self):
        basket_price = (self.browser.find_element(*CorrectBasketPriceLocator.BASKET_PRICE)).text
        product_price = (self.browser.find_element(*CorrectBasketPriceLocator.PRODUCT_PRICE)).text
        assert basket_price == product_price, 'Price of basket is not equal with price of good'
