

# Solution of the challenge proposed on Hackerrank at https://www.hackerrank.com/challenges/the-birthday-bar/problem

import math
import random
import sys


def birthday(s, d, m):

    return len([1 for i in range(len(s)-m+1) if sum(s[i:i+m])==d])


if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    print(birthday(s, d, m))

