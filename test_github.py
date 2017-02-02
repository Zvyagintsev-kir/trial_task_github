import pytest
from selenium import webdriver
from steps.registration_steps import RegistrationSteps
from steps.base_steps import BaseSteps
from models.user import User

user_data = [
    User.generate_user_with_empty_name(),
    User.generate_user_with_empty_email(),
    User.generate_user_with_empty_password(),
    User.generate_user_with_wrong_name(),
    User.generate_user_with_wrong_email(),
    User.generate_user_with_wrong_password()
]

validation_test_id = [
    "blank_name",
    "blank_email",
    "blank_password",
    "wrong_name",
    "wrong_email",
    "wrong_password"
]


@pytest.fixture(scope="function")
def test_driver(request, selenium_driver):
    yield selenium_driver
    selenium_driver.get("http://www.github.com/join")


@pytest.fixture(scope="function")
def logout(request, selenium_driver):
    yield
    base_steps = BaseSteps(selenium_driver)
    base_steps.logout()


def test_github_registration_successes(test_driver, logout):
    reg_steps = RegistrationSteps(test_driver)
    user = User.generate_random_user()
    reg_steps.fill_user_information_on_first_step(user)
    reg_steps.choose_account_type_on_second_step()
    reg_steps.check_necessary_checkbox_on_third_step()
    assert reg_steps.confirm_user_was_created()


@pytest.mark.parametrize("gen_user", user_data, ids=validation_test_id)
def test_github_validation_error(gen_user, test_driver):
    reg_steps = RegistrationSteps(test_driver)
    reg_steps.fill_user_information_on_first_step(gen_user)
    assert reg_steps.check_validation_error(gen_user.validation_error)

