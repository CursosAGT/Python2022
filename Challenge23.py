
'''
DESAFIO N~'23
 * MÁXIMO COMÚN DIVISOR Y MÍNIMO COMÚN MÚLTIPLO
 * Dificultad: MEDIA
 *
 * Enunciado: Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
'''

def mcd(firstNumber, secondNumber): 
    while (firstNumber != 0 and secondNumber != 0):
        firstNumber,secondNumber = secondNumber,firstNumber % secondNumber
    return firstNumber + secondNumber

def mcdRecursive(firstNumber, secondNumber): 
    if (firstNumber == 0 or secondNumber == 0):
        salida = firstNumber + secondNumber
    else:
        salida = mcdRecursive(secondNumber, firstNumber % secondNumber)
    return salida
def mcm(firstNumber, secondNumber): 
    return (firstNumber * secondNumber) / mcd(firstNumber, secondNumber)

print(f"{mcd(56, 180)=}")
print(f"{mcdRecursive(56, 180)=}")
print(f"{mcm(56, 180)=}")
