import pytest

from Tests.BaseTest import BaseTest
from Pages.HomePage import HomePage
from Pages.StatsPage import StatsPage


@pytest.mark.usefixtures("init_driver")
class TestStatsPage():

    def test_player_information(self):

        self.homepage=HomePage(self.driver)

        self.fifthteampage=self.homepage.hover_over_team_click_fifth()

        self.statsPage=self.fifthteampage.stats_click()

        self.statsPage.get_player_information()