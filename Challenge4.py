
'''
DESAFIO N~4
 * ÁREA DE UN POLÍGONO
 * Dificultad: FÁCIL
Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
'''



def area(funcion):

    def Triangle( base,  height):
        area= (base * height) / 2
        print(f"El área del triángulo es {area}")

    def Rectangle(length, width):
        area=length * width
        print(f"El área del rectángulo es {area}")

    def Square( side): 
        area= side * side
        print(f"El área del cuadrado es ${area}")
    return funcion()

area(Triangle(10.0, 5.0))
area(Rectangle(5.0, 7.0))
area(Square(4.0))
def function1(name):
    def function2():
        print('Hello ' + name)
    return function2

func = function1('Nicholas')
func()
