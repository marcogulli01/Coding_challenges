
# Solution of the challenge proposed on Hackerrank at shorturl.at/myDOW


# In order to know whether two strings share a common substring, it suffices to determine if they have
# at least one common letter. This implies that, after converting them into sets, their intersection
# should not be empty.



import math

import random
import re
import sys


def twoStrings(s1, s2):

    str1 = set(s1)
    str2 = set(s2)

    intr = str1.intersection(str2)


    if intr != set():
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        print(result)


