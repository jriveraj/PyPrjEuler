# Problem Description
#
# Problem Details

from datetime import datetime
import math

def GetTriangleSample(x, y, steps):
    global aLine
    sampleTriangle = []

    for stepX in range(0, steps):
        sampleLine = []
        for stepY in range(0, stepX+1):
            sampleLine.append(int(aLine[stepX+x][stepY+y]))
        sampleTriangle.append(sampleLine)

    return sampleTriangle

def solveTriangle(lTriangle):
    sumTriangle = []
    steps = len(lTriangle)
    x = y = 0
    for stepX in range(0, steps):
        sampleLine = []
        sumLine = []
        for stepY in range(0, stepX+1):
            if stepX == 0 and stepY == 0:
                sumLine.append(lTriangle[stepX+x][stepY+y])
            elif stepY == 0:
                sumLine.append(lTriangle[stepX+x][stepY+y]+sumTriangle[stepX + x - 1][stepY + y])
            elif stepY == stepX:
                sumLine.append(lTriangle[stepX+x][stepY+y]+sumTriangle[stepX + x - 1][stepY + y - 1])
            else:
                if sumTriangle[stepX + x - 1][stepY + y] > sumTriangle[stepX + x - 1][stepY + y - 1]:
                    sumLine.append(lTriangle[stepX+x][stepY+y]+sumTriangle[stepX + x - 1][stepY + y])
                else:
                    sumLine.append(lTriangle[stepX+x][stepY+y]+sumTriangle[stepX + x - 1][stepY + y - 1])
            sampleLine.append(lTriangle[stepX+x][stepY+y])
        sumTriangle.append(sumLine)
    return sumTriangle
        # print(sampleLine)
        # print(sumLine)




StartTime = datetime.now()
nResult = 1

# text_file = open("files/p018_triangles.txt", "r")
text_file = open("files/p067_triangle", "r")

sTriangle = text_file.readlines()
aLine = []

nTarget = 100

for sLine in sTriangle:
    aLine.append(sLine.split())

miniTriangle = GetTriangleSample(0,0,nTarget)

resultTriangle = solveTriangle(miniTriangle)

print(resultTriangle[nTarget - 1])

text_file.close()

print(StartTime, datetime.now(), datetime.now() - StartTime )
print(nResult)
