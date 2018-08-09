class Territory:

    def __init__(self, name, neighbours):
        self.name = name
        self.neighbours = neighbours
        self.occupier = None
        self.army_count = 0

    def add_armies(self, amount):
        self.army_count = self.army_count + amount

    def remove_armies(self, amount):
        self.army_count = self.army_count - amount

    def set_occupier(self, occupier):
        self.occupier = occupier

    def get_army_count(self):
        return self.army_count

    def get_name(self):
        return self.name




