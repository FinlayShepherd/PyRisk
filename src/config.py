class Config:

    def __init__(self):
        self.territory_names = ["england", "france", "spain", "germany"]
        self.territory_neighbours = {"england": ["france"],
                                     "france": ["england", "spain", "germany"],
                                     "spain": ["france"],
                                     "germany": ["france"]}
        self.continent_names = ["uk", "europe"]
        self.continent_territories = {"uk": ["england"], "europe": ["france", "spain", "germany"]}
        self.continent_bonus = {"uk": 8, "europe": 1}
        self.players = {"green": "Finlay", "purple": "Nick", "yellow": "Maz"}
