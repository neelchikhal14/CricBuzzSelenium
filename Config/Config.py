from pathlib import Path
import os

class ConfigData():

    BASE_URL="https://www.cricbuzz.com/"
    
    #TEMPLATE_DIR=os.path.join(BASE_DIR,'blog\templates')
    #GECKODRIVER_PATH="D:\Python Selenium\CricbuzzSelenium\geckodriver.exe"
    BASE_DIR=Path(__file__).parent.parent
    GECKODRIVER_PATH=os.path.join(BASE_DIR,'Drivers','geckodriver.exe')

# mydata=ConfigData()
# print(mydata.BASE_DIR)
# print(mydata.GECKODRIVER_PATH)