import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from constants import BASE_URL


# Данные тестового пользователя (один на все тесты, как разрешил наставник)
TEST_USER = {
    "email": "IvanIvanov13234@yandex.ru",
    "password": "password123"
}

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """Создание драйвера браузера"""
    browser = request.param
    
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    
    driver.get(BASE_URL)
    driver.maximize_window()
    
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    """Главная страница"""
    from pages.main_page import MainPage
    return MainPage(driver)

@pytest.fixture
def login_page(driver):
    """Страница авторизации"""
    from pages.login_page import LoginPage
    return LoginPage(driver)

@pytest.fixture
def order_feed_page(driver):
    """Страница раздела "Лента Заказов"""
    from pages.order_feed_page import OrderFeedPage
    return OrderFeedPage(driver)

@pytest.fixture
def authorized_user(main_page, login_page):
    """Авторизованный пользователь"""
    main_page.click_profile()
    login_page.login(TEST_USER["email"], TEST_USER["password"])
    main_page.wait.until(EC.url_to_be(BASE_URL))
    return main_page

@pytest.fixture
def ingredient_modal_page(driver):
    """Модальное окно с информацией об ингредиенте"""
    from pages.ingredient_modal_page import IngredientModalPage
    return IngredientModalPage(driver)

@pytest.fixture
def order_modal_page(driver):
    from pages.order_modal_page import OrderModalPage
    return OrderModalPage(driver)
