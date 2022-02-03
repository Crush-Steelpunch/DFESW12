class Athlete:
    def __init__(self, name):
        self.name = name

class Footballer(Athlete):
    def __init__(self, ID_Number, team):
        self.team = team



player1 = Footballer("0x567", "Droylsden FC")
player2 = Footballer(name, team)