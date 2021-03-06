# Problem Description
#
# Problem Details

from datetime import datetime
import math

def isPrime(nPrime):
    if nPrime == 1:
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

StartTime = datetime.now()
nResult = 1

import math

nLimit = 1001
bExit = False
nMult = -1
nPrimeCounterMax = 0

a = nLimit * nMult
while a < nLimit + 1:
    b = nLimit * nMult
    while b < nLimit + 1:
        n = nPrimeCounter = 0
        bExit = False
        while n <= nLimit + 1 and not bExit:
            nResult = (n * n) + (n * a) + b
            if isPrime(abs(nResult)):
                nPrimeCounter += 1
                # print(n, nResult)
            else:
                if nPrimeCounter >= nPrimeCounterMax:
                    print(n, a, b, nPrimeCounter)
                    nPrimeCounterMax = nPrimeCounter
                bExit = True
            n += 1
        b += 1
    a += 1

# n = nPrimeCounter = 0
# bExit = False
# a = -41
# b = -41
#
# while n <= nLimit + 1 and not bExit:
#     nResult = n * (n + a) + b
#     if isPrime(nResult):
#         nPrimeCounter += 1
#         # print(n, nResult)
#     else:
#         if nPrimeCounter >= nPrimeCounterMax:
#             print(n, a, b, nPrimeCounter)
#             nPrimeCounterMax = nPrimeCounter
#         bExit = True
#     n += 1

print(StartTime, datetime.now(), datetime.now() - StartTime )
print(nResult, nPrimeCounter)
