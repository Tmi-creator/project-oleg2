class Enemy(object):
    def __init__(self, hp, atk, provocation, windpower):
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.cur_atk = atk
        self.provocation = provocation
        self.windpower = windpower


class SkeletW(object):
    def __init__(self):
        super().__init__(hp=75, atk=10, provocation=5, windpower=1)

