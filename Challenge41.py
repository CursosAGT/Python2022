'''
DESAFIO N~''41
 * LA LEY DE OHM
 * Fecha publicación enunciado: 10/10/22
 * Fecha publicación resolución: 17/10/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que calcule el valor del parámetro perdido correspondiente a la ley de Ohm.
 * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará el valor del tercero (redondeado a 2 decimales).
 * - Si los parámetros son incorrectos o insuficientes, la función retornará la cadena de texto "Invalid values".
'''



# V = R * I
def ohm(v = None, r = None, i = None) : 
    try:
        if (v != None and r != None and i == None) :
            salida= f"I = {round((v / r),2)}"
        elif (v != None and i != None and r == None) :
            salida= f"R = {round((v / i),2)}"
        elif (r != None and i != None and v == None) :
            salida= f"V = {round((r * i),2)}"
        else:
            raise 
    except:
        salida= "Invalid values"
    return salida
print(f'{ohm()}')
print(f'{ohm(v = 5.0)}')
print(f'{ohm(v = 5.0, r = 4.0)}')
print(f'{ohm(v = 5.0, i = 4.0)}')
print(f'{ohm(r = 5.0, i = 4.0)}')
print(f'{ohm(v = 5.125, r = 4.0)}')
print(f'{ohm(v = 5.0, i = 4.125)}')
print(f'{ohm(r = 5.0, i = 4.125)}')
print(f'{ohm(v = 5.0, r = 0.0)}')
print(f'{ohm(v = 5.0, i = 0.0)}')
print(f'{ohm(r = 5.0, i = 0.0)}')
print(f'{ohm(v = 5.0, r = 4.0, i = 3.0)}')
