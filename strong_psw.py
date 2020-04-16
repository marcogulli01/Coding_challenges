
# Solutions of the challenge proposed on Hackerrank at https://www.hackerrank.com/challenges/strong-password/problem


import math
import random
import re
import sys

# The function will initialize a variable count to 0, which will be raised by 1 for each character contained into
# one of the sets of digits, lowercase, uppercase letters and symbols. Eventually, the function returns the maximum
# between count and 6-n. We should remember that the minimum password length is indeed 6.

def minimumNumber(n, password):


    count = 0

    if any(i.isdigit() for i in password) == False:
        count += 1
    if any(i.islower() for i in password) == False:
        count += 1
    if any(i.isupper() for i in password) == False:
        count += 1
    if any(i in '!@#$%^&*()-+' for i in password) == False:
        count += 1


    return max(count, 6 - n)


if __name__ == '__main__':

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    print(str(answer))
