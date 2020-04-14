

# Challenges proposed at https://www.codementor.io/@ilyaas97/6-python-projects-for-beginners-yn3va03fs

import random
import numpy as np


#  Guess the Number



if __name__ == '__main__':

    num = np.random.randint(0,20) # random integer drawn from (0,20)

# function to decide whether you have won or not
# this function takes the guessed number as the argument and prints out three different messages
# the number of available attempts is 6

    count = 0
    while count < 6:
        guess = int(input("Guess an integer between 0 and 20: "))
        if num == guess:
            print("Congratulations, your guess is correct. You win!")
            break
        elif num < guess:
            print("Sorry, your guess is too high. Please, retry. You still have " + str(6-count) + " attempts left.")
            count += 1
        elif num > guess:
            print("Sorry, your guess is too low. Please, retry. You still have " + str(6-count) + " attempts left.")
            count += 1


    if num != guess:
        print("Sorry, you have lost. The number to guess was " + str(num))









