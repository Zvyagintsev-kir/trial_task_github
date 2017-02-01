from pages.registration import RegistrationStepOnePage
from pages.registration import RegistrationStepTwoPage
from pages.registration import RegistrationStepThreePage
from pages.registration import RegistrationConfirmPage


class RegistrationSteps(object):
    def __init__(self, driver):
        self.registration_page_step_one = RegistrationStepOnePage(driver)
        self.registration_page_step_two = RegistrationStepTwoPage(driver)
        self.registration_page_step_three = RegistrationStepThreePage(driver)
        self.registration_page_confirm = RegistrationConfirmPage(driver)

    def fill_user_information_on_first_step(self, user):
        self.registration_page_step_one.name_field.send_keys(user.user_name)
        self.registration_page_step_one.email_field.send_keys(user.user_email)
        self.registration_page_step_one.password_field.send_keys(user.user_password)
        self.registration_page_step_one.sign_button.click()

    def choose_account_type_on_second_step(self):
        self.registration_page_step_two.submit_button.click()

    def check_necessary_checkbox_on_third_step(self):
        self.registration_page_step_three.development_checkbox.click()
        self.registration_page_step_three.research_checkbox.click()
        self.registration_page_step_three.submit_button.click()

    def confirm_user_was_created(self):
        if self.registration_page_confirm.confirmation_message.get_text() == "Learn Git and GitHub without any code!":
            return True
        else:
            return False

    def check_validation_error(self, error):
        if self.registration_page_step_one.validation_error.get_text() == error:
            return True
        else:
            return False
