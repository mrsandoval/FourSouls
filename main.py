# Author: Miguel Sandoval
# main.py

import sqlite3
import os
from player import Player
from card import *

# Clears terminal screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Prompt for beginning of turn
def prompt(p):
    return "Player " + str(p) + " it is your turn\n\nYour abilities have been refreshed\nYou drew a card\n\n"

def turn(p):
    clear()
    user_input = input(prompt(p.pnum) + "Make a move:\nPlay a card(1)\nAttack(2)\nBuy a treasure(3)\n")
    if user_input == '1':
        print("Select which card to play:")
        # p.display_hand()
        # selected_card = int(input())
        # p.playcard()
    elif user_input == '2':
        print("Fighting")
        # p.fight()
    elif user_input == '3':
        print("Buying")
        # p.buy()
    else:
        print("That is not a move")

def check_for_winner(players):
    for player in players:
        if player.souls == 4:
            print(str(player.getpnum()) + " Wins!")

def game_setup(players):
    for player in players:
        player.setup()

def cleanup():
    # Connect to SQLite database
    conn = sqlite3.connect('cards.db')

    # Create a cursor
    cursor = conn.cursor()

    try:
        # Reset the 'used' column to zero for all rows
        cursor.execute('UPDATE character SET used = 0')

        # Commit the changes
        conn.commit()
    except Exception as e:
        # Handle any exceptions if needed
        print(f"Error: {e}")
    finally:
        # Close the connection
        conn.close()

if __name__ == "__main__":
    cleanup()

    print("Let the game begin!")

    # Variables
    winner = False

    # Generic
    num_players = int(input("Number of Players: "))
    players = [Player(i) for i in range(1, num_players + 1)]

    # Sets up game
    game_setup(players)

    while not winner:
        # Turn
        for player in players:
            turn(player)

        winner = True
    

    print("Game Over!")
