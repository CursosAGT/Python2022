
'''
DESAFIO N~'19
 * CONVERSOR TIEMPO
 * Dificultad: FACIL
 *
 * Enunciado: Crea una función que reciba días, horas, minutos y segundos (como enteros) y retorne su resultado en milisegundos.
 sin usar datetime
'''


def timeToMillis(days, hours, minutes, seconds): 
    daysInMillis = days * 24 * 60 * 60 * 1000
    hoursInMillis = hours * 60 * 60 * 1000
    minutesInMillis = minutes*60 * 1000
    secondsToMillis = seconds * 1000
    return daysInMillis + hoursInMillis + minutesInMillis + secondsToMillis
    
def timeToMillis2(days, hours, minutes, seconds): 
    hours+= days * 24 
    minutes+= hours * 60 
    seconds+= minutes*60 
    secondsToMillis= seconds * 1000
    return secondsToMillis
    
print(f" en {timeToMillis(0, 0, 0, 10)=} milisegundos" )
print(f" en {timeToMillis(2, 5, -45, 10)=} milisegundos" )
print(f" en {timeToMillis(2000000000, 5, 45, 10)=} milisegundos" )
print ("*"*100)
print(f" en {timeToMillis2(0, 0, 0, 10)=} milisegundos" )
print(f" en {timeToMillis2(2, 5, -45, 10)=} milisegundos" )
print(f" en {timeToMillis2(2000000000, 5, 45, 10)=} milisegundos" )
