from pages.registration import InternalPage


class BaseSteps(object):
    def __init__(self, driver):
        self.internal_page = InternalPage(driver)

    def logout(self):
        self.internal_page.drop_down_menu.click()
        self.internal_page.sign_out_button.click()
