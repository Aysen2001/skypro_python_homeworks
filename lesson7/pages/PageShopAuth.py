from selenium.webdriver.common.by import By

class PageShopAuth:

    
    def __init__(self, browser): # открываем страницу
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
        

    def data_auth(self): # вводим данные для авторизации   
        input_username = self._driver.find_element(By.CSS_SELECTOR, "#user-name")
        input_username.clear()
        input_username.send_keys("standard_user")
        input_pass = self._driver.find_element(By.CSS_SELECTOR, "#password")
        input_pass.clear()
        input_pass.send_keys("secret_sauce")
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()
                    