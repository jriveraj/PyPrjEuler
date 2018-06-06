#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

def IsPalindrome( nNumber ):
    sNumber = str( nNumber )

    nCount = 0
    while nCount < len( sNumber ) / 2 - 0.5 :
        #print( sNumber[nCount], sNumber[ len( sNumber ) - nCount - 1] )
        if sNumber[nCount] != sNumber[ len( sNumber ) - nCount - 1]:
            return False
        nCount = nCount + 1
    return True

nCeiling = 998001

i = 999

bFoundIt = False

while i > 900 and not bFoundIt:
    j = 999
    while j > 900 and not bFoundIt:
        j = j - 1
        if IsPalindrome( i * j ) :
            bFoundIt = True
    i = i - 1

print( i, j, i * j)