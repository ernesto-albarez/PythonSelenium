# All the locators for each POM can be stored in a single file and also separated in classes
# This way I can update only a locator without modifying the POM methods


class HomePageLocator:
    loginLink = "//*[@class='option-login']"
    usernameHeader = "//*[@class='nav-header-username']"
    logoutButton = "//*[@data-id='logout']"


class LoginPageLocator:
    usernameField = "user_id"
    passwordField = "password"
    submitUsernameButton = "//*[@type='submit']"
    submitPasswordButton = "action-complete"
    invalidCredentials = "//div[@class='ui-form__message']"


class SearchProductPageLocator:
    searchBox = "//*[@class='nav-search-input']"
    lookupButton = "//*[@class='nav-icon-search']"
    foundProduct = "//*[@id='searchResults']/li[1]//*[@class='main-title']"
