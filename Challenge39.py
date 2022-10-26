'''
DESAFIO N~'39
 * TOP ALGORITMOS: QUICK SORT
 * Dificultad: MEDIA
 *
 * Enunciado: Implementa uno de los algoritmos de ordenación más famosos: el "Quick Sort",
 * creado por C.A.R. Hoare.
 * - Entender el funcionamiento de los algoritmos más utilizados de la historia nos ayuda a
 *   mejorar nuestro conocimiento sobre ingeniería de software. Dedícale tiempo a entenderlo,
 *   no únicamente a copiar su implementación.
 * - Esta es una nueva serie de retos llamada "TOP ALGORITMOS", donde trabajaremos y entenderemos
 *   los más famosos de la historia.
'''


def main(array_entrada):
    if len(array_entrada)==0:
        print("Array vacio")
        exit()
    else:
        return quicksort_(array_entrada, 0, len(array_entrada) - 1)


def quicksort_(array, first, last):
    i = first
    j = last
    pivot = (array[i] + array[j]) / 2
    while (i < j):
        while ( pivot > array[i] ):
            i += 1
        while ( pivot < array[j] ):
            j -= 1
        if (i <= j) :
            array[j] , array[i] =array[i] , array[j]
            i += 1
            j -= 1
    if first < j:
        array = quicksort_(array, first, j)
    if last > i:
        array = quicksort_(array, i, last)
    return array
array_entrada=[7,0, 5,2,6, 10,4,1, 8, 9, 3]
array_ordenado = main(array_entrada[:])# similar a .copy(hace una copia no un alias)
print(f"entrada =>{array_entrada}")
print(f"salida  =>{array_ordenado}")
for index,it in enumerate(array_ordenado):
    print(f"salida index=>{index}  dato=>{it}")
