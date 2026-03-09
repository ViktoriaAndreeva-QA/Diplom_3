import pytest
import allure
from pages.login_page import LoginPage
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.order_feed_locators import OrderFeedLocators
from constants import BASE_URL


@allure.feature("Конструктор")
class TestConstructor:
    """Тесты для страницы конструктора бургера"""

    @allure.title("Клик на «Конструктор» в личном кабинете возвращает пользователя на главную страницу")
    def test_constructor_navigation_click_on_constryctor_from_profile_returns_to_main_page(self, main_page):
        with allure.step("Перейти в профиль"):
            main_page.click_profile()
            LoginPage(main_page.driver).is_visible(LoginPageLocators.EMAIL_INPUT)

        with allure.step("Кликнуть на «Конструктор»"):
            main_page.click_constructor()

        with allure.step("Проверить, что URL соответствует главной странице"):
            assert main_page.get_current_url() == BASE_URL

    @allure.title("Клик на «Лента заказов» открывает страницу с лентой заказов")
    def test_click_order_feed_opens_order_feed_page(self, main_page, order_feed_page):
        with allure.step("Кликнуть на «Лента заказов»"):
            main_page.click_order_feed()

        with allure.step("Проверить, что заголовок ленты заказов отображается"):
            assert order_feed_page.is_visible(OrderFeedLocators.FEED_TITLE)

    @pytest.mark.parametrize("ingredient_locator, expected_name", [
        (MainPageLocators.BUN_INGREDIENT, "Флюоресцентная булка R2-D3"),
        (MainPageLocators.SAUCE_INGREDIENT_1, "Соус фирменный Space Sauce"),
        (MainPageLocators.FILLING_INGREDIENT_1, "Говяжий метеорит (отбивная)"),
        (MainPageLocators.FILLING_INGREDIENT_3, "Сыр с астероидной плесенью")
    ])
    @allure.title("Клик на ингредиент открывает модальное окно с деталями")
    def test_click_on_ingredient_opens_modal_with_details(self, main_page, ingredient_locator, expected_name, ingredient_modal_page):
        with allure.step(f"Кликнуть на ингредиент: {expected_name}"):
            main_page.click_ingredient(ingredient_locator)

        with allure.step("Проверить, что модальное окно открылось"):
            assert ingredient_modal_page.is_modal_open()
        with allure.step(f"Проверить, что название ингредиента соответствует ожидаемому: {expected_name}"):
            assert ingredient_modal_page.get_ingredient_name() == expected_name

    @allure.title("Модальное окно ингредиента закрывается при клике на крестик")
    def test_ingredient_modal_closes_when_click_close_button(self, main_page, ingredient_modal_page):
        with allure.step("Открыть модальное окно ингредиента"):
            main_page.click_ingredient(MainPageLocators.FILLING_INGREDIENT_2)

        with allure.step("Проверить, что модальное окно открылось"):
            assert ingredient_modal_page.is_modal_open()

        ingredient_modal_page.close_modal()

        with allure.step("Проверить, что модальное окно закрылось"):
            assert not ingredient_modal_page.is_modal_open()

    @pytest.mark.parametrize("ingredient_locator, counter_locator, expected_increment", [
        (MainPageLocators.BUN_INGREDIENT, MainPageLocators.BUN_COUNTER, 2),
        (MainPageLocators.SAUCE_INGREDIENT_1, MainPageLocators.SAUCE_COUNTER_1, 1),
        (MainPageLocators.FILLING_INGREDIENT_1, MainPageLocators.FILLING_COUNTER_1, 1)
    ])
    @allure.title("При добавлении ингредиента счётчик увеличивается")
    def test_adding_ingredient_increases_counter(self, authorized_user, ingredient_locator, counter_locator, expected_increment):
        with allure.step(f"Запомнить текущее значение счётчика"):
            initial_count = authorized_user.get_counter_value(counter_locator)
        
        with allure.step(f"Добавить ингредиент в заказ"):
            authorized_user.add_ingredient_to_order(ingredient_locator)
        
        with allure.step(f"Получить новое значение счётчика"):
            new_count = authorized_user.get_counter_value(counter_locator)
        
        with allure.step(f"Проверить, что счётчик увеличился на {expected_increment}"):
            assert new_count == initial_count + expected_increment
