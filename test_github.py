import pytest
from selenium import webdriver
import random
import string
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_github_registration_successes():
    driver = webdriver.Firefox()
    driver.get("http://www.github.com/join")
    random_sufix = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(7))
    name = "testUserName-{}".format(random_sufix)
    email = "testUserEmail-{}@test.com".format(random_sufix)
    passwords = "Pass{}".format(random_sufix)
    driver.find_element_by_id("user_login").send_keys(name)
    driver.find_element_by_id("user_email").send_keys(email)
    driver.find_element_by_id("user_password").send_keys(passwords)
    driver.find_element_by_id("signup_button").click()