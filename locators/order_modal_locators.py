from selenium.webdriver.common.by import By

"""Локаторы для модального окна с номером заказа"""

class OrderModalLocators:
    # Модальное окно (используем contains для надёжности)
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]")
    
    # Номер созданного заказа
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    
    # Кнопка закрытия
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'close')]")
