from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
time.sleep(5)

search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys("selenium")
search_box.send_keys(Keys.ENTER)

driver.close()
