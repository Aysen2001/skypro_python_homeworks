from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class PageCalc:
    """
    Класс PageCalc показывает работу калькулятора.
    Вывод ответа с задержкой.
    """
    def __init__(self, browser: str):
        """
        Специальная функция, которая вызывается при создании нового объекта
        класса. Запускает страницу Chrome на полное окно с ожиданием 4 сек.
        """
        self._driver = browser
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def delay(self):
        """
        Метод, вводящий новое время на ожидание получения результата.
        """
        input_delay = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        input_delay.clear()
        input_delay.send_keys("45")

    def btns_calc(self):
        """
        Метод, нажимающий на кнопки на калькуляторе.
        """
        input_7 = self._driver.find_element(By.XPATH, '//span[text()="7"]')
        input_7.click()
        input_p = self._driver.find_element(By.XPATH, '//span[text()="+"]')
        input_p.click()
        input_8 = self._driver.find_element(By.XPATH, '//span[text()="8"]')
        input_8.click()
        input_r = self._driver.find_element(By.XPATH, '//span[text()="="]')
        input_r.click()

    def wait_delay(self):
        """
        Метод, ожидающий выставленное время в Delay.
        """
        WebDriverWait(self._driver, 46).until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '[class="screen"]'), "15"
            )
        )

    def result(self):
        """
        Метод, получающий результат. Возвращает число.
        """
        res = self._driver.find_element(
            By.CSS_SELECTOR, '[class="screen"]').text
        return int(res)
