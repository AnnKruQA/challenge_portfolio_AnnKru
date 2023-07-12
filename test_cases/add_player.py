import os
import unittest
from datetime import time

from selenium import webdriver
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT
from selenium.webdriver.chrome.service import Service


from page.base_page import BasePage
from page.dashboard import Dashboard
from page.login_page import LoginPage
from page.add_a_plyer import AddPlayer
class TestAddPlayer(unittest.TestCase):
    @classmethod
    def setUp(self):
        TestLoginPage(unittest.TestCase)
        user_login = LoginPage(self.driver)
        user.login.title_of_the_page()
        user_login.type_in_email('user09@getnada.com')
        user_login.type_in_password('Test-1234')
        user.login.click_on_the_button("//*[text()='Sign in']")
        time.sleep(5)

    def test_add_a_player(self):
        self.click_on_the_button("//*[text()='Add player']")
        asser self.get_page_title(self.add_player_url) == expected_title
        time.sleep(2)

    class AddPlayer(BasePage):
        expected_title = 'Add Player'
        dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'

        def title_of_page(self):
            time.sleep(4)
            assert self.get_page_title(self.dashboard_url)=expected_title
    @classmethod
    def tearDown(self):
