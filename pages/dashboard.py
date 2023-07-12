import time
from pages.base_page import BasePage


class Dashboard(BasePage):
    1.
    main_page_xpath = "//*[text()='Main page']"
    2.
    players_xpath = "//*[text()='Players']"
    3.
    polski_xpath = "//*[text()='Polski']"
    4.
    sign_out_button_xpath = "//*[text()='Sign out']"
    5.
    players_count_xpath = "//*[text()='Players count']"
    6.
    matches_count_xpath = "//*[text()='Matches count']"
    7.
    reports_count_xpath = "//*[text()='Reports count']"
    8.
    events_count_xpath = "//*[text()='Events count']"
    9.
    dev_team_contanct_button_xpath = "//*[text()='Dev team contact']"
    10.
    add_player_button_xpath = "//*[text()='Add player']"

    expected_title = 'Scouts Panel'
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en/'

    pass

    def title_of_page(self):
        test_title = self.get_page_title(self.dashborad_url)
        time.sleep(4)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_add_player_button(self):
        self.click_on_the_element(self.add_a_player_button_xpath)
