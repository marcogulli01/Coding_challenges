

# Solution of the challenge proposed on Hackerrank at https://www.hackerrank.com/challenges/kangaroo/problem


import math
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):

    if x2-x1 > v1 and v1 < v2: # if the first kangaroo starts before than the second and has a shorter skip, it will never catch it up
        answer = "NO"
    else:
        if v1 != v2:
            if (x2-x1) % (v2-v1) == 0: # if the gap between the initial positions is a multiple of the skips gap, they will meet
                answer = "YES"
            else:
                answer = "NO"
        else:
            answer = "NO"

    return answer

if __name__ == '__main__':

    x1V1X2V2 = input().split() # read the input

    x1, v1, x2, v2 = int(x1V1X2V2[0]), int(x1V1X2V2[1]), int(x1V1X2V2[2]), int(x1V1X2V2[3]) # split the previous input on different lines

    print(kangaroo(x1, v1, x2, v2))


