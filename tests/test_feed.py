import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage
from locators.feed_locators import OrderHistoryLocators


@allure.feature("Feed")
@allure.title("функционал на стр создания заказа")
class TestFeed:

    @allure.title("открытие модалки созданного заказа")
    def test_order_modal_opens(self, driver, base_url):
        feed = FeedPage(driver, base_url)
        feed.open_feed()
        assert feed.open_first_order()

    @allure.title("Заказ из истории отображается в ленте заказов")
    def test_orders_from_history_visible_in_feed(self, driver, base_url, auth_user):
        # 1) создаём заказ
        main = MainPage(driver, base_url)
        main.open_main()
        main.drag_first_ingredient_to_constructor()
        main.place_order()

        order_number = main.get_order_number()  # "353921"
        main.close_modal()

        # 2) идём в личный кабинет -> история заказов
        main.go_to_account()
        profile = ProfilePage(driver, base_url)
        profile.go_to_order_history()

        history_number = profile.get_first_order_number()
        assert history_number == order_number

        # 3) проверяем, что этот заказ есть в ленте
        feed = FeedPage(driver, base_url)
        feed.open_feed()

        assert feed.visible(OrderHistoryLocators.FIRST_ORDER_NUMBER)

        feed_number = f"#{order_number.zfill(7)}"  # "#0353921"
        assert feed.wait_order_present(feed_number)

    @allure.title("каунтер повысился после добавления нового заказа")
    def test_done_counters_increase_after_new_order(self, driver, base_url, auth_user):
        feed = FeedPage(driver, base_url)
        feed.open_feed()
        all_before = feed.get_done_all_time()
        today_before = feed.get_done_today()

        # создаём новый заказ
        main = MainPage(driver, base_url)
        main.open_main()
        main.drag_first_ingredient_to_constructor()
        main.place_order()
        main.close_modal()

        # возвращаемся в ленту и ждём роста счётчиков
        feed.open_feed()
        assert feed.wait_done_all_time_at_least(all_before)
        assert feed.wait_done_today_at_least(today_before)

        assert feed.get_done_all_time() >= all_before
        assert feed.get_done_today() >= today_before

    @allure.title("в блоке В работе появился новый заказ")
    def test_new_order_number_appears_in_in_work(self, driver, base_url, auth_user):
        main = MainPage(driver, base_url)
        main.open_main()
        main.drag_first_ingredient_to_constructor()
        main.place_order()
        order_number = main.get_order_number()
        main.close_modal()

        feed = FeedPage(driver, base_url)
        feed.open_feed()

        # ждём, что заказ появится в "В работе" (или быстро уйдет в "Готовы")
        assert feed.wait_order_in_work_or_ready(order_number)

        # проверяем "В работе"
        assert feed.is_order_in_work(order_number) or feed.is_order_ready(order_number)
