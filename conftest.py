import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from constants import BASE_URL
from data.user_data import TEST_USER
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from pages.ingredient_modal_page import IngredientModalPage
from pages.order_modal_page import OrderModalPage


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
    return MainPage(driver)

@pytest.fixture
def login_page(driver):
    """Страница авторизации"""
    return LoginPage(driver)

@pytest.fixture
def order_feed_page(driver):
    """Страница раздела "Лента Заказов"""
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
    return IngredientModalPage(driver)

@pytest.fixture
def order_modal_page(driver):
    return OrderModalPage(driver)
