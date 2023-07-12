import time
from pages.base_page import BasePage


class Dashboard(BasePage):
   1. main_page_en_xpath = "//*[text()='Main page']"
   2. players_en_xpath = "//*[text()='Players']"
   3. polski_en_xpath = "//*[text()='Polski']"
   4. sign_out_button_en_xpath = "//*[text()='Sign out']"
   5. players_count_en_xpath = "//*[text()='Players count']"
   6. matches_count_en_xpath = "//*[text()='Matches count']"
   7. reports_count_en_xpath = "//*[text()='Reports count']"
   8. events_count_en_xpath = "//*[text()='Events count']"
   9. dev_team_contanct_button_en_xpath = "//*[text()='Dev team contact']"
   10. add_player_button_en_xpath = "//*[text()='Add player']"
   pass


class Dashboard(BasePage):
   expected_title = "Scouts panel"
   dashboard_url = "https://scouts-test.futbolkolektyw.pl/en/"
   def title_of_page(self):
      time.sleep(4)
      assert self.get_page_title(self.dashboard_url)=expected_title
