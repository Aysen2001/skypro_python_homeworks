from selenium.webdriver.common.by import By


class PageShopProd:
    """
    Класс PageShopProd представляет страницу товаров
    с их последующим выбором"
    """
    def __init__(self, browser: str):  # открываем страницу товаров
        self._driver = browser
        """
        Специальная функция, которая вызывается при создании
        нового объекта класса. Запускает страницу Chrome.
        """

    def add_products(self):
        """
        Метод, выбирающий 3 продукта.
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    def container(self):
        """
        Метод, нажимающий на значок корзина.
        """
        self._driver.find_element(
            By.CSS_SELECTOR, "#shopping_cart_container").click()
