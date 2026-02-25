from selenium.webdriver.common.by import By


class ModalLocators:
    # Универсальный крестик закрытия модалки (ингредиенты/заказ)
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button.Modal_modal__close__TnseK")
    # модалка созданного заказа в feed
    MODAL = (By.CSS_SELECTOR, "div.Modal_modal__contentBox__sCy8X")


class IngredientModalLocators:
    TITLE = (By.XPATH, '//h2[normalize-space()="Детали ингредиента"]')


class OrderModalLocators:
    # номер заказа в модалке (digits-large)
    ORDER_NUMBER = (By.CSS_SELECTOR, "div.Modal_modal__contentBox__sCy8X h2.Modal_modal__title__2L34m")