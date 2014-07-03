from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class FAW(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://hukkster.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_f_a_w(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("FAQ").click()

    def test_header_present(self):
        driver = self.driver
        driver.get(self.base_url + "faq")
        driver.find_element_by_xpath("/html/body/div[2]/div[12]/div/div/div/h3").click()

    def test_bottom_link_present(self):
        driver = self.driver
        driver.get(self.base_url + "faq")
        driver.find_element_by_link_text("Featured Stores Page").click()
        self.assertEqual(driver.current_url, "https://hukkster.com/featured-stores")

    def test_top_link_present(self):
        driver = self.driver
        driver.get(self.base_url + "faq")
        driver.find_element_by_xpath("/html/body/div[2]/div[11]/div/div[1]/a").click()  
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
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
