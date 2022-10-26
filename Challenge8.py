
'''
DESAFIO N~8
 * DECIMAL A BINARIO
 * Dificultad: FÁCIL
Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
'''



def decimalToBinary(decimal): 

    number = decimal
    binary = ""
    while (number != 0) :
        reminder = number % 2
        number = number //2
        binary = f"{reminder}"+binary

    return binary

print(f"{decimalToBinary(387)=}")
print(f"{decimalToBinary(0)=}")
print(f"{decimalToBinary(1)=}")
print(f"{decimalToBinary(2)=}")
print(f"{decimalToBinary(3)=}")
print(f"{decimalToBinary(4)=}")
print(f"{decimalToBinary(5)=}")
print(f"{decimalToBinary(6)=}")
print(f"{decimalToBinary(7)=}")
print(f"{decimalToBinary(8)=}")
print(f"{decimalToBinary(9)=}")
print(f"{decimalToBinary(10)=}")
print(f"{decimalToBinary(32)=}")
print(f"{decimalToBinary(256)=}")
print(f"{decimalToBinary(1024)=}")
