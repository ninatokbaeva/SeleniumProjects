from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select

class BasePage:

    def __init__(self, driver):
        driver = webdriver.Chrome()
        self.driver = driver
        self.wdwait = WebDriverWait(driver, 10)
    def click_element_by_id (self,id):
        #element = self.driver.find_element(By.ID, id)
        element = self.wdwait.until