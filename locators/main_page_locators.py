from selenium.webdriver.common.by import By


"""Локаторы для главной страницы (конструктора)"""

class MainPageLocators:
    # Навигация
    CONSTRUCTOR_LINK = (By.XPATH, "//a[.//p[text()='Конструктор']]")
    ORDER_FEED_LINK = (By.XPATH, "//p[text()='Лента Заказов']/parent::a")
    PROFILE_LINK = (By.XPATH, "//a[.//p[text()='Личный Кабинет']]")

    # Кнопки
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    # Зона конструктора
    CONSTRUCTOR_ZONE = (By.CLASS_NAME, "BurgerConstructor_basket__list__l9dp_")

    # Ингредиенты
    BUN_INGREDIENT = (By.XPATH, "//a[contains(@href, '61c0c5a71d1f82001bdaaa6d')]")
    SAUCE_INGREDIENT_1 = (By.XPATH, "//a[contains(@href, '61c0c5a71d1f82001bdaaa73')]")
    SAUCE_INGREDIENT_2 = (By.XPATH, "//a[contains(@href, '61c0c5a71d1f82001bdaaa75')]")
    FILLING_INGREDIENT_1 = (By.XPATH, "//a[contains(@href, '61c0c5a71d1f82001bdaaa70')]")
    FILLING_INGREDIENT_2 = (By.XPATH, "//a[contains(@href, '61c0c5a71d1f82001bdaaa77')]")
    FILLING_INGREDIENT_3 = (By.XPATH, "//a[contains(@href, '61c0c5a71d1f82001bdaaa7a')]")
    
    # Счётчики
    BUN_COUNTER = (By.XPATH, "//a[contains(@href, '61c0c5a71d1f82001bdaaa6d')]//p[contains(@class, 'counter__num')]")
    SAUCE_COUNTER_1 = (By.XPATH, "//a[contains(@href, '61c0c5a71d1f82001bdaaa73')]//p[contains(@class, 'counter__num')]")
    SAUCE_COUNTER_2 = (By.XPATH, "//a[contains(@href, '61c0c5a71d1f82001bdaaa75')]//p[contains(@class, 'counter__num')]")
    FILLING_COUNTER_1 = (By.XPATH, "//a[contains(@href, '61c0c5a71d1f82001bdaaa70')]//p[contains(@class, 'counter__num')]")
    FILLING_COUNTER_2 = (By.XPATH, "//a[contains(@href, '61c0c5a71d1f82001bdaaa77')]//p[contains(@class, 'counter__num')]")
    FILLING_COUNTER_3 = (By.XPATH, "//a[contains(@href, '61c0c5a71d1f82001bdaaa7a')]//p[contains(@class, 'counter__num')]")
