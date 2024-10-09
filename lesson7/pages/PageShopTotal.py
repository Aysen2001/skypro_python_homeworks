from selenium.webdriver.common.by import By


class PageShopTotal:
    def __init__(self, browser):
        self._driver = browser

    def total_sum(self):
        txt = self._driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
        return str(txt)
