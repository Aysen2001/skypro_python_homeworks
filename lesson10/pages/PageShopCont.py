from selenium.webdriver.common.by import By


class PageShopCont:
    """
    Класс PageShopCont подтверждения выбора товаров в корзине,
    через кнопку Checkout"
    """
    def __init__(self, browser: str):
        """
        Специальная функция, которая вызывается при создании
        нового объекта класса. Запускает страницу Chrome.
        """
        self._driver = browser

    def checkout(self):
        """
        Метод, нажимающий на кнопку Checkout.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()
