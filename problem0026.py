# Reciprocal cycles
# Problem 26
# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def division(numerador, denominador, resultado = 0):
    if numerador >= denominador:
        numerador -= denominador
        resultado += 1
        resultado = division( numerador, denominador, resultado)
    return resultado

def evalua(cadena):
    if len(cadena) % 2 != 0 or len(cadena) < 11:
        return False
    elif cadena[int(len(cadena) / 2):] == cadena[:int(len(cadena) / 2)]:
        return True
    return False

def divide_dec(numerador, denominador, primer=0, cadena=''):
    # if evalua(cadena[zeros:]):
    #     return ''
    if numerador >= denominador:
        cociente = division(numerador, denominador)
        residuo = numerador - (cociente * denominador)
        if residuo * 10 == primer:
            return 'X'
        if residuo == 0:
            sResult = str(cociente)
        else:
            if primer == 0:
                primer = residuo * 10
            sResult = str(cociente) + divide_dec(residuo * 10, denominador, primer, cadena + str(cociente))
    else:
        # if zeros - 0 == len(cadena):
        #     zeros += 1
        sResult = '0' + divide_dec(numerador * 10, denominador, primer, cadena + '0')
    return sResult


def divide(numerador, denominador):
    if numerador >= denominador:
        cociente = division(numerador, denominador)
        residuo = numerador - (cociente * denominador)
        if residuo == 0:
            sResult = str(cociente)
        else:
            sResult = str(cociente) + '.' + divide_dec(residuo * 10, denominador)
    else:
        sResult = '0' + '.' + divide_dec(numerador * 10, denominador)
    return sResult

# print(divide(1, 24))
# print(divide(1, 75))
# print(divide(1, 69))
# print(divide(1, 900))
# print(divide(1, 491))
# print(divide(1, 991))

for i in range(999, 1, -2):
    nCounter = 0
    sResult = divide(1, i)
    print(i, (len(sResult) - 2) / 2, sResult)

# print(checa('01234561235', 4)