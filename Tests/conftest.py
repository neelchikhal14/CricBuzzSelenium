from selenium import webdriver
import pytest

from Config.Config import ConfigData

@pytest.fixture(params=['firefox',],scope="class")
def init_driver(request):
    
    if request.param == 'firefox':

        web_driver=webdriver.Firefox(executable_path=ConfigData.GECKODRIVER_PATH)

    request.cls.driver=web_driver 

    web_driver.get(ConfigData.BASE_URL)
    web_driver.implicitly_wait(10)
    
    yield

    web_driver.close()
