import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.PageShopAuth import PageShopAuth
from pages.PageShopProd import PageShopProd
from pages.PageShopCont import PageShopCont
from pages.PageShopInfo import PageShopInfo
from pages.PageShopTotal import PageShopTotal


@allure.title("Автотест на интернет-магазин")
@allure.description("Дымовое тестирование основных функций сайта")
@allure.feature("SHOP")
@allure.severity("CRITICAL")
def test_shop_03():
    with allure.step("Открыть страницу в Chrome"):
        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()))
        page_shop_auth = PageShopAuth(browser)
    with allure.step("Авторизация на сайте"):
        page_shop_auth.data_auth()
    with allure.step("Выбираем и добавляем продукты в корзину"):
        page_shop_prod = PageShopProd(browser)
        page_shop_prod.add_products()
    with allure.step("Переходим в корзину"):
        page_shop_prod.container()
    with allure.step("Подтвержаем выбор в корзине"):
        page_shop_cont = PageShopCont(browser)
        page_shop_cont.checkout()
    with allure.step("Вводим данные покупателя"):
        page_shop_info = PageShopInfo(browser)
        page_shop_info.data_name()
        page_shop_info.btn_continue()
    with allure.step("Получаем итоговую сумму"):
        page_shop_total = PageShopTotal(browser)
        total_sum = page_shop_total.total_sum()
    with allure.step("Проверяем итоговую сумму"):
        assert total_sum == 'Total: $58.29'
    with allure.step("Закрываем браузер"):
        browser.quit()
