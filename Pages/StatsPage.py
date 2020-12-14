from Pages.BasePage import BasePage


from selenium.webdriver.common.by import By


class StatsPage(BasePage):
    
    def __init__(self,driver):

        super().__init__(driver)

    #locators for the page

    xpath_player_text=(By.XPATH,"//a[contains(@href,'dilshan')]")

    xpath_player_parent_td=(By.XPATH,"//a[contains(@href,'dilshan')]/parent::td[1]")

    xpath_player_matches=(By.XPATH,"//a[contains(@href,'dilshan')]/parent::td[1]/following-sibling::td[1]")

    xpath_player_innings=(By.XPATH,"//a[contains(@href,'dilshan')]/parent::td[1]/following-sibling::td[2]")

    xpath_player_runs=(By.XPATH,"//a[contains(@href,'dilshan')]/parent::td[1]/following-sibling::td[3]")

    xpath_player_avg=(By.XPATH,"//a[contains(@href,'dilshan')]/parent::td[1]/following-sibling::td[4]")

    #create action methods 

    def get_player_information(self):

        player_name=self.get_text(self.xpath_player_text)
        
        player_matches=self.get_text(self.xpath_player_matches)

        player_innings=self.get_text(self.xpath_player_innings)

        player_runs=self.get_text(self.xpath_player_runs)

        player_avg=self.get_text(self.xpath_player_avg)


        print("Player Information")
        print("Player Name: {0}".format(player_name))
        print("Total Matches: {0}".format(player_matches))
        print("Innings: {0}".format(player_innings))
        print("Runs: {0}".format(player_runs))
        print("Average: {0}".format(player_avg))



