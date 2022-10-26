
'''
DESAFIO N~'22
 * CONJUNTOS
 * Dificultad: FÁCIL
 *
Enunciado: Crea una función que reciba dos array, un booleano y retorne un array.
  - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
  - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
  - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
'''

def calculateSet(first, second, common):
    if common is True:
        salida = set(first) & set(second)#       interseccion
    else:
        salida = set(first) ^ set(second)#       Symmetric Difference
    return salida

print(f"{calculateSet((1, 2, 3, 3, 4), (2, 2, 3, 3, 3, 4, 6), True)=}")
print(f"{calculateSet((1, 2, 3, 3, 4), (2, 2, 3, 3, 3, 4, 6), False)=}")
