import allure

from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from selenium.webdriver.support.ui import WebDriverWait


@allure.feature("Password recovery")
class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    def test_go_to_forgot_password_page(self, driver, base_url):
        login = LoginPage(driver, base_url)
        login.open_login()
        login.go_to_forgot_password()

        assert "/forgot-password" in driver.current_url

    @allure.title("Ввод почты и клик по кнопке 'Восстановить' ведут на reset-password")
    def test_restore_password_flow_goes_to_reset_password(self, driver, base_url, go_to_reset_password):
        assert "/reset-password" in driver.current_url

    @allure.title("Клик по показать/скрыть пароль делает поле пароля активным")
    def test_restore_password_flow_goes_to_reset_password(self, driver, base_url, go_to_reset_password):
        assert "/reset-password" in driver.current_url