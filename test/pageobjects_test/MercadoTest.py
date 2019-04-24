import unittest
import HtmlTestRunner
from selenium import webdriver
# Imports to run from command line
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from main.pageobjects.pages.HomePage import HomePage
from main.pageobjects.pages.LoginPage import LoginPage
from main.pageobjects.pages.SearchProductPage import SearchProductPage


class MercadoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Running only once, before all the test methods")
        # setUpClass runs only once, before all the test methods
        # If the driver is configured here, the same browser session will apply for all the test cases
        # cls.driver = webdriver.Chrome()
        # cls.driver.implicitly_wait(10)
        # cls.driver.maximize_window()

    def setUp(self):
        # setUp runs before every test method
        # When the driver is configured here, all the tests will have a different browser session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        print("Running before the test method")
        self.home = HomePage(self.driver)
        self.home.navigate_to_home_page()
        self.login = LoginPage(self.driver)

    def test_01_search_for_a_product(self):
        search = SearchProductPage(self.driver)
        search.search_product("huevo de pascuas")
        search.open_product_profile()

    def test_02_login_to_ml(self):
        self.home.go_to_login_page()

        self.login.enter_username("oanderson189@hidebusiness.xyz")
        self.login.enter_password("QAtest1234")

        self.home.logout_page()

    def test_03_login_invalid_username(self):
        self.home.go_to_login_page()

        self.login.enter_username("InvalidUsername")
        invalid_username_message = self.login.get_invalid_username_message()
        self.assertEqual(invalid_username_message, "Revisá tu e‑mail o usuario.")

    def test_04_login_invalid_password(self):
        self.home.go_to_login_page()

        self.login.enter_username("oanderson189@hidebusiness.xyz")
        self.login.enter_password("QAtest")

        invalid_password_message = self.login.get_invalid_password_message()
        self.assertEqual(invalid_password_message, "Revisá tu clave.")

    def tearDown(self):
        # tearDown runs after every method
        print("Running after the test method")
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        # tearDownClass runs after all the methods
        print("Running only once, after all the test methods")
        # cls.driver.close()


# This condition is to run the test cases from the command line
# cmd: <dir> python <python_test_cases_file.py>
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reports"))
