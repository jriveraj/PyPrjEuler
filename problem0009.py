# Special Pythagorean triplet
# Problem 9
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from datetime import datetime
# import math
StartTime = datetime.now()

#  M^2 - 2 M a - 2 M b + 2 a b = 0
def evaluate(a, b):
    nResult = M * M
    nResult -= 2 * M * a
    nResult -= 2 * M * b
    nResult += 2 * a * b
    if nResult == 0:
        return True
    return False

nInter = 0
M = 1000

for a in range(1, 1000):
    for b in range(a + 1, 1000):
        # print(a, b)
        if evaluate(a, b):
            print(a, b)
        nInter += 1

print(StartTime, datetime.now(), datetime.now() - StartTime )
print(nInter)
