
'''
DESAFIO N~'34
 * LOS NÚMEROS PERDIDOS
 * Dificultad: FÁCIL

Enunciado: Dado un array de enteros ordenado y sin repetidos, crea una función que calcule y retorne todos los que faltan entre el mayor y el menor.
- Lanza un error si el array de entrada no es correcto.
'''





def arrayListOf(*numbers): 
    print("*"*50)
    try :
        numbers=list(numbers)
        if len(numbers) < 2 or numbers!= sorted(list(set(numbers))):
            raise LostNumbersException
            
        numbers=list(numbers)

        total =  list(range(numbers[0],(numbers[-1]+1)))
        exclude=sorted(list(set(total)-set(numbers)))
        return(f"dados:{numbers}\nfalantes:{exclude}")
    except :
        print("No cumple:")
        print("El listado no puede poseer repetidos ni estar desordenado, y debe tener mínimo 2 valores.")


print(arrayListOf(1, 3, 5))
print(arrayListOf(5, 3, 1))
print(arrayListOf(5, 1))
print(arrayListOf(-5, 1))
print(arrayListOf(1, 3, 3, 5))
print(arrayListOf(5, 7, 1))
print(arrayListOf(10, 7, 7, 1))
print(arrayListOf(1,3,6,7,8,10, 12, 17, 21))
