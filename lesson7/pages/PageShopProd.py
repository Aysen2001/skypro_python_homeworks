from selenium.webdriver.common.by import By

class PageShopProd:

    
    def __init__(self, browser): # открываем страницу товаров
        self._driver = browser
          

    def add_products(self):
        self._driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        

    def container(self):
        self._driver.find_element(
        By.CSS_SELECTOR, "#shopping_cart_container").click()
