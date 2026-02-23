from selenium.webdriver.common.by import By


class HeaderLocators:
    # кнопка/ссылка "Личный кабинет" (по тексту)
    PERSONAL_ACCOUNT = (By.XPATH, '//p[normalize-space()="Личный Кабинет"]')

    # "Лента заказов"
    FEED = (By.XPATH, '//p[normalize-space()="Лента Заказов"]')

    # "Конструктор"
    CONSTRUCTOR = (By.XPATH, '//p[normalize-space()="Конструктор"]')
