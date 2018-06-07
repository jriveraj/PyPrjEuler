# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

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
nResult = 2

for i in range(1, 2000000, 2):
    if isPrime(i):
        nResult += i

print(StartTime, datetime.now(), datetime.now() - StartTime )
print(nResult)
