from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.PageShopAuth import PageShopAuth
from pages.PageShopProd import PageShopProd
from pages.PageShopCont import PageShopCont
from pages.PageShopInfo import PageShopInfo
from pages.PageShopTotal import PageShopTotal


def test_shop_03():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    page_shop_auth = PageShopAuth(browser)
    page_shop_auth.data_auth()

    page_shop_prod = PageShopProd(browser)
    page_shop_prod.add_products()
    page_shop_prod.container()

    page_shop_cont = PageShopCont(browser)
    page_shop_cont.checkout()

    page_shop_info = PageShopInfo(browser)
    page_shop_info.data_name()
    page_shop_info.btn_continue()

    page_shop_total = PageShopTotal(browser)
    total_sum = page_shop_total.total_sum()
    assert total_sum == 'Total: $58.29'
    browser.quit()
