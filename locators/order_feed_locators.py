from selenium.webdriver.common.by import By

"""Локаторы для страницы ленты заказов"""

class OrderFeedLocators:
    # Счётчик "Выполнено за всё время" (первый по порядку)
    TOTAL_ORDERS_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[1]")

    # Счётчик "Выполнено за сегодня" (второй по порядку)
    TODAY_ORDERS_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]")

    # Раздел "В работе" — все номера заказов в этом разделе
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")

    # Заголовок страницы
    FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")

    # Надпись "Все текущие заказы готовы!"
    ALL_ORDERS_READY_MESSAGE = (By.XPATH, "//li[text()='Все текущие заказы готовы!']")
