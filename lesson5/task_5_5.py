import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")
input_tekst = driver.find_element(By.TAG_NAME, "input")
input_tekst.send_keys("1000")
time.sleep(2)
input_tekst.clear()
time.sleep(2)
input_tekst.send_keys("999")
time.sleep(2)
