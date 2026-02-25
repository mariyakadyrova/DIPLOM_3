from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    # /forgot-password
    EMAIL_INPUT = (By.NAME, "name")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

    # /reset-password
    NEW_PASSWORD_INPUT = (By.NAME, "Введите новый пароль")
    CODE_INPUT = (By.NAME, "name")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    SHOW_HIDE_ICON = (By.CSS_SELECTOR, ".input__icon")