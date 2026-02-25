import allure
from pages.base_page import BasePage
from locators.auth_locators import ForgotPasswordPageLocators

class ForgotPasswordPage(BasePage):
    PATH = "/forgot-password"

    @allure.step("Открыть страницу восстановления пароля")
    def open_forgot_password(self):
        self.open(self.PATH)

    @allure.step("Ввести email для восстановления")
    def enter_email(self, email: str):
        self.type(ForgotPasswordPageLocators.EMAIL_INPUT, email)

    @allure.step("Нажать кнопку 'Восстановить'")
    def click_restore(self):
        self.safe_click(ForgotPasswordPageLocators.RESTORE_BUTTON)