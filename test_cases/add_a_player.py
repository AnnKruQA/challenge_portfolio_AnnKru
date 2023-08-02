import os
import unittest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.add_a_player import AddAPlayer
from page.base_page import BasePage
from page.dashboard import Dashboard
from page.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddAPlayer(unittest.TestCase):
    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_player(self):
        user_login = LoginPage(self.driver)
        user.login.title_of_page()
        user_login.type_in_email('user09@getnada.com')
        user_login.type_in_password('Test-1234')
        user.login.click_sign_in_button("//*[text()='Sign in']")
        dasbord_page = Dasboard(self.driver)
        dasbord_page.title_of_page()
        time.sleep(3)
        dasboard_page.click_add_player_button()
        time.sleep(3)
        add_a_player = AddAPlayer(self.driver)
        add_a_player.title_of_page
        time.sleep(3)
        add_a_player.type_in_name('Franciszek')
        add_a_player.type_in_surname('Kruk')
        add_a_player.type_in_age('11-11-1999')
        add_a_player.type_in_main_position('strike')
        add_a_player.click_submit_button()
        time.sleep(3)

    self.click_on_the_button("//*[text()='Add player']")
    assert self.get_page_title(self.add_player_url) == expected_title
    time.sleep(2)

    @classmethod
    def tearDown(self):
        self.driver.quit()
