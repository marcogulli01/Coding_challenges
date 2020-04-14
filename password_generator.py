
# Challenges proposed at https://www.codementor.io/@ilyaas97/6-python-projects-for-beginners-yn3va03fs

import random
import numpy as np
import string

#  Password generator

# function to create a random password
# We should define some random variables. A first variable, p1, draws a number from (0.4, 0.7) that defines
# the proportion of letters. If the password length is n, the proportion of letters will be given by int(p1*n).
# The latter, p2, is uniformly drawn from (0.15, 0.3) and defines the proportion of special characters.
# Moreover, we draw uniformly a variable, p, from (0,1), such that if it is bigger than 0.5, the appended letter is
# uppercase, otherwise it is lowercase. Once the password has been created, we shuffle all its characters randomly.
# Note that the minimum length of the password must be 7 and the previous intervals guarantee that the password contains
# all of letters, characters and numbers with no exclusions. For example, even in the case p2 = 0.15 and n=7,
# we would have at least b=1 special character.

def create_psw(n):

    letters = "abcdefghijklmnopqrstuvwxyz"
    characters = ",-_.*'!?^|#@()[]{}&%$£/=+"
    numbers = "0123456789"

    p1 = np.random.uniform(0.4, 0.7)
    p2 = np.random.uniform(0.15,0.3)

    a = int(p1*n) # proportion of letters
    b = int(p2*n) # proportion of special characters
    c = n-b-a # proportion of numbers

    psw = ""


    for i in range(a):
        p = np.random.uniform(0, 1)
        if p > 0.5:
            psw += random.choice(letters).upper()
        else:
            psw += random.choice(letters).lower()

    for i in range(b):
        psw += random.choice(characters)

    for i in range(c):
        psw += random.choice(numbers)

    psw_list = list(psw)
    random.shuffle(psw_list)
    password = ''.join(psw_list)

    return password

# Function to call if the password length is smaller than 6, in which case it would not be safe 
def error():
    return "Sorry, this password length makes the password weak. Try with a length equal to or higher than 6."


if __name__ == '__main__':

    while True:
        try:
            psw_length = int(input("Type the length of your password: "))
            break
        except ValueError:
            print("Error. Type a number that indicates the length of your password.")

    if psw_length > 6:
        result = create_psw(psw_length)
        print(result)
    else:
        print(error())


