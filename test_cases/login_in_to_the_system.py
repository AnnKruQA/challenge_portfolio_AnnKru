import os
import unittest
from datetime import time
from lib2to3.pgen2 import driver

from selenium import webdriver

from pages import dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service

from page.base_page import BasePage
from page.dashboard import Dashboard
from page.login_page import LoginPage


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_in_to_the_system(self):
        BasePage.setUp(self)
        user_login = LoginPage(self.driver)
        user.login.title_of_page()
        user.login.check_page_title()
        user_login.type_in_email('user09@getnada.com')
        user_login.type_in_password('Test-1234')
        user.login.click_on_the_button("//*[text()='Sign in']")
        time.sleep(5)
        dashborad_page = Dashboard(self, driver)
        dashboard.title_of_page()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
