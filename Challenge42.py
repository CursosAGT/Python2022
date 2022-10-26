'''
DESAFIO N~'42
 * CONVERSOR DE TEMPERATURA
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que transforme grados Celsius en Fahrenheit y viceversa.
 * - Para que un dato de entrada sea correcto debe poseer un símbolo "°" y su unidad ("C" o "F").
 * - En caso contrario retornará un error.

'''

exit()

def temperatureConverter(degrees):
    try :
        if "°C" in degrees.upper():
            degrees=degrees.upper().replace(" ","").replace("°C","")
            degrees=eval(degrees)
            salida= f"{round((degrees * 9/5) + 32,2)}°F"

        elif "°F" in degrees.upper():
            degrees=degrees.upper().replace(" ","").replace("°F","")
            degrees=eval(degrees)
            salida= f"{round((degrees - 32) * 5/9,2)}°C"
        else:
            raise
    except:
        salida="Error en los datos"       
    return salida


print(f'{temperatureConverter("100°C")}')
print(f'{temperatureConverter("100°F")}')
print(f'{temperatureConverter("100C")}')
print(f'{temperatureConverter("100F")}')
print(f'{temperatureConverter("100")}')
print(f'{temperatureConverter("100")}')
print(f'{temperatureConverter("- 100 °C ")}')
print(f'{temperatureConverter("- 100 °F ")}')
print(f'{temperatureConverter("100A°C")}')
print(f'{temperatureConverter("100A°F")}')
print(f'{temperatureConverter("°C")}')
print(f'{temperatureConverter("°F")}')
