from .pages.product_page import AddProductToBasket


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = AddProductToBasket(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_adding_message_to_basket()
    page.should_be_correct_product_name()
    page.should_be_message_with_basket_cost()
    page.should_be_correct_basket_price()


