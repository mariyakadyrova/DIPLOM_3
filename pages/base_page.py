from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, base_url: str):
        self.driver = driver
        self.base_url = base_url.rstrip("/")
        self.wait = WebDriverWait(driver, 10)

    def open(self, path: str = "/"):
        self.driver.get(f"{self.base_url}{path}")

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def not_visible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()
        return el

    def safe_click(self, locator):
        # 1) закрыть overlay, если он есть
        self.close_modal_if_present()

        # 2) проскроллить к элементу
        self.scroll_into_view(locator)

        try:
            return self.click(locator)
        except ElementClickInterceptedException:
            # если снова перекрыли — пробуем закрыть overlay и кликнуть JS
            self.close_modal_if_present()
            return self.js_click(locator)

    def close_modal_if_present(self):
        """
        Если на странице есть overlay модалки — закрываем ESC.
        """
        try:
            self.wait.until(EC.presence_of_element_located(("css selector", "div.Modal_modal_overlay__x2ZCr")))
            self.driver.find_element("tag name", "body").send_keys(Keys.ESCAPE)
            self.wait.until(EC.invisibility_of_element_located(("css selector", "div.Modal_modal_overlay__x2ZCr")))
        except TimeoutException:
            pass

    def type(self, locator, text: str):
        el = self.find(locator)
        el.clear()
        el.send_keys(text)
        return el

    def scroll_into_view(self, locator):
        el = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", el)
        return el

    def js_click(self, locator):
        el = self.find(locator)
        self.driver.execute_script("arguments[0].click();", el)
        return el

    def close_modal_by_cross(self): #отдельный метод для закрытия модалки
        close_btn = (By.CSS_SELECTOR, "button.Modal_modal__close__TnseK")
        # ждём появление и видимость
        el = self.wait.until(EC.visibility_of_element_located(close_btn))
        # клик через JS — самый стабильный для крестиков в модалках
        self.driver.execute_script("arguments[0].click();", el)

    def clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def visible_with_timeout(self, locator, timeout: int):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_until_text_not_equal(self, locator, bad_text: str, timeout: int = 20):
        def _predicate(driver):
            text = driver.find_element(*locator).text.strip()
            return text and text != bad_text

        return WebDriverWait(self.driver, timeout).until(_predicate)