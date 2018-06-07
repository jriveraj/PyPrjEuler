# 10001st prime
# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

from datetime import datetime
import math

def isPrime(nPrime):
    if nPrimes == 1:
        return False
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



def GeneratePrimeList():
    nCount = 3
    global nInter
    while len(nPrimes) <= nPrimesTarget:
        nInter += 1
        nCountPrimes = 0
        bIsPrime = True
        while nCountPrimes < len( nPrimes ) and bIsPrime:
            if nCount % nPrimes[ nCountPrimes ] == 0:
                bIsPrime = False
            nCountPrimes = nCountPrimes + 1
        if bIsPrime:
            nPrimes.append( nCount )
        nCount  = nCount + 2

def GeneratePrimeList2():
    nCount = 3
    global nInter
    while len(nPrimes) <= nPrimesTarget:
        nInter += 1
        nCountPrimes = 0
        if isPrime(nCount):
            nPrimes.append( nCount )
        nCount  = nCount + 2

StartTime = datetime.now()
# nTarget = 13195

nPrimesTarget = 10000
nPrimes = []
nPrimes.append(2)
nInter = 0

GeneratePrimeList()

print(StartTime, datetime.now(), datetime.now() - StartTime )
print(nInter, len(nPrimes), nPrimes[len(nPrimes)-2])
print( nPrimes)
# print(nPrimes2)

StartTime = datetime.now()
# nTarget = 13195


nPrimes = []
nPrimes.append(2)
nInter = 0

GeneratePrimeList2()

print(StartTime, datetime.now(), datetime.now() - StartTime )
print(nInter, len(nPrimes), nPrimes[len(nPrimes)-2])
print( nPrimes)
