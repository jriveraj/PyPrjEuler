# Lexicographic permutations
#
#
# Problem 24
#
#
#
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from datetime import datetime
import math

StartTime = datetime.now()
nResult = 0
nTarget = 10
nStopAt = 1000000
nCycles = 0

# def solve(cList):
#     bList = []
#     if len(cList) == 1:
#         return cList[0]
#     for i in cList:
#         for a in cList:
#             if a != i:
#                 bList.append(a)
#         print(i + solve(bList))
#
# cFullList = [ '0', '1', '2', '3' ]
#
# nResult = solve(cFullList)

# import math

for a in range(0, nTarget):
    for b in range(0, nTarget):
        if a != b:
            for c in range(0, nTarget):
                if c != a and c != b:
                    for d in range(0, nTarget):
                        if d != a and d != b and d != c:
                            for e in range(0, nTarget):
                                if e != a and e != b and e != c and e != d:
                                    for f in range(0, nTarget):
                                        if f != a and f != b and f != c and f != d and f != e:
                                            for g in range(0, nTarget):
                                                if g != a and g != b and g != c and g != d and g != e and g != f:
                                                    for h in range(0, nTarget):
                                                        if h != a and h != b and h != c and h != d and h != e and h != f and h != g:
                                                            for i in range(0, nTarget):
                                                                if i != a and i != b and i != c and i != d and i != e and i != f and i != g and i != h:
                                                                    for j in range(0, nTarget):
                                                                        if j != a and j != b and j != c and j != d and j != e and j != f and j != g and j != h and j != i:
                                                                        # ---------------------------------------------------------------
                                                                            nResult += 1
                                                                            if nResult >= nStopAt - 2:
                                                                                print(nResult, a, b, c, d, e, f, g, h, i, j)
                                                                            if nResult == nStopAt + 2:
                                                                                break
                                                                        nCycles += 1
                                                                        # ---------------------------------------------------------------
                                                                        if nResult == nStopAt + 2:
                                                                            break
                                                                if nResult == nStopAt + 2:
                                                                    break
                                                        if nResult == nStopAt + 2:
                                                            break
                                                if nResult == nStopAt + 2:
                                                    break
                                        if nResult == nStopAt + 2:
                                            break
                                if nResult == nStopAt + 2:
                                    break
                        if nResult == nStopAt + 2:
                            break
                if nResult == nStopAt + 2:
                    break
        if nResult == nStopAt + 2:
            break

# for a in range(0, nTarget):
#     for b in range(0, nTarget):
#         for c in range(0, nTarget):
#             for d in range(0, nTarget):
#                 nCycles += 1
#                 if \
#                         a != b and \
#                                 c != a and c != b and \
#                                 d != a and d != b and d != c:
#                     nResult += 1
#                     if nResult >= nStopAt - 2:
#                         print(nResult, a, b, c, d)
#                     if nResult == nStopAt + 2:
#                         break
#                 if nResult == nStopAt + 2:
#                     break
#             if nResult == nStopAt + 2:
#                 break
#         if nResult == nStopAt + 2:
#             break
#     if nResult == nStopAt + 2:
#         break

# for a in range(0, nTarget):
#     for b in range(0, nTarget):
#         for c in range(0, nTarget):
#             for d in range(0, nTarget):
#                 for e in range(0, nTarget):
#                     for f in range(0, nTarget):
#                         for g in range(0, nTarget):
#                             for h in range(0, nTarget):
#                                 for i in range(0, nTarget):
#                                     for j in range(0, nTarget):
#                                         if \
#                                                 a != b and \
#                                                         c != a and c != b and \
#                                                         d != a and d != b and d != c and \
#                                                         e != a and e != b and e != c and e != d and \
#                                                         f != a and f != b and f != c and f != d and f != e and \
#                                                         g != a and g != b and g != c and g != d and g != e and g != f and \
#                                                         h != a and h != b and h != c and h != d and h != e and h != f and h != g and \
#                                                         i != a and i != b and i != c and i != d and i != e and i != f and i != g and i != h and \
#                                                         j != a and j != b and j != c and j != d and j != e and j != f and j != g and j != h and j != i:
#                                             nResult += 1
#                                             if nResult >= nStopAt - 2:
#                                                 print(nResult, a, b, c, d, e, f, g, h, i, j)
#                                             if nResult == nStopAt + 2:
#                                                 break
#                                         if nResult == nStopAt + 2:
#                                             break
#                                     if nResult == nStopAt + 2:
#                                         break
#                                 if nResult == nStopAt + 2:
#                                     break
#                             if nResult == nStopAt + 2:
#                                 break
#                         if nResult == nStopAt + 2:
#                             break
#                     if nResult == nStopAt + 2:
#                         break
#                 if nResult == nStopAt + 2:
#                     break
#             if nResult == nStopAt + 2:
#                 break
#         if nResult == nStopAt + 2:
#             break
#     if nResult == nStopAt + 2:
#         break



print(StartTime, datetime.now(), datetime.now() - StartTime )
print(nResult, nCycles)
