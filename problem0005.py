# Smallest multiple
# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from datetime import datetime

starttime = datetime.now()

nNum = 20
nInter = 0

def IsSmallestMultiple(nNumber):
    global nInter
    # for i in range(2, nNum + 1):
    # for i in range(nNum + 1, 2):
    i = nNum
    while i != 2: #nNum:
        nInter += 1
        i -= 1
        if nNumber % i != 0:
            return False
    return True

def IsSmallestMultiple2(nNumber):
    global nInter
    for i in range(2, nNum + 1):
        nInter += 1
        if nNumber % i != 0:
            return False
    return True

nMultiple = 1
# nMultiple = 12252240

while not IsSmallestMultiple(nMultiple):
    nMultiple += 1
print( starttime, datetime.now())
print(nMultiple, nInter)


# starttime = datetime.now()
# nInter = 0
# while not IsSmallestMultiple2(nMultiple):
#     nMultiple += 1
# print( starttime, datetime.now())
# print(nMultiple, nInter)
