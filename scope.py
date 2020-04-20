
# Solution of the challenge proposed on Hackerrank at https://www.hackerrank.com/challenges/30-scope/problem

# The solution of the problem could be implemented just taking the absolute value between the last and the first
# element of the list a, sorted according to ascending order

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
    def computeDifference(self):
        self.maximumDifference = abs(sorted(a)[len(a)-1]-sorted(a)[0])

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)