# Longest Collatz sequence
# Problem 14
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

from datetime import datetime
# import math

nCollatz_Seq = {}
nMaxMax = 0

def collaltz(n, nCounter):
    global nCollatz_Seq
    global nMaxMax
    nNew = 0
    if n > nMaxMax:
        nMaxMax = n
    if  int(n) in nCollatz_Seq:
        return nCollatz_Seq[int(n)]
    if n == 1:
        nCollatz_Seq[n] = 1
        return 1
    if n % 2 == 0:
        nNew = int(n / 2)
    else:
        nNew = int(3 * n + 1)
    nCollatz_Seq[n] = collaltz(nNew, nCounter ) + nCounter
    return nCollatz_Seq[n]
StartTime = datetime.now()
nResult = 0

# for i in range(0, 11):
#     nCollatz_Seq.append(0)
#
nAux = 0
for i in range(1, 999999):
    nMax = collaltz(i, 1)
    if nMax > nAux:
        print( i, nMax, nMaxMax)
        nAux = nMax
# print( 13, collaltz(13, 1))


print(StartTime, datetime.now(), datetime.now() - StartTime )
print(nResult)