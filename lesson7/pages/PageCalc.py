from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class PageCalc:

    
    def __init__(self, browser): # открываем страницу
        self._driver = browser
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
        

    def delay(self): # вводим новое время на ожидание получения результата         
        input_delay = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        input_delay.clear()
        input_delay.send_keys("45")
            

    def btns_calc(self): # нажимаем кнопки на калькуляторе
        input_7 = self._driver.find_element(By.XPATH, '//span[text()="7"]')
        input_7.click()
        input_p = self._driver.find_element(By.XPATH, '//span[text()="+"]')
        input_p.click()
        input_8 = self._driver.find_element(By.XPATH, '//span[text()="8"]')
        input_8.click()
        input_r = self._driver.find_element(By.XPATH, '//span[text()="="]')
        input_r.click()
            

    def wait_delay(self): # Ожидание выставленное в Delay
        WebDriverWait(self._driver, 46).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[class="screen"]'), "15"))


    def result(self): # Получение результата
        res = self._driver.find_element(By.CSS_SELECTOR, '[class="screen"]').text
        return int(res)
        