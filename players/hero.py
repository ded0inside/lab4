from players import player


class Heroes(player.Player):
    def __init__(self):
        super().__init__()


class Batman(Heroes):
    def __init__(self):
        super().__init__()
        self.name = "Batman"
        self.health = 100
        self.base_damage = 10


class Superman(Heroes):
    def __init__(self):
        super().__init__()
        self.name = "Superman"
        self.health = 150
        self.base_damage = 15


class Wonderwoman(Heroes):
    def __init__(self):
        super().__init__()
        self.name = "Wonder-woman"
        self.health = 150
        self.base_damage = 15
