from selenium.webdriver.common.by import By


class ProfileLocators:
    # "История заказов"
    ORDER_HISTORY_LINK = (By.CSS_SELECTOR, 'a[href="/account/order-history"]')

    # кнопка "Выход"
    LOGOUT_BUTTON = (By.XPATH, '//button[normalize-space()="Выход"]')
