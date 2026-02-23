import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException

from pages.base_page import BasePage
from locators.header_locators import HeaderLocators
from locators.main_locators import MainPageLocators
from locators.modal_locators import ModalLocators, IngredientModalLocators, OrderModalLocators


class MainPage(BasePage):
    PATH = "/"

    @allure.step("Открыть главную страницу")
    def open_main(self):
        self.open(self.PATH)

    @allure.step("Перейти в 'Конструктор'")
    def go_to_constructor(self):
        self.safe_click(HeaderLocators.CONSTRUCTOR)

    @allure.step("Перейти в 'Лента заказов'")
    def go_to_feed(self):
        self.safe_click(HeaderLocators.FEED)

    @allure.step("Перейти в 'Личный кабинет'")
    def go_to_account(self):
        self.safe_click(HeaderLocators.PERSONAL_ACCOUNT)

    @allure.step("Клик по ингредиенту (открыть детали)")
    def open_ingredient_details(self):
        self.close_modal_if_present()
        self.safe_click(MainPageLocators.ANY_INGREDIENT_IMAGE)
        self.visible(IngredientModalLocators.TITLE)

    @allure.step("Закрыть модалку (крестик)")
    def close_modal(self):
        self.close_modal_by_cross()

    @allure.step("Перетащить первый ингредиент в конструктор")
    def drag_first_ingredient_to_constructor(self):
        source = self.find(MainPageLocators.ANY_INGREDIENT_IMAGE)
        target = self.find(MainPageLocators.CONSTRUCTOR_DROP_AREA)

        try:
            ActionChains(self.driver).drag_and_drop(source, target).perform()
            return
        except WebDriverException:
            pass

    @allure.step("Получить каунтер ингредиента (если есть)")
    def get_ingredient_counter_text_or_none(self):
        els = self.driver.find_elements(*MainPageLocators.INGREDIENT_COUNTER)
        return els[0].text if els else None

    @allure.step("Оформить заказ")
    def place_order(self):
        self.clickable(MainPageLocators.PLACE_ORDER_BUTTON).click()
        self.visible_with_timeout(ModalLocators.MODAL, 20)
        self.wait_until_text_not_equal(OrderModalLocators.ORDER_NUMBER, "9999", 20)

    @allure.step("Получить номер заказа из модалки")
    def get_order_number(self):
        self.wait_until_text_not_equal(OrderModalLocators.ORDER_NUMBER, "9999", 20)
        raw = self.driver.find_element(*OrderModalLocators.ORDER_NUMBER).text.strip()

        # убираем ведущие нули
        return str(int(raw))

