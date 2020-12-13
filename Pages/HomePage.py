from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By

import time

class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        

    #identify locators for the page

    xpath_teams=(By.XPATH,"//div[@id='teamDropDown']")

    xpath_teams_list=(By.XPATH,"//div[@class='cb-sub-lg-outer']/div[1]/a")

    # create action method for every method

    def get_landingpage_title(self):

        return self.driver.title

    def hover_over_team(self):
        super().hover_over_element(self.xpath_teams)
        total_teams=self.count_number_of_teams(self.xpath_teams_list)
        print(total_teams)
        count=len(total_teams)
        print("The total Teams are {0}".format(count))    