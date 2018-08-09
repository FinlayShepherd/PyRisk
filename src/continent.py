class Continent:

    def __init__(self, name, territories, bonus):
        self.name = name
        self.territories = territories
        self.bonus = bonus

    def check_for_bonus(self):
        return False
