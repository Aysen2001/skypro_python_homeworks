import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.PageCalc import PageCalc


@allure.title("Автотест на калькулятор")
@allure.description("Проверка работы калькулятора")
@allure.feature("CALCULATOR")
@allure.severity("BLOCKER")
def test_calc_02():
    with allure.step("Открыть страницу в Chrome"):
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        page_calc = PageCalc(browser)
    with allure.step("Вводим новое время ожидания"):
        page_calc.delay()
    with allure.step("Нажимаем на кнопки калькулятора"):
        page_calc.btns_calc()
        page_calc.wait_delay()
    with allure.step("Сохраняем результат"):
        res = page_calc.result()
    with allure.step("Проверяем полученный результат"):
        assert res == 15
    with allure.step("Закрываем браузер"):
        browser.quit()
