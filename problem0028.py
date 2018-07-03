# Number spiral diagonals
#
#
# Problem 28
#
#
#
# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
#  20  7  8  9 10
#  19  6  1  2 11
#  18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

from datetime import datetime

StartTime = datetime.now()
nResult = 0

nLimit = 1001
bExit = False
i = 1
nDelta = 2
bIncrementDelta = False
nCounter = 0


while i <= nLimit * nLimit:
    # print(i, nCounter)
    nResult += i
    nCounter += 1
    i += nDelta
    if nCounter == 4:
        nCounter = 0
        nDelta += 2


print(StartTime, datetime.now(), datetime.now() - StartTime )
print(nResult)
