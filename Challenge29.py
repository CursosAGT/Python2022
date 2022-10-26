
'''
DESAFIO N~'29
 * ORDENA LA LISTA
 * Dificultad: FÁCIL
 *
Enunciado: Crea una función que ordene y retorne una matriz de números.
  - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro adicional
     o "Desc" para indicar si debe ordenarse de menor a mayor o de mayor a menor.
  - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
'''


def sort(numbers, ascn):

    sortedNumbers = []
    
    for index,number in enumerate(numbers):
        if ascn==True:
            if index==0:
                sortedNumbers.append(number)
            elif number <sortedNumbers[0]:
                sortedNumbers.insert(0,number)
            elif number >sortedNumbers[-1]:
                sortedNumbers.append(number)
        else:
            if index==0:
                sortedNumbers.append(number)
            elif number >sortedNumbers[0]:
                sortedNumbers.insert(0,number)
            elif number <sortedNumbers[-1]:
                sortedNumbers.append(number)
    return sortedNumbers


print(sort((4, 6, 1, 8, 2), True)) # 1, 2, 4, 6, 8
print(sort((4, 6, 1, 8, 2), False)) # 8, 6, 4, 2, 1

