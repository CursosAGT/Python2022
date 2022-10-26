'''
DESAFIO N~''40
 * TRIÁNGULO DE PASCAL
 * Dificultad: MEDIA
 *
 * Enunciado: Crea una función que sea capaz de dibujar el "Triángulo de Pascal" indicándole
 * únicamente el tamaño del lado.
 * - Aquí puedes ver rápidamente cómo se calcula el triángulo:
 *   https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif
'''



def pascalTriangle(size) :
    if size<2:
        print ("imposible")
        return
    print ("*".center(100))
    for row in range(2, size):
        print ("*".rjust(51-row)+"*".rjust((row-1)*2))
    print (("* "*size).center(100))


pascalTriangle(5)
pascalTriangle(1)
pascalTriangle(0)
pascalTriangle(-5)
pascalTriangle(10)
pascalTriangle(11)
pascalTriangle(12)
pascalTriangle(20)
