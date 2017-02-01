import pytest
from selenium import webdriver
from steps.registration_steps import RegistrationSteps
from models.user import User

user_data = [
    User.generate_user_with_empty_name(),
    User.generate_user_with_empty_email(),
    User.generate_user_with_empty_password()
]

validation_test_id = [
    "blank_name",
    "blank_email",
    "blank_password"
]


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


@pytest.mark.parametrize("gen_user", user_data, ids=validation_test_id)
def test_github_validation_error(gen_user):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("http://www.github.com/join")
    reg_steps = RegistrationSteps(driver)
    reg_steps.fill_user_information_on_first_step(gen_user)
    assert reg_steps.check_validation_error(gen_user.validation_error)

