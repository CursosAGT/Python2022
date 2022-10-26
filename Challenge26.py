
'''
DESAFIO N~'26
 * CUADRADO Y TRIÁNGULO 2D
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 * - EXTRA: ¿Eres capaz de dibujar más figuras?
'''
def drawPolygon(size, fig_type) :
    if size < 2:
        print(f"El tamaño debe ser mayor a 1")
        return
    if (fig_type == "SQUARE") :
        print(f"* "*size)
        for _ in range (0,size-1):
            print(f"{'*'}{' '*((size*2)-3)}{'*'}")
        print(f"* "*size)
    elif (fig_type == "TRIANGLE"):
        print(f"*".center(int(size*2)+5))
        for i in range(0,size-2):
            linea=f"*{' '*(i*2+1)}*"
            print(linea.center(int(size*2)+5))
        fin="* "*(size)
        print(fin.center(int(size*2)+5))
    elif (fig_type == "DIAMOND"):
        size  *=2
        print(f"*".center(int(size*2)+5))
        for i in range(0,int((size-2)/2)):
            linea=f"*{' '*(i*2+1)}*"
            print(linea.center(int(size*2)+5))
        for i in range(int((size-2)/2),0,-1):
            linea=f"*{' '*(i*2+1)}*"
            print(linea.center(int(size*2)+5))
        print(f"*".center(int(size*2)+5))
drawPolygon(10,"SQUARE")
drawPolygon(15,"TRIANGLE")
drawPolygon(12,"DIAMOND")
