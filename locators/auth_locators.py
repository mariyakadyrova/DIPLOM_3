from selenium.webdriver.common.by import By


class LoginPageLocators:
    # ссылка "Восстановить пароль"
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, 'a.Auth_link__1fOlj[href="/forgot-password"]')


class ForgotPasswordPageLocators:
    # input Email (placeholder label "Email")
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    # кнопка "Восстановить"
    RESTORE_BUTTON = (By.XPATH, '//button[contains(@class,"button_button_type_primary") and normalize-space()="Восстановить"]')


class ResetPasswordPageLocators:
    CODE_INPUT = (By.XPATH, '//label[contains(text(),"Введите код из письма")]/following-sibling::input')

    PASSWORD_INPUT = (By.XPATH, '//label[normalize-space()="Пароль"]/following-sibling::input')

    # eye-кнопка именно внутри блока пароля "Пароль"
    PASSWORD_EYE_BUTTON = (
        By.XPATH,
        '//label[normalize-space()="Пароль"]/following-sibling::input/following-sibling::div[contains(@class,"input__icon-action")]'
    )

    SAVE_BUTTON = (By.XPATH, '//button[normalize-space()="Сохранить"]')

class AuthFormLocators:
    EMAIL_INPUT = (By.XPATH, '//label[normalize-space()="Email"]/following-sibling::input')
    PASSWORD_INPUT = (By.XPATH, '//label[normalize-space()="Пароль"]/following-sibling::input')
    LOGIN_BUTTON = (By.XPATH, '//button[normalize-space()="Войти"]')