from utils.web_ui import WebElement


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class RegistrationStepOnePage(BasePage):

    @property
    def name_field(self):
        return WebElement(self.driver, locator_type="id", locator="user_login")

    @property
    def email_field(self):
        return WebElement(self.driver, locator_type="id", locator="user_email")

    @property
    def password_field(self):
        return WebElement(self.driver, locator_type="id", locator="user_password")

    @property
    def sign_button(self):
        return WebElement(self.driver, locator_type="id", locator="signup_button")


class RegistrationStepTwoPage(BasePage):

    @property
    def public_repository_radio_button(self):
        return WebElement(self.driver, locator_type="xpath",
                          locator="//*[@class='plan-choice-radio js-plan-choice' and @value='free']")

    @property
    def submit_button(self):
        return WebElement(self.driver, locator_type="xpath",
                          locator="//button[@type='submit' and @class='btn btn-primary js-choose-plan-submit']")


class RegistrationStepThreePage(BasePage):

    @property
    def research_checkbox(self):
        return WebElement(self.driver, locator_type="id", locator="answers_99_choice_467")

    @property
    def development_checkbox(self):
        return WebElement(self.driver, locator_type="id", locator="answers_99_choice_464")

    @property
    def submit_button(self):
        return WebElement(self.driver, locator_type='xpath', locator="//input[@value='Submit']")


class RegistrationConfirmPage(BasePage):
    @property
    def confirmation_message(self):
        return WebElement(self.driver, locator_type='xpath', locator="//h2[@class='shelf-title']")