import unittest
import HtmlTestRunner

import sys

sys.path.append("D:\Python Selenium\CricbuzzSelenium")

from selenium import webdriver

from Pages.HomePage import HomePage


from Pages.BasePage import BasePage



class HomePageTest(unittest.TestCase):


    driver=webdriver.Firefox(executable_path=BasePage.GECKODRIVER_PATH)

    @classmethod
    def setUp(cls):
        cls.driver.get(BasePage.BASE_URL)
        cls.driver.maximize_window()
    
    def test_homepage_title(self):
        hp=HomePage(self.driver)

        homePageTitle=hp.get_title
        actualHomePageTitle="Live Cricket Score, Schedule, Latest News, Stats & Videos | Cricbuzz.com"

        self.assertEqual(homePageTitle,actualHomePageTitle)

    @classmethod
    def tearDown(cls):

        cls.driver.quit();

if __name__ == '__main__':

    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:\Python Selenium\CricbuzzSelenium\Report'))
