from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By



class LoginPage(BasePage):
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        go_to_login_page = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        go_to_login_page.click()
        x = self.browser.find_element(By.CSS_SELECTOR, "input#id_registration-email.form-control")
        x.send_keys(email)
        registration_password1 = self.browser.find_element(By.CSS_SELECTOR,
                                                           "input#id_registration-password1.form-control")
        registration_password1.send_keys(password)
        registration_password2 = self.browser.find_element(By.CSS_SELECTOR,
                                                           "input#id_registration-password2.form-control")
        registration_password2.send_keys(password)
        button_register = self.browser.find_element(By.XPATH, "//button[@value='Register']")
        button_register.click()



