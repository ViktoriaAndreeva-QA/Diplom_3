import pytest
import allure
from locators.main_page_locators import MainPageLocators


@allure.feature("Лента заказов")
class TestOrderFeed:
    """Тесты для раздела Лента Заказов"""

    @allure.title("После создания нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_counter_of_total_increases_after_create_new_order_success(self, authorized_user, order_feed_page, order_modal_page):
        with allure.step("Перейти в ленту заказов и запомнить текущее значение счётчика"):
            authorized_user.click_order_feed()
            initial_total = order_feed_page.get_total_orders_count()

        with allure.step("Создать новый заказ"):
            authorized_user.click_constructor()
            authorized_user.add_ingredient_to_order(MainPageLocators.BUN_INGREDIENT)
            authorized_user.add_ingredient_to_order(MainPageLocators.SAUCE_INGREDIENT_1)
            authorized_user.add_ingredient_to_order(MainPageLocators.FILLING_INGREDIENT_3)
            authorized_user.add_ingredient_to_order(MainPageLocators.FILLING_INGREDIENT_1)
            authorized_user.click_order_button()

        with allure.step("Дождаться появления номера заказа и закрыть модальное окно"):
            order_modal_page.wait_for_real_order_number()
            order_modal_page.close_modal()

        with allure.step("Вернуться в ленту заказов и получить новое значение счётчика"):
            authorized_user.click_order_feed()
            new_total = order_feed_page.get_total_orders_count()

        with allure.step("Проверить, что счётчик увеличился"):
            assert new_total > initial_total

    @allure.title("После создания нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_counter_of_today_increases_after_create_new_order_success(self, authorized_user, order_feed_page, order_modal_page):
        with allure.step("Перейти в ленту заказов и запомнить текущее значение счётчика за сегодня"):
            authorized_user.click_order_feed()
            initial_today = order_feed_page.get_today_orders_count()

        with allure.step("Создать новый заказ"):
            authorized_user.click_constructor()
            authorized_user.add_ingredient_to_order(MainPageLocators.BUN_INGREDIENT)
            authorized_user.add_ingredient_to_order(MainPageLocators.SAUCE_INGREDIENT_2)
            authorized_user.add_ingredient_to_order(MainPageLocators.FILLING_INGREDIENT_3)
            authorized_user.click_order_button()

        with allure.step("Дождаться появления номера заказа и закрыть модальное окно"):
            order_modal_page.wait_for_real_order_number()
            order_modal_page.close_modal()

        with allure.step("Вернуться в ленту заказов и получить новое значение счётчика"):
            authorized_user.click_order_feed()
            new_today = order_feed_page.wait_for_today_orders_increase(initial_today)

        with allure.step("Проверить, что счётчик увеличился"):
            assert new_today > initial_today

    @allure.title("После создания нового заказа его номер появляется в разделе «В работе»")
    def test_order_number_appears_in_progress_section_after_create_order_success(self, authorized_user, order_feed_page, order_modal_page):
        with allure.step("Создать новый заказ"):
            authorized_user.click_constructor()
            authorized_user.add_ingredient_to_order(MainPageLocators.BUN_INGREDIENT)
            authorized_user.add_ingredient_to_order(MainPageLocators.SAUCE_INGREDIENT_1)
            authorized_user.add_ingredient_to_order(MainPageLocators.FILLING_INGREDIENT_2)
            authorized_user.click_order_button()
        
        with allure.step("Получить номер созданного заказа"):
            order_number = order_modal_page.wait_for_real_order_number()
            order_modal_page.close_modal()

        with allure.step("Перейти в ленту заказов"):
            authorized_user.click_order_feed()

        with allure.step("Получить список заказов в работе"):
            orders_in_progress = order_feed_page.get_orders_in_progress()

        with allure.step("Проверить, что наш заказ есть в списке"):
            assert int(order_number) in [int(order) for order in orders_in_progress]
