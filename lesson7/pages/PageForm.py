from selenium.webdriver.common.by import By

class PageForm:

    
    def __init__(self, browser): # открываем страницу
        self._driver = browser
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()
        self._fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }


    def fields(self): # вставляем данные в поля
        
        for field_name, value in self._fields.items():
            self._driver.find_element(
                By.CSS_SELECTOR, f"input[name='{field_name}']").send_keys(value)
            

    def submit(self): # нажимаем кнопку Submit
        self._driver.find_element(
            By.CSS_SELECTOR, 'button[type="submit"]').click()
            

    def status_fields(self): # Проверяем статусы полей
        for field_name in self._fields.keys() :
            color_fields = self._driver.find_element(By.CSS_SELECTOR, 
                f"#{field_name}").value_of_css_property(
                    "background-color")
        return str(color_fields)


    def status_zip_code(self): # Проверяем статус поля Zip code
        color_field_zip_cod = self._driver.find_element(
            By.CSS_SELECTOR, '#zip-code').value_of_css_property("background-color")
        return str(color_field_zip_cod)
        