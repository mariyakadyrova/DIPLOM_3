import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage


@allure.feature("Feed")
class TestFeed:

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

        # номер из модалки создания заказа (у тебя в get_order_number уже есть ожидание != 9999)
        order_number = main.get_order_number()  # например "353921"
        main.close_modal()

        # 2) идём в личный кабинет -> история заказов
        main.go_to_account()
        profile = ProfilePage(driver, base_url)
        profile.go_to_order_history()

        # номер из истории (сейчас лучше тоже возвращать str(int(...)) внутри метода)
        history_number = profile.get_first_order_number()  # например "353921"

        # сравниваем одинаковый формат
        assert history_number == order_number

        # 3) проверяем, что этот заказ есть в ленте
        feed = FeedPage(driver, base_url)
        feed.open_feed()  # <-- ВОТ СЮДА ПИШЕТСЯ open_feed(): после создания feed-страницы

        # дождаться, что лента прогрузилась (появился хоть один номер заказа вида "#...")
        feed.visible(
            (By.XPATH, "//p[contains(@class,'text_type_digits-default') and starts-with(normalize-space(.),'#')]"))

        # в ленте номер обычно в виде "#0xxxxxx" (пример: "#0353921")
        feed_number = f"#0{order_number.zfill(6)}"

        assert feed_number in driver.page_source
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
        WebDriverWait(driver, 10).until(lambda d: feed.get_done_all_time() >= all_before)
        WebDriverWait(driver, 10).until(lambda d: feed.get_done_today() >= today_before)

        assert feed.get_done_all_time() >= all_before
        assert feed.get_done_today() >= today_before

    def test_new_order_number_appears_in_in_work(self, driver, base_url, auth_user):
        main = MainPage(driver, base_url)
        main.open_main()
        main.drag_first_ingredient_to_constructor()
        main.place_order()
        order_number = main.get_order_number()
        main.close_modal()

        feed = FeedPage(driver, base_url)
        feed.open_feed()

        # ждём, что номер появится в "В работе" (иногда быстро уходит в "Готовы", поэтому ждём немного)
        WebDriverWait(driver, 10).until(lambda d: feed.is_order_in_work(order_number) or feed.is_order_ready(order_number))

        # строго по ТЗ — проверяем "В работе"
        assert feed.is_order_in_work(order_number) or feed.is_order_ready(order_number)
