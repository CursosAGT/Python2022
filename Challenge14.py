
'''
DESAFIO N~'14
 * ¿ES UN NÚMERO DE ARMSTRONG?
 * Dificultad: FÁCIL
Enunciado: Escribe una función que calcule si un número dado es un número de Amstrong (o también llamado narcisista).
  Un número narcisista es aquel que es igual a la suma de cada uno de sus dígitos elevados a la “n” potencia
   (donde “n” es el número de cifras del número). La metáfora de su nombre alude a lo mucho que parecen “quererse a sí mismos” estas cifras. 
   Por ejemplo, el 153 es un número narcisista puesto que 1**3 + 5**3 + 3**3 = 1 + 125 + 27 = 153. 
   Los primeros números narcisistas son: 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474 y 54748.
'''


def isArmstrong(number):
    if (number < 0) :
        salida= False
    else :
        str_num  = str(number)
        powValue = len(str_num)
        suma = 0
        for caracter in str_num:
            suma+=int(caracter)**powValue
        if suma==number:
            salida = True
        else:
            salida= False
    return salida    
for valor in [ 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20, 153, 370, 371, 407, 1634, 8208, 9474 , 54748]:
    print(f'{valor} isArmstrong   {isArmstrong(valor)=}')
# ~ print(f'{isArmstrong(371)=}')
# ~ print(f'{isArmstrong(-371)=}')
# ~ print(f'{isArmstrong(372)=}')
# ~ print(f'{isArmstrong(0)=}')
