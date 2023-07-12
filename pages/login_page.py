import time

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//input[@name='password']"
    sign_in_button_xpath = " //*[text()='Sign in']"
    login_url = 'https://scouts-test.futbolkolektyw.pl/en/login'
    expected_title = 'Scouts panel - sign in'
    header_xpath = "//*[@id="__next"]/div[1]/header/div/h6"
    expected_header = 'Scouts Panel'
    add_a_player_button_xpath = "//*[text()='Add player']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def clic_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        time.sleep(1)
        assert self.get_page_title(self.login_url) == self.expected_title

    def check_page_title(self):
        self.assert_element_text(self.driver, self.header_xpath, self.expected_header)
