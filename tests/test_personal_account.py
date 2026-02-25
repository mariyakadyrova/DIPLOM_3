#PASSED


import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


@allure.feature("Personal account")
@allure.title("блоки в ЛК")
class TestPersonalAccount:

    @allure.title("открыть ЛК")
    def test_go_to_personal_account(self, driver, base_url, auth_user):
        main = MainPage(driver, base_url)
        main.open_main()
        main.go_to_account()

        profile = ProfilePage(driver, base_url)
        profile.assert_profile_opened()

    @allure.title("открыть Историю заказов")
    def test_go_to_order_history(self, driver, base_url, auth_user):
        main = MainPage(driver, base_url)
        main.open_main()
        main.go_to_account()

        profile = ProfilePage(driver, base_url)
        profile.go_to_order_history()
        profile.assert_history_opened()

    @allure.title("выйти из аккаунта/деавторизация")
    def test_logout(self, driver, base_url, auth_user):
        main = MainPage(driver, base_url)
        main.open_main()
        main.go_to_account()

        profile = ProfilePage(driver, base_url)
        profile.logout()

        assert "/login" in driver.current_url

