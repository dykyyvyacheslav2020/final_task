from .base_page import BasePage
from .locators import BasketIsEmptyLocators
from .locators import ProductNotPresentInBasketLocators


class BasketPage(BasePage):
    def should_be_any_product_in_basket(self):
        assert self.is_not_element_present(
            *ProductNotPresentInBasketLocators.PRODUCT_NOT_PRESENT_IN_BASKET), "Product is presented in basket, but should not be"

    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasketIsEmptyLocators.BASKET_IS_EMPTY), "Empty basket message is not presented"
