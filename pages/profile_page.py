import allure
from pages.base_page import BasePage
from locators.profile_locators import ProfileLocators
from locators.feed_locators import OrderHistoryLocators
from selenium.webdriver.support.ui import WebDriverWait

class ProfilePage(BasePage):
    PROFILE_PATH = "/account/profile"
    HISTORY_PATH = "/account/order-history"

    @allure.step("Ожидать, что открыта страница профиля")
    def assert_profile_opened(self):
        WebDriverWait(self.driver, 10).until(lambda d: "/account/profile" in d.current_url)
        assert "/account/profile" in self.driver.current_url

    @allure.step("Перейти в историю заказов")
    def go_to_order_history(self):
        self.safe_click(ProfileLocators.ORDER_HISTORY_LINK)

    @allure.step("Ожидать, что открыта история заказов")
    def assert_history_opened(self):
        assert "/account/order-history" in self.driver.current_url

    @allure.step("Выйти из аккаунта")
    def logout(self):
        self.safe_click(ProfileLocators.LOGOUT_BUTTON)
        WebDriverWait(self.driver, 10).until(lambda d: "/login" in d.current_url)

    @allure.step("Получить номер первого заказа в истории")
    def get_first_order_number(self) -> str:
        text = self.visible(OrderHistoryLocators.FIRST_ORDER_NUMBER).text  # "#0353837"
        raw = text.replace("#", "").strip()
        return str(int(raw))  # "353837"

