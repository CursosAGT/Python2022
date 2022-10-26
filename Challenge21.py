
'''
DESAFIO N~'221
 * CALCULADORA .TXT
 * Fecha publicación enunciado: 23/05/22
 * Fecha publicación resolución: 01/06/22
 * Dificultad: MEDIA
 *
 * Enunciado: Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su resultado e imprímelo.
 * - El .txt se corresponde con las entradas de una calculadora.
 * - Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
 * - Soporta números enteros y decimales.
 * - Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
 * - El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
 * - Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.
'''
def calculate(filePath):
    try:
        filePath=filePath
        with open (filePath, 'r') as objtxt:
            objstr = objtxt.read()
            objstr=objstr.replace("\n","")
            print (f"formula= {objstr}\n{type(objstr)}")
            x=eval(objstr)
            return x
    except FileNotFoundError:
        print (f'"No se han enconra el archivo {filePath}')
    except Exception as e:
        print (f'"No se han podido resolver las operaciones" {e}')
print(f"el resultado es {calculate('Challenge21.txt')=}")
