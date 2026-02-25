import allure
from pages.base_page import BasePage
from locators.auth_locators import LoginPageLocators, AuthFormLocators


class LoginPage(BasePage):
    PATH = "/login"

    @allure.step("Открыть страницу логина")
    def open_login(self):
        self.open(self.PATH)

    @allure.step("Перейти по ссылке 'Восстановить пароль'")
    def go_to_forgot_password(self):
        self.close_modal_if_present()
        self.safe_click(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Выполнить логин")
    def login(self, email: str, password: str):
        self.type(AuthFormLocators.EMAIL_INPUT, email)
        self.type(AuthFormLocators.PASSWORD_INPUT, password)
        self.safe_click(AuthFormLocators.LOGIN_BUTTON)