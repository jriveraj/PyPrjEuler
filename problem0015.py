# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20×20 grid?

from datetime import datetime
import math

class nNode:
    def __init__(self, sA: object, sB: object) -> object:
        self.A = sA
        self.B = sB
        self.name = "(" + str(self.A) + ", " + str(self.B) + ")"
        self.left = 0
        self.down = 0
        self.right = 0
        self.up = 0
        self.value = -1
        self.isnull = False
        if sA == "" or sB == "":
            self.isnull = True
    def show_me(self):
        return self.name


nTarget = 21
nChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nResult = 0
nInter = 0

nNodeMatrix = []

# nNodeMatrix[1 * nTarget + 1] = 53

def generateMatrix(nTarget):
    nNullNode = nNode("","")

    for x in range(0, nTarget):
        for y in range(0, nTarget):
            nNewNode = nNode(nChar[x], nChar[y])
            nNodeMatrix.append(nNewNode)

    for x in range(0, nTarget):
        for y in range(0, nTarget):
            if y != nTarget - 1:
                nNodeMatrix[x * nTarget + y].left = nNodeMatrix[(x * nTarget) + (y + 1)]
            else:
                nNodeMatrix[x * nTarget + y].left = nNullNode
            if x != nTarget - 1:
                nNodeMatrix[x * nTarget + y].down = nNodeMatrix[((x + 1) * nTarget) + y]
            else:
                nNodeMatrix[x * nTarget + y].down = nNullNode
    return nNodeMatrix[0]

def solve(nPointer, sChain):
    global nResult
    global nInter
    nInter += 1
    leftNode = nPointer.left
    downNode = nPointer.down
    if leftNode.isnull and downNode.isnull:
        nResult += 1
        # nPointer.value = nResult
    if not leftNode.isnull:
        if leftNode.value > 0:
            nResult += leftNode.value
        else:
            solve(leftNode, sChain + leftNode.name)
    if not downNode.isnull:
        if downNode.value > 0:
            nResult += downNode.value
        else:
            solve(downNode, sChain + downNode.name)

StartTime = datetime.now()

# StartNode = generateMatrix(nTarget)
# solve(StartNode, StartNode.name)
nResult = nTarget * 2 - 2
nResult = math.factorial(nResult) / (math.factorial(nResult/2)*math.factorial(nResult/2))

# 40116600 115000920

# nResult = 1
# for i in range(20, 39):
#     nResult *= i
#     print(i, nResult)

print(StartTime, datetime.now(), datetime.now() - StartTime )
print(nResult, nInter)