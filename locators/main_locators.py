from selenium.webdriver.common.by import By


class MainPageLocators:
    # кликаем по любому ингредиенту (картинка)
    ANY_INGREDIENT_IMAGE = (By.CSS_SELECTOR, "img.BurgerIngredient_ingredient__image__3e-07")

    # зона конструктора (куда дропаем)
    CONSTRUCTOR_DROP_AREA = (By.CSS_SELECTOR, 'ul[class^="BurgerConstructor_basket__list"]')

    # кнопка "Оформить заказ"
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[normalize-space()="Оформить заказ"]')

    # каунтер на карточке ингредиента
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, "p.counter_counter__num__3nue1")


class OrderModalLocators:
    ORDER_NUMBER = (By.CSS_SELECTOR, "h2.Modal_modal__title__2L34m")