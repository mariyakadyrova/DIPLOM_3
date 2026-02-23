from selenium.webdriver.common.by import By


class FeedLocators:
    FIRST_ORDER_LINK = (By.CSS_SELECTOR, "li.OrderHistory_listItem__2x95r a.OrderHistory_link__1iNby")
    DONE_ALL_TIME_VALUE = (By.XPATH, '//p[normalize-space()="Выполнено за все время:"]/following-sibling::p')
    DONE_TODAY_VALUE = (By.XPATH, '//p[normalize-space()="Выполнено за сегодня:"]/following-sibling::p')

    IN_WORK_LIST_ITEMS = (By.CSS_SELECTOR, 'ul.OrderFeed_orderListReady__1YFem li')
    READY_LIST_ITEMS = (By.CSS_SELECTOR, 'ul.OrderFeed_orderList__cBvyi li')


class OrderHistoryLocators:
    # первый заказ в истории (номер вида #0353837)
    FIRST_ORDER_NUMBER = (By.CSS_SELECTOR, "p.text.text_type_digits-default")
