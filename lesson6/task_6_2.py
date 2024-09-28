from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://uitestingplayground.com/textinput")
name = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
name.send_keys("SkyPro")

click_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
txt_new_buton = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(txt_new_buton)

driver.quit()
