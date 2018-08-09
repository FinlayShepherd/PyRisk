from .config import Config
from .territory import Territory
from .continent import Continent
from .player import Player


class Board:

    def __init__(self, player_number):
        self.config = Config.__init__()
        self.player_number = player_number
        self.territories = self.init_territories()
        self.continents = self.init_continents()

    def init_territories(self):
        territory_list = []
        for name in self.config.territory_names:
            territory_neighbours = self.config.territory_neighbours[name]
            territory = Territory.__init__(name, territory_neighbours)
            territory_list.append(territory)
        return territory_list

    def init_continents(self):
        continent_list = []
        for name in self.config.continent_names:
            continent_territories = self.config.continent_territories[name]
            continent_bonus = self.config.continent_bonus[name]
            continent = Continent.__init__(name, continent_territories, continent_bonus)
            continent_list.append(continent)
        return continent_list

    def init_players(self):
        players = []
        for player_colour in list(self.config.players.keys()):
            player_name = self.config.players[player_colour]
            player = Player.__init__(player_name, player_colour)
            players.append(player)
        return players
