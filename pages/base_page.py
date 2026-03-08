import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from constants import TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)
    
    @allure.step("Найти элемент {locator}")
    def find_element(self, locator):
        """Найти элемент с явным ожиданием появления"""
        return self.wait.until(EC.presence_of_element_located(locator))
    
    @allure.step("Найти все элементы {locator}")
    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def find_clickable_element(self, locator):
        """Найти кликабельный элемент с явным ожиданием"""
        return self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {locator} не кликабелен"
        )
    
    def find_visible_element(self, locator):
        """Найти видимый элемент с явным ожиданием"""
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент {locator} не видим"
        )
    
    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator):
        """Кликнуть по элементу"""
        element = self.find_clickable_element(locator)
        element.click()
    
    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        """Получить текст элемента"""
        element = self.find_visible_element(locator)
        return element.text
    
    def is_visible(self, locator, timeout=5):
        """Проверить, виден ли элемент (с меньшим таймаутом)"""
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
    
    @allure.step("Прокрутить до элемента {locator}")
    def scroll_to_element(self, locator):
        """Прокрутить до элемента"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url
