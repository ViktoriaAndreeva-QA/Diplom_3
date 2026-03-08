import allure
from pages.base_page import BasePage
from locators.ingredient_modal_locators import IngredientModalLocators


class IngredientModalPage(BasePage):
    """Page Object для модального окна ингредиента"""
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Проверить, что модальное окно открыто')
    def is_modal_open(self):
        return self.is_visible(IngredientModalLocators.MODAL_WINDOW)
    
    @allure.step('Получить название ингредиента в модальном окне')
    def get_ingredient_name(self):
        element = self.find_visible_element(IngredientModalLocators.INGREDIENT_NAME)
        return element.text

    @allure.step('Закрыть модальное окно')
    def close_modal(self):
        self.click(IngredientModalLocators.CLOSE_BUTTON)
