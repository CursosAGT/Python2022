'''
DESAFIO N~'38
 * BINARIO A DECIMAL
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa se encargue de transformar un número binario a decimal sin utilizar
 * funciones propias del lenguaje que lo hagan directamente.
'''



def binaryToDecimal(binary):

    length = len(binary)-1
    decimal = 0
    for index ,digitChar in enumerate(binary[::-1]):
        if (digitChar == '0' or digitChar == '1') :
            decimal += int(digitChar) * 2.0**index
        else :
            return None
    return decimal

print(f'{binaryToDecimal("00110")=}')
print(f'{binaryToDecimal("01100")=}')
print(f'{binaryToDecimal("000000000")=}')
print(f'{binaryToDecimal("00210")=}')
print(f'{binaryToDecimal("001101001110")=}')
print(f'{binaryToDecimal("00b10")=}')
print(f'{binaryToDecimal("")=}')
print(f'{binaryToDecimal("-00110")=}')
print(f'{binaryToDecimal(" ")=}')
print(f'{binaryToDecimal(" 10011")=}')
print(f'{binaryToDecimal("1O1OO11")=}')
print(f'{binaryToDecimal("1010011")=}')
