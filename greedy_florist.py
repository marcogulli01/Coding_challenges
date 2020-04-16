
# Solutions of the challenge proposed on Hackerrank at https://www.hackerrank.com/challenges/greedy-florist/problem


import math
import random
import re
import sys

# The idea behind the solution of the problem is that the most expensive flowers should be bought first and the cheapest
# ones should be bought last. This will require to sort the c array into descending order and to multiply its first
# elements (largest ones) by the lowest number of friends. A greedy algorithm built with this idea would yield the
# optimal result. 

def getMinimumCost(k, c):

    c = sorted(c, reverse=True) # sort c according to descending order

    a = len(c) // k # quotient between n and k

    b = len(c) % k # reminder n mod k

    arr = []

    # slice the list of costs, c, into sublists, each of length k

    if b == 0:
        for i in range(a):
            arr += [c[k*i : k*(i+1)]]
    else:
        for i in range(a):
            arr += [c[k * i:k * (i + 1)]]
        arr += [c[k * a:n]]

    sums = []

    for i in range(len(arr)):
        sums += [sum(arr[i])] # to store the sums of the previous sublists

    prices = [sums[i] * (i+1) for i in range(len(sums))] # to save the prices of the greedy florist

    return sum(prices)


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    print(getMinimumCost(k, c))
