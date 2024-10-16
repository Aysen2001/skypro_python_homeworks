from selenium.webdriver.common.by import By


class PageShopTotal:
    """
    Класс PageShopTotal представляет вывод результата с ценой"
    """
    def __init__(self, browser: str):
        """
        Специальная функция, которая вызывается при создании
        нового объекта класса. Запускает страницу Chrome.
        """
        self._driver = browser

    def total_sum(self):
        """
        Метод, выводящий результат в текстовом формате.
        """
        txt = self._driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
        return str(txt)
