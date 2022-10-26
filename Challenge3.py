
'''
DESAFIO N~3
 * ¿ES UN NÚMERO PRIMO?
 * Dificultad: MEDIA
Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
'''


def isPrime(number): 

    if (number < 2):
        return  False
    for i in range(2, number) :
        if (number % i == 0) :
            return False
    return True
for number in range(1,101):
    salida=isPrime(number)
    print (f"numero {number} en primo {salida}")



def is_prime2():

    for number in range(1, 101):

        if number >= 2:

            is_divisible = False

            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break
                    
            if not is_divisible:
                print(number)

is_prime2()
