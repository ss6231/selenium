from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Careers(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://hukkster.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_careers(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Careers").click()
    
    def test_email_link_present(self):
        driver = self.driver
        driver.get(self.base_url + "careers")
        driver.find_element_by_xpath("/html/body/div[2]/div[12]/div/div[2]/div/div[2]/div/div/a").click()

    def test_careers_header_present(self):
        driver = self.driver
        driver.get(self.base_url + "careers")
        driver.find_element_by_xpath("/html/body/div[2]/div[12]/div/header/h3")

    def test_hukkster_is_hiring_present(self):
        driver = self.driver
        driver.get(self.base_url + "careers")
        driver.find_element_by_xpath("/html/body/div[2]/div[12]/div/div[2]/h1")

    def test_want_to_work_for_us_present(self):
        driver = self.driver
        driver.get(self.base_url + "careers")
        driver.find_element_by_xpath("/html/body/div[2]/div[12]/div/div[2]/div/div[2]/div/div/p")

    def test_images_present(self):
        driver = self.driver
        driver.get(self.base_url + "careers")
        driver.find_element_by_xpath("/html/body/div[2]/div[12]/div/div[2]/div/div[1]/div/div[1]/img")
        driver.find_element_by_xpath("/html/body/div[2]/div[12]/div/div[2]/div/div[1]/div/div[2]/img")
    
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
