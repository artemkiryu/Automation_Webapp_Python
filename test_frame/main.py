import unittest
from selenium import webdriver
import page

class PythonOrgSearch (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
        self.driver.get("http://www.python.org")


    def test_title(self):
        mainPage = page.MainPage()
        assert mainPage.istitle_matches()
        #self.assertEqual("The Home Depot", mainPage, "webpage title is not same")


    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.istitle_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultsPagePage(self.driver)
        assert search_result_page.is_results_found()


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
