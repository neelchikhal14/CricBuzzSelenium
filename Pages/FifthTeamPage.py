from Pages.BasePage import BasePage
from Pages.PlayersPage import PlayersPage

from selenium.webdriver.common.by import By

class FifthTeamPage(BasePage):

    def __init__(self,driver):

        super().__init__(driver)

    #identify locators for the page

    xpath_fifth_team_page_title=(By.CSS_SELECTOR,"h1.cb-nav-hdr.cb-font-24.line-ht30")

    xpath_team_players=(By.CSS_SELECTOR,"a[title*='Sri Lanka Cricket Team Players']")

    # create action method for every method

    def get_title(self):

        fifth_team_title=self.get_text(self.xpath_fifth_team_page_title)

        return fifth_team_title
    
    def players_click(self):

        self.do_click(self.xpath_team_players)

        return PlayersPage(self.driver)
