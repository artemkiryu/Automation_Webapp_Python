#pip install selenium - in terminal

import unittest
from selenium.webdriver.common.keys import Keys
from selenium_pro import webdriver
import time


class Test (unittest.TestCase):
    def testName(self):
        path = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
        driver = webdriver.Chrome(path)
        driver.get("https://www.homedepot.com/")
        print(driver.title)
        titleOfWebPage=driver.title
        #assertEqual - assertion for "Google"
        self.assertEqual("The Home Depot", titleOfWebPage, "webpage title is not same")
if __name__ == "__main__":
    unittest.main()
# Search field and assertion

#driver.find_element_by_id("searchField").type("Movies") -- searching by ID
#driver.find_element_by_name("q").send_keys("Tutorial")
#driver.find_element_by_name("btnK").click()
#driver.find_element_by_link_text("Learn More").click()
#driver.find_element_by_css_selector("#twotabsearchtextbox").send_keys("Fishing")
#driver.find_element_by_partial_link_text("Best").click()

driver.quit()