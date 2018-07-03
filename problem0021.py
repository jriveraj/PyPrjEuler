# Amicable numbers
# Problem 21
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import math
from datetime import datetime

def isPrime(nPrime):
    if nPrime == 1:
        return True
    elif nPrime < 4:
        return True
    elif nPrime % 2 == 0:
        return False
    elif nPrime < 9:
        return True
    elif nPrime % 3 == 0:
        return False
    else:
        r = int(math.sqrt(nPrime))
        f = 5
        while f <= r:
            if nPrime % f == 0:
                return False
            elif nPrime % (f + 2) == 0:
                return False
            f = f + 6
        return True

def getfactors(n):
    nFactors = []
    nFactors.append(1)
    if isPrime(n):
        return nFactors
    nLastMax = n
    i = 2

    while i < nLastMax:
        if n % i == 0:
            nFactors.append(i)
            nLastMax = int(n / i)
            if i != nLastMax:
                nFactors.append(nLastMax)
        i += 1
    nFactors.sort()
    # nFactors.pop()
    return nFactors

def sumelmn(lList):
    sSum = 0
    for nNum in lList:
        sSum += nNum
    return sSum

StartTime = datetime.now()

dDir = {}
lAmic = []
for i in range(1,10000):
    nRes = sumelmn(getfactors(i))
    if nRes in dDir and dDir[nRes] == i:
        lAmic.append(nRes)
        lAmic.append(i)
        # print(dDir[nRes], i)
    dDir[i] = nRes
print(lAmic)
print(sumelmn(lAmic))
print(StartTime, datetime.now(), datetime.now() - StartTime )