from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_02_calc():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # вводим новое время на ожидание получения результата
    input_delay = driver.find_element(By.CSS_SELECTOR, "#delay")
    input_delay.clear()
    input_delay.send_keys("45")

    # нажимаем кнопки на калькуляторе
    input_7 = driver.find_element(By.XPATH, '//span[text()="7"]')
    input_7.click()
    input_p = driver.find_element(By.XPATH, '//span[text()="+"]')
    input_p.click()
    input_8 = driver.find_element(By.XPATH, '//span[text()="8"]')
    input_8.click()
    input_r = driver.find_element(By.XPATH, '//span[text()="="]')
    input_r.click()
    
    WebDriverWait(driver, 46).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[class="screen"]'), "15"))
    
    res = driver.find_element(By.CSS_SELECTOR, '[class="screen"]').text

    driver.quit()
    assert res == '15'
   