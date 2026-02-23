import allure
from pages.base_page import BasePage
from locators.feed_locators import FeedLocators, OrderHistoryLocators
from locators.modal_locators import ModalLocators, OrderModalLocators


class FeedPage(BasePage):
    PATH = "/feed"

    @allure.step("Открыть ленту заказов")
    def open_feed(self):
        self.open(self.PATH)

    @allure.step("Открыть первый заказ из ленты")
    def open_first_order(self):
        # 1) дождаться, что список заказов появился
        self.visible(OrderHistoryLocators.FIRST_ORDER_NUMBER)

        # 2) кликнуть по первому заказу (лучше через "clickable")
        self.clickable(OrderHistoryLocators.FIRST_ORDER_NUMBER).click()

        # 3) дождаться модалки (лучше сначала контейнер/заголовок модалки)
        self.visible(ModalLocators.MODAL)

        # 4) и уже потом номер внутри
        self.visible(OrderModalLocators.ORDER_NUMBER)

    @allure.step("Закрыть модалку")
    def close_modal(self):
        self.safe_click(ModalLocators.CLOSE_BUTTON)

    @allure.step("Получить 'Выполнено за все время'")
    def get_done_all_time(self) -> int:
        return int(self.visible(FeedLocators.DONE_ALL_TIME_VALUE).text)

    @allure.step("Получить 'Выполнено за сегодня'")
    def get_done_today(self) -> int:
        return int(self.visible(FeedLocators.DONE_TODAY_VALUE).text)

    @allure.step("Проверить, что номер есть в блоке 'В работе'")
    def is_order_in_work(self, order_number: str) -> bool:
        items = self.driver.find_elements(*FeedLocators.IN_WORK_LIST_ITEMS)
        return any(order_number in el.text for el in items)

    @allure.step("Проверить, что номер есть в блоке 'Готовы'")
    def is_order_ready(self, order_number: str) -> bool:
        items = self.driver.find_elements(*FeedLocators.READY_LIST_ITEMS)
        return any(order_number in el.text for el in items)

    @allure.step("Проверить, что заказ с номером есть в ленте")
    def is_order_present(self, feed_number: str) -> bool:
        locator = (By.XPATH, f"//p[contains(@class,'text_type_digits-default') and normalize-space()='{feed_number}']")
        self.visible(locator)
        return True