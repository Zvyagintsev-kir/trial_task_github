from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class WebElement(object):
    def __init__(self, driver, locator_type, locator, timeout=10):
        self.driver = driver
        self.locator_type = locator_type
        self.locator = locator
        self.timeout = timeout

    def find(self):
        if self.locator_type == "xpath":
            return WebDriverWait(self.driver, self.timeout).\
                until(EC.presence_of_all_elements_located((By.XPATH, self.locator)))
        else:
            return WebDriverWait(self.driver, self.timeout).\
                until(EC.presence_of_all_elements_located((By.ID, self.locator)))

    def click(self):
        self.find().click()