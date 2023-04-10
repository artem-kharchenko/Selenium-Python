# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://localhost:8080/litecart/admin/")
        driver.find_element_by_xpath("//li[@id='app-']/a/span[2]").click()
        driver.find_element_by_xpath("//li[@id='doc-template']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-logotype']/a/span").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Logotype'])[1]/following::span[2]").click()
        driver.find_element_by_xpath("//li[@id='doc-product_groups']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-option_groups']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-manufacturers']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-suppliers']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-delivery_statuses']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-sold_out_statuses']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-quantity_units']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-csv']/a/span").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='CSV Import/Export'])[1]/following::span[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Countries'])[1]/following::span[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Currencies'])[1]/following::span[2]").click()
        driver.find_element_by_xpath("//li[@id='doc-csv']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-newsletter']/a/span").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Newsletter'])[1]/following::span[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Geo Zones'])[1]/following::span[2]").click()
        driver.find_element_by_xpath("//li[@id='doc-storage_encoding']/a/span").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Storage Encoding'])[1]/following::span[2]").click()
        driver.find_element_by_xpath("//li[@id='doc-customer']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-shipping']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-payment']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-order_total']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-order_success']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-order_action']/a/span").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Order Action'])[1]/following::span[2]").click()
        driver.find_element_by_xpath("//li[@id='doc-order_statuses']/a/span").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Order Statuses'])[1]/following::span[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Pages'])[1]/following::span[2]").click()
        driver.find_element_by_xpath("//li[@id='doc-most_sold_products']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-most_shopping_customers']/a/span").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Most Shopping Customers'])[1]/following::span[2]").click()
        driver.find_element_by_xpath("//li[@id='doc-defaults']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-general']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-listings']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-images']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-checkout']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-advanced']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-security']/a/span").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Security'])[1]/following::span[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Slides'])[1]/following::span[2]").click()
        driver.find_element_by_xpath("//li[@id='doc-tax_rates']/a/span").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Tax Rates'])[1]/following::span[2]").click()
        driver.find_element_by_xpath("//li[@id='doc-scan']/a/span").click()
        driver.find_element_by_xpath("//li[@id='doc-csv']/a/span").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='CSV Import/Export'])[1]/following::span[2]").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Users'])[1]/following::span[2]").click()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
