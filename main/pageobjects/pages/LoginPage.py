from main.pageobjects.locators.Locators import LoginPageLocator


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.usernameField = LoginPageLocator.usernameField
        self.passwordField = LoginPageLocator.passwordField
        self.submitUsernameButton = LoginPageLocator.submitUsernameButton
        self.submitPasswordButton = LoginPageLocator.submitPasswordButton
        self.invalidCredentials = LoginPageLocator.invalidCredentials

    def enter_username(self, username):
        self.driver.find_element_by_id(self.usernameField).clear()
        self.driver.find_element_by_id(self.usernameField).send_keys(username)
        self.driver.find_element_by_xpath(self.submitUsernameButton).click()

    def enter_password(self, password):
        self.driver.find_element_by_id(self.passwordField).clear()
        self.driver.find_element_by_id(self.passwordField).send_keys(password)
        self.driver.find_element_by_id(self.submitPasswordButton).click()

    def get_invalid_username_message(self):
        msg = self.driver.find_element_by_xpath(self.invalidCredentials).text
        return msg

    def get_invalid_password_message(self):
        msg = self.driver.find_element_by_xpath(self.invalidCredentials).text
        return msg
