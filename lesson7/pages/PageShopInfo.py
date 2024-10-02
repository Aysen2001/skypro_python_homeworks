from selenium.webdriver.common.by import By


class PageShopInfo:
    def __init__(self, browser):
        self._driver = browser

    def data_name(self):
        input_first_name = self._driver.find_element(
            By.CSS_SELECTOR, "#first-name")
        input_first_name.clear()
        input_first_name.send_keys("Aysen")

        input_last_name = self._driver.find_element(
            By.CSS_SELECTOR, "#last-name")
        input_last_name.clear()
        input_last_name.send_keys("Ivanov")

        input_postal_code = self._driver.find_element(
            By.CSS_SELECTOR, "#postal-code")
        input_postal_code.clear()
        input_postal_code.send_keys("478788")

    def btn_continue(self):
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()
