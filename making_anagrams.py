
# Solution of the challenge proposed on Hackerrank at https://www.hackerrank.com/challenges/making-anagrams/problem

import math
import random
import re
import sys

# Once the two strings have been merged, we should count how many times a certain character appears in both.
# If the character appears in both strings, we count the difference of the numbers of occurrences in the strings.
# If the character appears in only one string, we count how many times it does.
# The total count is exactly the number of letters we should delete to make an anagram.

def makeAnagram(a, b):

    characters = list(set(a+b))

    counts = 0

    for item in characters:
        if item in list(a) and item in list(b):
            counts += abs(a.count(item)-b.count(item))
        elif item in list(a) and item not in list(b):
            counts += a.count(item)
        elif item in list(b) and item not in list(a):
            counts += b.count(item)

    return counts


if __name__ == '__main__':

    a = input()

    b = input()

    res = makeAnagram(a, b)

    print(res)

