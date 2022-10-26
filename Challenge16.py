
'''
DESAFIO N~'16
 * EN MAYÚSCULA
 * Dificultad: FÁCIL
 * sin usar .title
 * Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
 *
'''


def capitalize(text):
    capitalizedText=''
    for index,caracter in enumerate(text):
        if index ==0 or text[index-1]==' ' or not text[index-1].isalpha():
            capitalizedText +=caracter.upper()
        else:
            capitalizedText +=caracter.lower()
    return capitalizedText
    

print(f'{"¿hola qué tal estás?".title()=}')
print(f'{capitalize("¿hola qué tal estás?")=}')


print(f'{"¿hola      qué tal estás?".title()=}')
print(f'{capitalize("¿hola      qué tal estás?")=}')

print(f'{"El niño ñoño".title()=}')
print(f'{capitalize("El niño ñoño")=}')

