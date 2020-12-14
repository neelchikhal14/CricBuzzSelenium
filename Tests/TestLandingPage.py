from Tests.BaseTest import BaseTest
from Pages.HomePage import HomePage

import pytest

@pytest.mark.usefixtures("init_driver")
class Test_Landing():

    @pytest.mark.skip
    def test_landing_page_title(self):

        self.homepage=HomePage(self.driver)

        actual_title=self.homepage.get_landingpage_title()
        print(actual_title)
        assert actual_title == "Google"

    def test_hover_to_teams(self):

        self.homepage=HomePage(self.driver)

        self.fifthteampage=self.homepage.hover_over_team_click_fifth()