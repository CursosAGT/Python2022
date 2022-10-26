
'''
DESAFIO N~'32
 * EL SEGUNDO
 * Dificultad: FÁCIL
 *
Enunciado: Dado un listado de números, encuentra el SEGUNDO más grande.
'''

def findSecondGreater(*numbers): 
    numbers=list(numbers) 
    if len(numbers)>=2:
        sortedNumbers = []
        found = False
        while found == False:
            found = True
            for index in range(0,len(numbers)-1) :
                if numbers[index]>numbers[index+1] :
                    found = False
                    numbers[index],numbers[index+1]=numbers[index+1],numbers[index]
                elif numbers[index]==numbers[index+1] :
                    numbers.pop(index)
                    break
    return "Error, no hay 2 elementos" if len(numbers)<2 else f'el segundo elemento mayor es {numbers[-2]}'
    

print(findSecondGreater(9, 8, 7, 6, 5, 4, 3, 2, 1, 0))
print(findSecondGreater(4, 6, 1, 8, 2))
print(findSecondGreater(4, 6, 8, 8, 6))
print(findSecondGreater(4, 4))
print(findSecondGreater(2, 4))
print(findSecondGreater())
print("*"*100)
def findSecondGreater_2(*numbers): 
    numbers=sorted(list(set(numbers))) 
    return "Error, no hay 2 elementos" if len(numbers)<2 else f'el segundo elemento mayor es {numbers[-2]}'


print(findSecondGreater(9, 8, 7, 6, 5, 4, 3, 2, 1, 0))
print(findSecondGreater_2(4, 6, 1, 8, 2))
print(findSecondGreater_2(4, 6, 8, 8, 6))
print(findSecondGreater_2(4, 4))
print(findSecondGreater_2(2, 4))
print(findSecondGreater_2())
print("*"*100)
