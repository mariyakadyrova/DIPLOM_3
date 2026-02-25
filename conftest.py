
#PASSED

import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait

from api.helpers import create_user, delete_user
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage

BASE_URL_UI = "https://stellarburgers.education-services.ru"


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1280,900")
        drv = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
    else:
        options = FirefoxOptions()
        drv = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options
        )
        drv.set_window_size(1280, 900)

    yield drv
    drv.quit()


@pytest.fixture()
def base_url():
    return BASE_URL_UI


@pytest.fixture()
def test_user():
    user = create_user()
    yield user
    delete_user(user["accessToken"])


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(autouse=True)
def attach_screenshot_on_fail(request, driver):
    yield
    rep = getattr(request.node, "rep_call", None)
    if rep and rep.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG,
        )

@pytest.fixture()
def go_to_reset_password(driver, base_url):
    login = LoginPage(driver, base_url)
    login.open_login()
    login.go_to_forgot_password()

    forgot = ForgotPasswordPage(driver, base_url)
    forgot.enter_email("test@example.com")
    forgot.click_restore()

    WebDriverWait(driver, 10).until(lambda d: "/reset-password" in d.current_url)
    return True

@pytest.fixture()
def auth_user(driver, base_url, test_user):
    login = LoginPage(driver, base_url)
    login.open_login()
    login.login(test_user["email"], test_user["password"])

    # ждём, что нас НЕ оставило на /login (то есть логин прошёл)
    WebDriverWait(driver, 10).until(lambda d: "/login" not in d.current_url)
    return test_user

