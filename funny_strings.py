
# Solution of the challenge Funny String proposed on HackerRank at https://www.hackerrank.com/challenges/funny-string/problem


import math
import random
import re
import sys

# After converting each letter of s to its ascii value, we do the same for the reverted string s. Two arrays
# containing the absolute value of the differences between consecutive elements are then computed.
# If the two arrays are equal, then we return "Funny", otherwise we return "Not Funny"

def funnyString(s):

    ascii_values = [ord(item) for item in list(s)]

    ascii_values_rev = [ord(item) for item in list(s)[::-1]]

    diff_ascii_values = [abs(ascii_values[i+1]-ascii_values[i]) for i in range(len(ascii_values)-1)]
    diff_ascii_values_rev = [abs(ascii_values_rev[i+1]-ascii_values_rev[i]) for i in range(len(ascii_values_rev)-1)]


    if diff_ascii_values == diff_ascii_values_rev:
        return "Funny"
    else:
        return "Not Funny"


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        print(result)




