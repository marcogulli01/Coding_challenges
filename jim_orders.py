
# Solutions of the challenge proposed on Hackerrank at https://www.hackerrank.com/challenges/jim-and-the-orders/problem

import math
import random
import re
import sys


def jimOrders(orders):

    total = [] # list of lists

    for i in range(len(orders)):
        a = orders[i][0]+orders[i][1]
        total.append([i+1,a]) # the first element is the customer number, the second element is prep time + order number

    total = sorted(total, key=lambda x: x[1]) # sort the previous list according to ascending order

    ord = [] # array in which customer numbers will be stored

    for i in range(len(total)):
        ord += [total[i][0]]

    return ord



if __name__ == '__main__':

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = ''.join(map(str, jimOrders(orders)))

    print(result)
