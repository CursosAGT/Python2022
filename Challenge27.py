
'''
DESAFIO N~'27
 * VECTORES ORTOGONALES
 * Dificultad: FÁCIL
 *
Enunciado: Crea un programa que determine si dos vectores son ortogonales.
 * - Los dos array deben tener la misma longitud.
 * - Cada vector se podría representar como un array. Ejemplo: [1, -2]
'''



def areOrthogonal(vectorOne, vectorTwo): 
    return ((vectorOne[0] * vectorTwo[0] + vectorOne[1] * vectorTwo[1])==0)

print(areOrthogonal((1, 2), (2, 1)))
print(areOrthogonal((2, 1), (-1, 2)))
