# Power digit sum
# Problem 16
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 21000?

StartTime = datetime.now()
nResult = 1

for i in range(1, 1001):
    nResult *= 2

sResult = str(nResult)
nResult = 0
for digit in sResult:
    nResult += int(digit)

print(StartTime, datetime.now(), datetime.now() - StartTime )
print(nResult)