from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Howitworks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://hukkster.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_howitworks(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("How it Works").click()
        

    def test_sidebar_links (self):
        driver = self.driver
        driver.get(self.base_url + "how-it-works")
        list_of_links = driver.find_elements_by_xpath ("//*[@id='howtohukk_nav_container']/ul/li/a")
        for link in list_of_links:
            link.click()
            time.sleep (5)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
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
