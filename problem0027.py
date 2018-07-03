# Quadratic primes
#
#
# Problem 27
#
#
#
# Euler discovered the remarkable quadratic formula:
#
# n 2 +n+41
# n2+n+41
#
#
# It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
# 0≤n≤39
# . However, when n=40,40 2 +40+41=40(40+1)+41
# n=40,402+40+41=40(40+1)+41
#  is divisible by 41, and certainly when n=41,41 2 +41+41
# n=41,412+41+41
#  is clearly divisible by 41.
#
# The incredible formula n 2 −79n+1601
# n2−79n+1601
#  was discovered, which produces 80 primes for the consecutive values 0≤n≤79
# 0≤n≤79
# . The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
# n 2 +an+b
# n2+an+b
# , where |a|<1000
# |a|<1000
#  and |b|≤1000
# |b|≤1000
#
#
#
# where |n|
# |n|
#  is the modulus/absolute value of n
# n
#
# e.g. |11|=11
# |11|=11
#  and |−4|=4
# |−4|=4
#
# Find the product of the coefficients, a
# a
#  and b
# b
# , for the quadratic expression that produces the maximum number of primes for consecutive values of n
# n
# , starting with n=0
# n=0
# .

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
