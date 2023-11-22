# player.py
import sqlite3
import random

class Player:
    def __init__(self, pnum):
        self.diceRollMod = 0
        self.attack = 1
        self.health = 2
        self.pnum = pnum
        self.souls = 0
        self.hand = []
        self.character = ""

    def fight(self, m):
        print("fight", m)
        return True

    def deal_damage(self, p):
        p.take_damage(self.attack)

    def take_damage(self, damage):
        self.health -= damage

    def heal(self, amount):
        self.health += amount

    def is_living(self):
        return self.health > 0

    def setup(self):

        # Connect to SQLite database
        conn = sqlite3.connect('cards.db')

        # Create a cursor
        cursor = conn.cursor()

        # Execute a query to get the number of unused cards
        cursor.execute('SELECT COUNT(*) FROM character WHERE NOT used')
        total_unused_cards = cursor.fetchone()[0]

        if total_unused_cards > 0:
            # Generate a random row number for an unused card
            random_row_number = random.randint(1, total_unused_cards)

            # Execute a query to get the random card
            cursor.execute(f'SELECT * FROM character WHERE NOT used LIMIT 1 OFFSET {random_row_number - 1}')
            random_card = cursor.fetchone()

            # Mark the chosen card as used
            cursor.execute(f'UPDATE character SET used = 1 WHERE id = ?', (random_card[-2],))
            conn.commit()

            self.character = random_card[0]
            print("Player " + str(self.pnum) + ": " + self.character +"\n")
        else:
            print("No unused cards left.")

        # Close the connection
        conn.close()

    def set_pnum(self, p):
        self.pnum = p

    def get_pnum(self):
        return self.pnum

    # Cards
    def play_card(self, c):
        print("play card", c)
        return True

    #def display_hand(self):
        #for i in range(len(self.hand)):
            #print(self.hand[i].get_title(), "(", i, ")")
        #print()

    def buy(self, t):
        print("buy", t)
        return True
