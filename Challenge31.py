
'''
DESAFIO N~'31
 * AÑOS BISIESTOS
 * Dificultad: FÁCIL
 
  Enunciado: Crea una función que imprima los 30 próximos años bisiestos siguientes a uno dado.
  - Utiliza el menor número de líneas para resolver el ejercicio.

'''

def thirtyLeapYears(year) :
    currentYear = year + 1
    yearCount = 0
    while (yearCount < 30) :
        if (currentYear % 4 == 0 and (currentYear % 100 != 0 or currentYear % 400 == 0)) :
            print(currentYear)
            yearCount+=1
        currentYear+=1

thirtyLeapYears(1999)
thirtyLeapYears(-500)
