
'''
DESAFIO N~'15
CUÁNTOS DÍAS?
 * Dificultad: DIFÍCIL
Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
  - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
  - La función recibirá dos String y retornará un Int.
  - La diferencia en días será absoluta (no importa el orden de las fechas).
  - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
'''
from datetime import date, datetime
def printDaysBetween(firstDate, secondDate) :
    try :
        first_Date = datetime.strptime(firstDate, "%d/%m/%Y")
        second_Date = datetime.strptime(secondDate, "%d/%m/%Y")
        print(first_Date- second_Date)
    except Exception as e:
        print(f"Error en el formato de alguna fecha {e}")



printDaysBetween("18/05/2022", "29/05/2022")
printDaysBetween("1 de enero de 2022", "29/04/2022")
printDaysBetween("18/5/2022", "29/04/2022")
