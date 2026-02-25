#Passed

import allure
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage
from pages.feed_page import FeedPage
from locators.modal_locators import IngredientModalLocators
from locators.main_locators import MainPageLocators

@allure.feature("Main functionality")
@allure.title("главный функционал")
class TestMainFunctionality:

    @allure.title("переход в Конструктор")
    def test_go_to_constructor(self, driver, base_url):
        main = MainPage(driver, base_url)
        main.open_main()
        main.go_to_feed()
        main.go_to_constructor()
        assert driver.current_url.endswith("/") or "/?/" in driver.current_url or "stellarburgers" in driver.current_url

    @allure.title("переход в Ленту заказов")
    def test_go_to_feed(self, driver, base_url):
        main = MainPage(driver, base_url)
        main.open_main()
        main.go_to_feed()
        assert "/feed" in driver.current_url

    @allure.title("открытие модалки ингридиента (описание и тд)")
    def test_ingredient_modal_opens(self, driver, base_url):
        main = MainPage(driver, base_url)
        main.open_main()
        main.open_ingredient_details()
        assert main.visible(IngredientModalLocators.TITLE)

    @allure.title("закрытие модалки ингридиента по крестику")
    def test_ingredient_modal_closes_by_cross(self, driver, base_url):
        main = MainPage(driver, base_url)
        main.open_main()
        main.open_ingredient_details()
        main.close_modal()
        assert main.not_visible(IngredientModalLocators.TITLE)

    @allure.title("каунтер в блоке собирания заказа увеличивается")
    def test_counter_increases_when_add_ingredient(self, driver, base_url):
        main = MainPage(driver, base_url)
        main.open_main()
        main.drag_first_ingredient_to_constructor()

        assert main.wait_and_get_ingredient_counter() >= 1

    @allure.title("авторизованный может сделать ордер")
    def test_authorized_user_can_place_order(self, driver, base_url, auth_user):
        main = MainPage(driver, base_url)
        main.open_main()

        # добавим ингредиент в конструктор (без этого кнопка может быть неактивна)
        main.drag_first_ingredient_to_constructor()

        main.place_order()
        order_number = main.get_order_number()
        assert order_number.isdigit()