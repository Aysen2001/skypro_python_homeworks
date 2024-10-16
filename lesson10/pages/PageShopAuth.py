from selenium.webdriver.common.by import By


class PageShopAuth:
    """
    Класс PageShopAuth авторизации на сайте "https://www.saucedemo.com/"
    """
    def __init__(self, browser: str):
        """
        Специальная функция, которая вызывается при создании нового объекта
        класса. Запускает страницу Chrome на полное окно с ожиданием 4 сек.
        """
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def data_auth(self):
        """
        Метод, вводящий данные для авторизации
        """
        input_username = self._driver.find_element(
            By.CSS_SELECTOR, "#user-name")
        input_username.clear()
        input_username.send_keys("standard_user")
        input_pass = self._driver.find_element(By.CSS_SELECTOR, "#password")
        input_pass.clear()
        input_pass.send_keys("secret_sauce")
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()
