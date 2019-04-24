from main.pageobjects.locators.Locators import HomePageLocator


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.loginLink = HomePageLocator.loginLink
        self.usernameHeader = HomePageLocator.usernameHeader
        self.logoutButton = HomePageLocator.logoutButton

    def navigate_to_home_page(self):
        self.driver.get("https://www.mercadolibre.com.ar")

    def go_to_login_page(self):
        self.driver.find_element_by_xpath(self.loginLink).click()

    def logout_page(self):
        self.driver.find_element_by_xpath(self.usernameHeader).click()
        self.driver.find_element_by_xpath(self.logoutButton).click()
