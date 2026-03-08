import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_modal_locators import OrderModalLocators
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    """Page Object для главной страницы (конструктора)"""
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликнуть на ссылку "Конструктор"')
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_LINK)
    
    @allure.step('Кликнуть на ссылку "Лента Заказов"')
    def click_order_feed(self):
        self.wait.until(EC.invisibility_of_element_located(OrderModalLocators.MODAL_WINDOW))
        link = self.wait.until(EC.element_to_be_clickable(MainPageLocators.ORDER_FEED_LINK))
        link.click()

    @allure.step('Кликнуть на ссылку "Личный Кабинет"')
    def click_profile(self):
        self.click(MainPageLocators.PROFILE_LINK)

    @allure.step('Кликнуть на ингредиент {locator}')
    def click_ingredient(self, locator):
        self.scroll_to_element(locator)
        self.find_clickable_element(locator).click()

    @allure.step('Получить значение счётчика {locator}')
    def get_counter_value(self, locator):
        text = self.get_text(locator)
        return int(text) if text.isdigit() else 0
    
    @allure.step('Добавить ингредиент {ingredient_locator} в заказ')
    def add_ingredient_to_order(self, ingredient_locator):
        ingredient = self.wait.until(
        EC.visibility_of_element_located(ingredient_locator),
        message=f"Ингредиент {ingredient_locator} не видим"
    )
        constructor_zone = self.find_element(MainPageLocators.CONSTRUCTOR_ZONE)

        self.driver.execute_script("""
            arguments[0].dispatchEvent(new DragEvent('dragstart', {bubbles: true}));
            arguments[1].dispatchEvent(new DragEvent('drop', {bubbles: true}));
        """, ingredient, constructor_zone)

    @allure.step('Кликнуть на "Оформить заказ"')
    def click_order_button(self):
        order_button = self.wait.until(
            EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON)
        )
        order_button.click()
