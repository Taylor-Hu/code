import time
from framework.woniucbt.common.utility import UtilityTest

class SellObject:

    def __init__(self):
        self.driver = UtilityTest.get_webdriver()

    def get_barcode(self):
        self.driver.find_element_by_id('barcode').clear()
        return self.driver.find_element_by_id('barcode')

    def get_barcode_button(self):
        return self.driver.find_element_by_xpath("(//button[@type='button'])[5]")

    def get_discount_ratio(self):
        element = self.driver.find_element_by_css_selector('.discountratio > input')
        element.clear()
        return element

    def get_buy_count_plus(self):
        return self.driver.find_element_by_xpath("//button[@onclick='buyCountPlus(this)']")

    def get_customer_phone(self):
        return self.driver.find_element_by_id('customerphone')

    def get_customer_query_button(self):
        return self.driver.find_element_by_xpath("//button[contains(.,' 查询会员信息')]")

    def get_credit_ratio(self):
        self.driver.find_element_by_id('creditratio').clear()
        return self.driver.find_element_by_id('creditratio')

    def get_submit_button(self):
        return self.driver.find_element_by_id('submit')

    def do_buy_goods(self, barcode, discount_ratio):
        self.get_barcode().send_keys(barcode)
        self.get_barcode_button().click()
        self.get_discount_ratio().send_keys(discount_ratio)
        self.get_buy_count_plus().click()
        time.sleep(1)

    def do_sell(self, phone, credit_ratio):
        self.get_customer_phone().send_keys(phone)
        self.get_customer_query_button().click()
        self.get_credit_ratio().send_keys(credit_ratio)
        self.get_submit_button().click()
        time.sleep(2)
        self.driver.switch_to.alert.accept()
        time.sleep(2)