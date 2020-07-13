import time
from framework.woniucbt.common.utility import UtilityTest

class LoginObject:

    def __init__(self):
        self.driver = UtilityTest.get_webdriver()

    def get_username(self):
        self.driver.find_element_by_id('username').clear()
        return self.driver.find_element_by_id('username')

    def get_password(self):
        self.driver.find_element_by_id('password').clear()
        return self.driver.find_element_by_id('password')

    def get_verify_code(self):
        self.driver.find_element_by_id('verifycode').clear()
        return self.driver.find_element_by_id('verifycode')

    def get_login_button(self):
        return self.driver.find_element_by_xpath("(//button[@type='button'])[5]")

    def do_login(self, username, password):
        self.get_username().send_keys(username)
        self.get_password().send_keys(password)
        self.get_verify_code().send_keys('0000')
        self.get_login_button().click()
        time.sleep(2)