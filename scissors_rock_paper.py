

# Challenges proposed at https://www.codementor.io/@ilyaas97/6-python-projects-for-beginners-yn3va03fs

import random
import numpy as np
import string

#  Rock, scissors, paper

# A first function, representing the virtual player, will pick randomly an item between scissors, rock and paper
# A second function compares the user input with the virtual player choice and prints out a statement.

def virtual_player():

    return random.choice(["scissors", "rock", "paper"])

def win_or_lose(guessed, virtual):

    if (guessed == "scissors" and virtual == "paper") or (guessed == "rock" and virtual == "scissors") or \
            (guessed == "paper" and virtual == "rock"):
        statement = "Your rival has picked " + virtual + ". You win."
    elif (guessed == "paper" and virtual == "scissors") or (guessed == "scissors" and virtual == "rock") or \
            (guessed == "rock" and virtual == "paper"):
        statement = "Your rival has picked " + virtual + ". You lose."
    else:
        statement = "Nobody wins. You are even."

    return statement


if __name__ == '__main__':

    while True:
        try:
            choice = input("Pick between scissors, rock and paper: ").lower()
            break
        except ValueError:
            print("Error. Please, pick between scissors, rock and paper.")

    result = win_or_lose(choice, virtual_player())
    print(result)







