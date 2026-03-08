import allure
from pages.base_page import BasePage
from locators.order_modal_locators import OrderModalLocators
from selenium.webdriver.support import expected_conditions as EC



class OrderModalPage(BasePage):
    """Page Object для модального окна создания заказа"""
    def __init__(self, driver):
        super().__init__(driver)


    
    @allure.step('Дождаться настоящего номера заказа')
    def wait_for_real_order_number(self):
        """Ждёт, пока номер заказа перестанет быть 9999"""
        
        def order_number_changed(driver):
            element = driver.find_element(*OrderModalLocators.ORDER_NUMBER)
            number_text = element.text
            # Ждём, пока номер не станет цифрой и не равен 9999
            return number_text.isdigit() and number_text != "9999"
        
        # Ждём максимум 10 секунд, пока номер не изменится
        self.wait.until(order_number_changed)
        
        # Получаем настоящий номер заказа
        element = self.find_element(OrderModalLocators.ORDER_NUMBER)
        return element.text

    @allure.step('Закрыть модальное окно')
    def close_modal(self):
        self.wait_for_real_order_number()
        self.wait.until(EC.visibility_of_element_located(OrderModalLocators.MODAL_WINDOW))

        close_button = self.wait.until(EC.element_to_be_clickable(OrderModalLocators.CLOSE_BUTTON))
        self.driver.execute_script("arguments[0].click();", close_button)
