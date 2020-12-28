from dodges import dodge


class Gadget(dodge.Dodges):
    damage = 0
    attack_speed = 16

    def __init__(self):
        super().__init__()
        self.type = "gadget"

    def __repr__(self):
        return "{0}, damage: {1}".format(self.name, self.damage)

    def get_text(self):
        return (
            f"Gadget: {0}, Damage: {1}, Attack Speed: {2}",
            self.name,
            self.damage,
            self.attack_speed,
        )


class Batarang(Gadget):
    def __init__(self):
        super().__init__()
        self.name = "Batarang"
        self.damage = 30


class JokerVenom(Gadget):
    def __init__(self):
        super().__init__()
        self.name = "Joker Venom"
        self.damage = 30


class BaneVenom(Gadget):
    def __init__(self):
        super().__init__()
        self.name = "Bane Venom"
        self.damage = 25


class TruthLasso(Gadget):
    def __init__(self):
        super().__init__()
        self.name = "Lasso of Truth"
        self.attack_speed = 10
        self.damage = 100