import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.PageForm import PageForm


@allure.title("Автотест на заполнение формы")
@allure.description("Проверка корректной работы формы")
@allure.feature("FORM")
@allure.severity("NORMAL")
def test_form_01():
    with allure.step("Открыть страницу в Chrome"):
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        page_form = PageForm(browser)
    with allure.step("Заполняем форму"):
        page_form.fields()
        page_form.submit()
    with allure.step("Получаем и сохраняем данные о цвете полей"):
        color_fields = page_form.status_fields()
    with allure.step("Проверяем цвет полей"):
        assert color_fields == "rgba(209, 231, 221, 1)"
    with allure.step("Получаем и сохраняем данные о цвете поля Zip-code"):
        color_field_zip_cod = page_form.status_zip_code()
    with allure.step("Проверяем цвет поля Zip-code"):
        assert color_field_zip_cod == "rgba(248, 215, 218, 1)"
    with allure.step("Закрываем браузер"):
        browser.quit()
