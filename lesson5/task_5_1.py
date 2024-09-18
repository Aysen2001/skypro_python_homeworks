from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for _ in range(5):
    click_button = driver.find_element(
        By.CSS_SELECTOR, '[onclick="addElement()"]').click()
del_button = driver.find_elements(
        By.CSS_SELECTOR, '[onclick="deleteElement()"]')
print(
    f"Размер списка кнопок Delete: {len(del_button)}")

sleep(10)
