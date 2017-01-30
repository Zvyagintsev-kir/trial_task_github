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
                until(EC.element_to_be_clickable((By.XPATH, self.locator)))
        else:
            return WebDriverWait(self.driver, self.timeout).\
                until(EC.element_to_be_clickable((By.ID, self.locator)))

    def click(self):
        self.find().click()

    def send_keys(self, keys):
        self.find().send_keys(keys)

    def get_text(self):
        return self.find().text