
'''
DESAFIO N~'13
 * FACTORIAL RECURSIVO
 * Dificultad: FÁCIL
Enunciado: Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.

'''


def factorial(n):
    salida=0
    if (n < 0) :
        salida = False 
    elif (n <= 1) :
        salida += 1 
    else:
        salida += n * (factorial(n - 1))
    return salida

def factorial2(n):
    if (n < 0) :
        salida = False 
    salida = 1
    while n > 0:
        salida *= n
        n -=1
    return salida


for fact in range(11):
    print(f'{fact}! = {factorial(fact)}')
for fact in range(11):
    print(f'{fact}! = {factorial2(fact)}')
