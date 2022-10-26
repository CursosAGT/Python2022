
'''
DESAFIO N~'20
 * PARANDO EL TIEMPO
 * Dificultad: MEDIA
Enunciado: Crea una función que sume 2 números y retorne su resultado pasados unos segundos.
  - Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar en finalizar su ejecución.
  - Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona, es decir, sin detener la ejecución del programa principal. Se podría ejecutar varias veces al mismo tiempo.
'''
from time import sleep, perf_counter

def syncSum(numberOne, numberTwo, seconds):
    print(f'Iniciando sync, espere {seconds} segundos...')
    sleep(seconds)
    print(f'resultado = {numberOne+numberTwo} sleep {seconds}')


start_time = perf_counter()

syncSum(5, 2, 10)
syncSum(1, 3, 5)

end_time = perf_counter()

print(f'total de tiempo {end_time- start_time: 0.2f} segundo(s) en terminar.')
from time import sleep, perf_counter
from threading import Thread


def asyncSum(numberOne, numberTwo, seconds):
    print(f'Iniciando async, espere {seconds} segundos...')
    sleep(seconds)
    print(f'resultado = {numberOne+numberTwo} //  sleep {seconds}')

start_time = perf_counter()

# create two new threads
t1 = Thread(target=asyncSum, args=(5, 2, 10))
t2 = Thread(target=asyncSum, args=(1, 3, 5))

# start the threads
t1.start()
t2.start()

# wait for the threads to complete
t1.join()
t2.join()

end_time = perf_counter()

print(f'total de tiempo {end_time- start_time: 0.2f} //  segundo(s) en terminar.')
