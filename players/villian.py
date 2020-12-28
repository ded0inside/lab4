from players import player


class Villians(player.Player):
    def __init__(self):
        super().__init__()


class Joker(Villians):
    def __init__(self):
        super().__init__()
        self.name = "Joker"
        self.health = 100
        self.base_damage = 10


class Bane(Villians):
    def __init__(self):
        super().__init__()
        self.name = "Bane"
        self.health = 130
        self.base_damage = 14


class Darkside(Villians):
    def __init__(self):
        super().__init__()
        self.name = "Darkside"
        self.health = 150
        self.base_damage = 20