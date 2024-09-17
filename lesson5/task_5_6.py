import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")
input_username = driver.find_element(By.ID, "username").send_keys("tomsmith")
time.sleep(2)
input_password = driver.find_element(By.ID, "password").send_keys(
    "SuperSecretPassword!")
time.sleep(2)
button = driver.find_element(By.TAG_NAME, "button").click()
time.sleep(2)
