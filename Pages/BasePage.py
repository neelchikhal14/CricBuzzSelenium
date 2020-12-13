from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC

"""This class is parent of all pages . It contains all generic methods and utilities"""

class BasePage():

    def __init__(self,driver):

        self.driver=driver


    # define all generic methods here

    def do_click(self, by_locator):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(by_locator)).click() 

    def hover_over_element(self,by_locator):
        
        hover_element=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))

        AC(self.driver).move_to_element(hover_element).perform()

    
    def count_number_of_teams(self,by_locator):
        
        total_teams=WebDriverWait(self.driver,10).until(EC.visibility_of_any_elements_located(by_locator)) 

        total_team_name=[]

        for i in range(0,len(total_teams)):
            total_team_name.append(total_teams[i].text)
  

        return total_team_name