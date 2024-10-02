from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_03_shop():

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()

    # заполняем форму для входа на сайт
    driver.get("https://www.saucedemo.com/")
    input_username = driver.find_element(By.CSS_SELECTOR, "#user-name")
    input_username.clear()
    input_username.send_keys("standard_user")
    input_pass = driver.find_element(By.CSS_SELECTOR, "#password")
    input_pass.clear()
    input_pass.send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    # выбираем товар и переходим в корзину
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"
    ).click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
    ).click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"
    ).click()
    driver.find_element(
        By.CSS_SELECTOR, "#shopping_cart_container"
    ).click()

    # заполняем форму для покупки товара
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    input_first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
    input_first_name.clear()
    input_first_name.send_keys("Aysen")

    input_last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    input_last_name.clear()
    input_last_name.send_keys("Ivanov")

    input_postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    input_postal_code.clear()
    input_postal_code.send_keys("478788")

    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    txt_total_sum = driver.find_element(
        By.CSS_SELECTOR, "div.summary_total_label").text

    print(txt_total_sum)

    driver.quit()

    assert txt_total_sum == "Total: $58.29"
