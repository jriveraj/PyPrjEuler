#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?


#nTarget = 600851475143
nTarget = 13195

nPrimes = []
nPrimes.append( 2 )

def GeneratePrimeList():
    nCount = 3
    while nCount <= nTarget:
        nCountPrimes = 0
        bIsPrime = True
        while nCountPrimes < len( nPrimes ) and bIsPrime:
            if nCount % nPrimes[ nCountPrimes ] == 0:
                bIsPrime = False
            nCountPrimes = nCountPrimes + 1
        if bIsPrime:
            nPrimes.append( nCount )
        nCount  = nCount + 2

GeneratePrimeList()

nCount = len( nPrimes )

nTarget = 600851475143

while nCount > 0:
    nCount = nCount - 1
    if nTarget % nPrimes[ nCount ] == 0:
        print( nPrimes[ nCount ] )
