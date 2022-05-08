from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Wdriver package, webdriver_class.py module
# WDRIVER CLASS
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20) # max wait time for all find element steps

driver.get("https://demoqa.com/browser-windows")
time.sleep(2)

# properties for WebDriver class
print("driver.current_url:", driver.current_url)
print("driver.current_window_handle:",driver.current_window_handle)
time.sleep(2)

#driver.find_element(By.XPATH, "//button[@id='tabButton']")
#driver.find_element(By.CSS_SELECTOR)

print("driver.window_handles:", driver.window_handles)


