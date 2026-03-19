from selenium.webdriver.common.by import By


"""Локаторы для страницы авторизации пользователя"""

class LoginPageLocators:
    # Поле для ввода email
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")

    # Поле для ввода пароля
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")

    # Кнопка входа в систему
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
