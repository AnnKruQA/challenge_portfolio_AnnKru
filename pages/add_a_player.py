from pages.base_page import BasePage


class AddAPlayer(BasePage):
    name_xpath = // *[ @ id = "__next"] / div[1] / main / div[2] / form / div[2] / div / div[
        2] / div / div / input // div
    surname_xpath = // *[ @ id = "__next"] / div[1] / main / div[2] / form / div[2] / div / div[
        3] / div / div / input // div
    age_xpath = // *[ @ id = "date-time-edit"] / div / span[1]
    main_position_xpath = // *[ @ id = "__next"] / div[1] / main / div[2] / form / div[2] / div / div[
        11] / div / div / input // div
    submit_button_xpath = "//*[text()='Submit']         " \
    clear_button_xpath = //*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[2]
    expected_title = 'Add Player'
    add_a_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'


def title_of_page(self):
    time.sleep(4)
    assert self.get_page_title(self.add_a_player_url) == self.expected_title


def type_in_name(self, name):
    self.field_send_keys(self.name_xpath, name)


def type_in_surname(self, surname):
    self.field_send_keys(self.surname_xpath, surname)


def type_in_age(self, age):
    self.field_send_keys(self.age_xpath, age)


def type_in_mane_position(self, main_position):
    self.field_send_keys(self.main_position_xpath, main_position)


def click_submit_button(self):
    self.click_on_the_element(self.submit_button_xpath)


def click_clear_button(self):
    self.click_on_the_element(self.clear_button_xpath)


self.click_on_the_button("//*[text()='Add player']")
assert self.get_page_title(self.add_player_url) == expected_title
time.sleep(2)


@classmethod
def tearDown(self):
