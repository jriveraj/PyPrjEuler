#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

nMaxNum = int( input( "Max Number: " ) )
print( nMaxNum )

nCounter = 0
nResult = 0

while nCounter < nMaxNum - 1:
    nCounter = nCounter + 1
    if nCounter % 3 == 0:
        nResult = nResult + nCounter
    elif nCounter % 5 == 0:
        nResult = nResult + nCounter
    #print( nCounter )

print( nResult )

