# Author: Miguel Sandoval
# card.py

class Card:
    def __init__(self):
        self.title = "Lootcard"
        self.desc = "Description"

    def get_title(self):
        return self.title
    
class Treasure(Card):
    def __init__(self):
        self.effect = 1

class Lootcard(Card):
    def __init__(self):
        self.effect = 1

class Living(Card):
    def __init__(self, a, h, dr):
        self.attack = a
        self.health = h
        self.diceRoll = dr

class Monster(Living):
    def __init__(self):
        self.effect = 1

class Character(Living):
    def __init__(self):
        self.effect = 1