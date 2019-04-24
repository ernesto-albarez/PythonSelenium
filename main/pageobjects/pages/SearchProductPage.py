from main.pageobjects.locators.Locators import SearchProductPageLocator


class SearchProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.searchBox = SearchProductPageLocator.searchBox
        self.lookupButton = SearchProductPageLocator.lookupButton
        self.foundProduct = SearchProductPageLocator.foundProduct

    def search_product(self, product_name):
        self.driver.find_element_by_xpath(self.searchBox).clear()
        self.driver.find_element_by_xpath(self.searchBox).send_keys(product_name)
        self.driver.find_element_by_xpath(self.lookupButton).click()

    def open_product_profile(self):
        self.driver.find_element_by_xpath(self.foundProduct).click()
