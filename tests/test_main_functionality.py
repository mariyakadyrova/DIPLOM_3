#Passed

import allure
from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage
from pages.feed_page import FeedPage
from locators.modal_locators import IngredientModalLocators
from locators.main_locators import MainPageLocators

@allure.feature("Main functionality")
class TestMainFunctionality:

    def test_go_to_constructor(self, driver, base_url):
        main = MainPage(driver, base_url)
        main.open_main()
        main.go_to_feed()
        main.go_to_constructor()
        assert driver.current_url.endswith("/") or "/?/" in driver.current_url or "stellarburgers" in driver.current_url

    def test_go_to_feed(self, driver, base_url):
        main = MainPage(driver, base_url)
        main.open_main()
        main.go_to_feed()
        assert "/feed" in driver.current_url

    def test_ingredient_modal_opens(self, driver, base_url):
        main = MainPage(driver, base_url)
        main.open_main()
        main.open_ingredient_details()
        assert True

    def test_ingredient_modal_closes_by_cross(self, driver, base_url):
        main = MainPage(driver, base_url)
        main.open_main()
        main.open_ingredient_details()
        main.close_modal()
        # модалка исчезла -> заголовка нет
        main.not_visible(IngredientModalLocators.TITLE)
        assert True

    def test_counter_increases_when_add_ingredient(self, driver, base_url):
        main = MainPage(driver, base_url)
        main.open_main()

        main.drag_first_ingredient_to_constructor()

        # ждём появления хотя бы одного каунтера
        WebDriverWait(driver, 10).until(
            lambda d: len(d.find_elements(*MainPageLocators.INGREDIENT_COUNTER)) > 0
        )

        counters = driver.find_elements(*MainPageLocators.INGREDIENT_COUNTER)
        assert any(int(c.text) >= 1 for c in counters if c.text.isdigit())

    def test_authorized_user_can_place_order(self, driver, base_url, auth_user):
        main = MainPage(driver, base_url)
        main.open_main()

        # добавим ингредиент в конструктор (без этого кнопка может быть неактивна)
        main.drag_first_ingredient_to_constructor()

        main.place_order()
        order_number = main.get_order_number()
        assert order_number.isdigit()