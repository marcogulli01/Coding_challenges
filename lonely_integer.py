
# Solutions of the challenge proposed on Hackerrank at https://www.hackerrank.com/challenges/angry-professor/problem


import math
import random
import re
import sys

# To solve the challenge, we can return that item whose number of occurences across a is equal to 1


def lonelyinteger(a):

    for item in a:
        if a.count(item) == 1:
            return item

if __name__ == '__main__':

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    print(result)

