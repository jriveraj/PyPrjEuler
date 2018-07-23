# Coin sums
# Problem 31
# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

from datetime import datetime
import math

StartTime = datetime.now()
nResult = 1
nTarget = 200
nCounter = nCyclesCounter = 0

for i in range(0,nTarget + 200, 200):
    for j in range(0, nTarget + 100 - i, 100):
        for k in range(0, nTarget + 50 - j - i, 50):
            for l in range(0, nTarget + 20 - k - j - i, 20):
                for m in range(0, nTarget + 10 - l - k - j - i, 10):
                    for n in range(0, nTarget + 5 - m - l - k - j - i, 5):
                        for o in range(0, nTarget + 2 - n - m - l - k - j - i, 2):
                            for p in range(0, nTarget + 1 - o - n - m - l - k - j - i, 1):
                                # print(i, j, k, l, m, n, o, p)
                                nCyclesCounter += 1
                                if i+j+k+l+m+n+o+p == nTarget:
                                    nCounter += 1
                                    # print(int(i/200), int(j/100), int(k/50), int(l/20), int(m/10), int(n/5), int(o/2), p, nCounter)


print(StartTime, datetime.now(), datetime.now() - StartTime )
print(nResult, nCounter, nCyclesCounter)
