
'''
DESAFIO N~2
 * LA SUCESIÓN DE FIBONACCI
 * Dificultad: DIFÍCIL
Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
 * 0, 1, 1, 2, 3, 5, 8, 13...
 genera una lista de salida con los primeros 50 valores
'''

lista=[]
def fibonacci() :
    n0 = 0
    n1 = 1
    
    while len(lista)<50:
        print(n0)
        fib = n0 + n1
        n0 = n1
        n1 = fib
        lista.append(fib)
fibonacci()       
print(lista)
