import pytest
from .pages.product_page import AddProductToBasket


# @pytest.mark.parametrize('link',
#                          ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
#                           pytest.param("offer7", marks=pytest.mark.xfail), "offer8",
#                           "offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={link}"
#     page = AddProductToBasket(browser, link)
#     page.open()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.should_be_adding_message_to_basket()
#     page.should_not_be_success_message()
#     page.should_be_message_is_disappeared()
#     page.should_be_correct_product_name()
#     page.should_be_message_with_basket_cost()
#     page.should_be_correct_basket_price()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = AddProductToBasket(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = AddProductToBasket(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = AddProductToBasket(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_message_is_disappeared()





