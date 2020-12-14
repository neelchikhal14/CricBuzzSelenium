from Pages.BasePage import BasePage
from Pages.StatsPage import StatsPage

from selenium.webdriver.common.by import By

class FifthTeamPage(BasePage):

    def __init__(self,driver):

        super().__init__(driver)

    #identify locators for the page

    xpath_fifth_team_page_title=(By.CSS_SELECTOR,"h1.cb-nav-hdr.cb-font-24.line-ht30")

    xpath_team_players_stats=(By.CSS_SELECTOR,"a[title*='Sri Lanka Cricket Team Stats']")

    # create action method for every method

    def get_title(self):

        fifth_team_title=self.get_text(self.xpath_fifth_team_page_title)

        return fifth_team_title
    
    def stats_click(self):

        self.do_click(self.xpath_team_players_stats)

        return StatsPage(self.driver)
