# Diplom_3
# Дипломный проект. 3 задание


## Описание проекта
Автоматизация тестирования учебного сервиса [Stellar Burgers](https://stellarburgers.education-services.ru/).  


## Структура проекта
Diplom_3/
├── pages/                              # Page Object классы
│ ├── base_page.py                      # Базовый класс для всех страниц
│ ├── main_page.py                      # Главная страница (конструктор)
│ ├── login_page.py                     # Страница авторизации
│ ├── order_feed_page.py                # Страница ленты заказов
│ ├── order_modal_page.py               # Модальное окно заказа
│ └── ingredient_modal_page.py          # Модальное окно ингредиента
│
├── locators/                           # Локаторы элементов
│ ├── main_page_locators.py
│ ├── login_page_locators.py
│ ├── order_feed_locators.py
│ ├── order_modal_locators.py
│ └── ingredient_modal_locators.py
│
├── tests/                              # Тесты
│ ├── test_constructor.py               # Тесты конструктора
│ └── test_order_feed.py                # Тесты ленты заказов
│
├── conftest.py                         # Фикстуры pytest
├── constants.py                        # Константы
├── requirements.txt                    # Зависимости
└── README.md                           # Документация


## Тестовые сценарии
### Конструктор
- ✅ Переход по клику на «Конструктор»
- ✅ Переход по клику на «Лента заказов»
- ✅ Открытие модального окна при клике на ингредиент
- ✅ Закрытие модального окна кликом по крестику
- ✅ Увеличение счётчика при добавлении ингредиента

### Лента заказов
- ✅ Увеличение счётчика «Выполнено за всё время» после создания заказа
- ✅ Увеличение счётчика «Выполнено за сегодня» после создания заказа
- ✅ Появление номера заказа в разделе «В работе»


## Технологии
- Python 3.14
- Selenium 4.15.0
- Pytest 7.4.3
- Allure 2.13.2
- WebDriver Manager 4.0.1


## Запуск всех тестов
py -m pytest tests -v

## Генерация Allure-отчёта
py -m pytest tests --alluredir=allure-results
allure serve allure-results
