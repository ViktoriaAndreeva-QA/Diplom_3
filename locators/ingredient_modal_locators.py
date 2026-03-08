from selenium.webdriver.common.by import By


"""Локаторы для модального окна с информацией об ингредиенте"""

class IngredientModalLocators:
    # Модальное окно
    MODAL_WINDOW = (By.XPATH, "//section[contains(@class, 'Modal_modal') and contains(@class, 'opened')]")

    # Кнопка закрытия (крестик)
    CLOSE_BUTTON = (By.XPATH, "(//button[contains(@class, 'Modal_modal__close')])[1]")
    
    # Название ингредиента в модальном окне
    INGREDIENT_NAME = (By.XPATH, "//section[contains(@class, 'Modal_modal')]//p[contains(@class, 'text_type_main-medium')]")
