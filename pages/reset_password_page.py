import allure
from pages.base_page import BasePage
from locators.auth_locators import ResetPasswordPageLocators

class ResetPasswordPage(BasePage):
    PATH = "/reset-password"

    @allure.step("Открыть страницу reset-password")
    def open_reset_password(self):
        self.open(self.PATH)

    @allure.step("Клик по иконке показать/скрыть пароль")
    def click_eye(self):
        self.close_modal_if_present()
        self.safe_click(ResetPasswordPageLocators.PASSWORD_EYE_BUTTON)

    @allure.step("Проверить, что поле пароля активно (в фокусе)")
    def is_password_focused(self) -> bool:
        pwd = self.find(ResetPasswordPageLocators.PASSWORD_INPUT)
        return self.driver.switch_to.active_element == pwd