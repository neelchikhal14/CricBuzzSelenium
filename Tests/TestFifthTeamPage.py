import pytest

from Pages.HomePage import HomePage
from Pages.HomePage import FifthTeamPage
from Tests.BaseTest import BaseTest




@pytest.mark.usefixtures("init_driver")
class Test_fifthteampage():

    @pytest.mark.skip
    def test_fifthpage_title(self):

        actual_title="Sri Lanka National Cricket Team"

        self.homepage=HomePage(self.driver)

        self.fifthteampage=self.homepage.hover_over_team_click_fifth()

        expected_title=self.fifthteampage.get_title()

        assert actual_title == expected_title


    def test_click_players_tab(self):

        self.homepage=HomePage(self.driver)

        self.fifthteampage=self.homepage.hover_over_team_click_fifth()

        self.playersPage=self.fifthteampage.players_click()

