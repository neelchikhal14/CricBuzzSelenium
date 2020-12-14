from Pages.BasePage import BasePage
from Pages.FifthTeamPage import FifthTeamPage

from selenium.webdriver.common.by import By



class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
        

    #identify locators for the page

    xpath_teams=(By.XPATH,"//div[@id='teamDropDown']")

    xpath_teams_list=(By.XPATH,"//div[@class='cb-sub-lg-outer']/div[1]/a")

    xpath_fifth_team=(By.XPATH,"(//div[@class='cb-sub-lg-outer']/div[1]/a)[5]")

    # create action method for every method

    def get_landingpage_title(self):

        return self.driver.title

    def hover_over_team_click_fifth(self):
        self.hover_over_element(self.xpath_teams)
        total_teams=self.count_number_of_teams(self.xpath_teams_list)
        print(total_teams)
        count=len(total_teams)
        print("The total Teams are {0}".format(count))
      #  self.hover_over_element(self.xpath_fifth_team)
        self.do_click(self.xpath_fifth_team)

        # do login returns the object of next page -> Page Chaining
        return FifthTeamPage(self.driver)