import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from locators.order_modal_locators import OrderModalLocators
from selenium.webdriver.support import expected_conditions as EC



class OrderFeedPage(BasePage):
    """Page Object для раздела "Лента Заказов"""
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Получить значение счётчика "Выполнено за всё время"')
    def get_total_orders_count(self):
        """Возвращает число из счётчика 'Выполнено за всё время'"""
        self.wait.until(lambda driver: driver.find_element(*OrderFeedLocators.TOTAL_ORDERS_COUNTER).text.strip().isdigit())
        text = self.get_text(OrderFeedLocators.TOTAL_ORDERS_COUNTER)
        return int(text)
    
    @allure.step('Получить значение счётчика "Выполнено за сегодня"')
    def get_today_orders_count(self):
        """Возвращает число из счётчика 'Выполнено за сегодня'"""
        self.wait.until(lambda driver: driver.find_element(*OrderFeedLocators.TODAY_ORDERS_COUNTER).text.strip().isdigit())
        text = self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNTER)
        return int(text)
    
    @allure.step('Ожидать увеличения счётчика "Выполнено за сегодня"')
    def wait_for_today_orders_increase(self, initial_count):
        """Ждёт, пока счётчик за сегодня станет больше initial_count"""
        def counter_increased(driver):
            return self.get_today_orders_count() > initial_count
    
        self.wait.until(counter_increased)
        return self.get_today_orders_count()
    
    @allure.step('Получить номера заказов в работе')
    def get_orders_in_progress(self):
        """Возвращает список номеров заказов в работе"""
        self.wait.until(lambda driver: driver.find_element(*OrderFeedLocators.ORDERS_IN_PROGRESS).text.strip().isdigit())
        order_elements = self.find_elements(OrderFeedLocators.ORDERS_IN_PROGRESS)
        return [element.text for element in order_elements]
    