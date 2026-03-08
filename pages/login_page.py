import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    """Page Object для страницы авторизации"""
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ввести email: {email}')
    def input_email(self, email):
        email_input = self.find_element(LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)

    @allure.step('Ввести пароль')
    def input_password(self, password):
        password_input = self.find_element(LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)

    @allure.step('Кликнуть на кнопку "Войти"')
    def click_login_button(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Авторизоваться с email: {email} и паролем: {password}')
    def login(self, email, password):
        self.input_email(email)
        self.input_password(password)
        self.click_login_button()
