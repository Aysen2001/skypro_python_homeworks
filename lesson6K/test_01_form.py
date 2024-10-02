from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_01_form():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполняем форму
    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro",
    }

    for field_name, value in fields.items():
        field = driver.find_element(
            By.CSS_SELECTOR, f"input[name='{field_name}']")
        field.send_keys(value)

    # Нажимаем кнопку Submit
    submit_button = driver.find_element(
        By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()

    # Проверяем статусы полей
    for field_name in fields.keys():
        field = driver.find_element(
            By.CSS_SELECTOR, f"#{field_name}"
        ).value_of_css_property("background-color")
        assert field == "rgba(209, 231, 221, 1)"

    # Проверяем статус поля Zip code
    color_field_zip_cod = driver.find_element(
        By.CSS_SELECTOR, "#zip-code"
    ).value_of_css_property("background-color")

    assert color_field_zip_cod == "rgba(248, 215, 218, 1)"
    driver.quit()
