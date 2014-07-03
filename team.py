from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Team(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://hukkster.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_team(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text("Team").click()
    
    def test_headers_present(self):
        driver = self.driver
        driver.get(self.base_url + "team")
        driver.find_element_by_xpath("/html/body/div[2]/div[12]/div/header/h3")
        driver.find_element_by_xpath("/html/body/div[2]/div[12]/div/div[2]/h1")

    def test_pictures_present(self):
        driver = self.driver
        driver.get(self.base_url + "team")
        driver.find_element_by_xpath("/html/body/div[2]/div[12]/div/div[2]/div/div[1]/section/article[1]/div/img")
        driver.find_element_by_xpath("/html/body/div[2]/div[12]/div/div[2]/div/div[1]/section/article[2]/div/img")

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
