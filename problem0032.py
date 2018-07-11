# Pandigital products
# #
# #
# # Problem 32
# #
# #
# #
# # We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# #
# # The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# #
# # Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# #
# # HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.


from datetime import datetime
import math

StartTime = datetime.now()
nResult = 0
nTarget = 10
nStopAt = 1000000
nCycles = 0

# text_file2 = open("files/p032_output.txt", "r")
# sOutput = text_file2.readlines()
# print(sOutput)
# text_file2.close()

text_file = open("files/p032_output.txt", "w+")

for a in range(1, nTarget):
    for b in range(1, nTarget):
        if a != b:
            for c in range(1, nTarget):
                if c != a and c != b:
                    for d in range(1, nTarget):
                        if d != a and d != b and d != c:
                            for e in range(1, nTarget):
                                if e != a and e != b and e != c and e != d:
                                    for f in range(1, nTarget):
                                        if f != a and f != b and f != c and f != d and f != e:
                                            for g in range(1, nTarget):
                                                if g != a and g != b and g != c and g != d and g != e and g != f:
                                                    for h in range(1, nTarget):
                                                        if h != a and h != b and h != c and h != d and h != e and h != f and h != g:
                                                            for i in range(1, nTarget):
                                                                if i != a and i != b and i != c and i != d and i != e and i != f and i != g and i != h:
                                                                # ---------------------------------------------------------------
                                                                    nResult += 1
                                                                    # if nResult >= nStopAt - 2:
                                                                    # print(a, b, c, d, e, f, g, h, i)
                                                                    text_file.write(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+"\n")
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

text_file.close()

print(StartTime, datetime.now(), datetime.now() - StartTime )
# print(nResult, nCycles)
