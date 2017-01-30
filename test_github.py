import pytest
from selenium import webdriver
from steps.registration_steps import RegistrationSteps
from models.user import User


def test_github_registration_successes():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://www.github.com/join")
    reg_steps = RegistrationSteps(driver)
    user = User.generate_random_user()
    reg_steps.fill_user_information_on_first_step(user)
    reg_steps.choose_account_type_on_second_step()
    reg_steps.check_necessary_checkbox_on_third_step()
    assert reg_steps.confirm_user_was_created()
