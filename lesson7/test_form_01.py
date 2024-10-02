from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.PageForm import PageForm


def test_form_01(): 
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    page_form = PageForm(browser)
    page_form.fields()
    page_form.submit()
    color_fields = page_form.status_fields()
    assert color_fields == "rgba(209, 231, 221, 1)"
    color_field_zip_cod = page_form.status_zip_code()
    assert color_field_zip_cod == "rgba(248, 215, 218, 1)"
    browser.quit()
