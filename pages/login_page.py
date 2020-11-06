from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
from .locators import RegistrationLocator


class LoginPage(BasePage):
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        go_to_login_page = (self.browser.find_element(*MainPageLocators.LOGIN_LINK))
        go_to_login_page.click()
        registration_email = (self.browser.find_element(*RegistrationLocator.REGISTRATION_EMAIL))
        registration_email.send_keys(email)
        registration_password1 = (self.browser.find_element(*RegistrationLocator.REGISTRATION_PASSWORD_1))
        registration_password1.send_keys(password)
        registration_password2 = (self.browser.find_element(*RegistrationLocator.REGISTRATION_PASSWORD_2))
        registration_password2.send_keys(password)
        button_registration = (self.browser.find_element(*RegistrationLocator.BUTTON_REGISTRATION))
        button_registration.click()
