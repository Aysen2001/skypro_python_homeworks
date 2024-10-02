from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.PageCalc import PageCalc


def test_calc_02():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    page_calc = PageCalc(browser)
    page_calc.delay()
    page_calc.btns_calc()
    page_calc.wait_delay()
    res = page_calc.result()
    assert res == 15
    browser.quit()
