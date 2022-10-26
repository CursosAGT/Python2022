
# ~ import subprocess, sys

# ~ p = subprocess.Popen(["powershell.exe", "D:\python_2022_2023___________________________________\P_0_____ej\Challenge42.py"], stdout=sys.stdout)
# ~ p.communicate()
# ~ import subprocess, sys

# ~ p = subprocess.Popen(["powershell.exe -file", 'D:\python_2022_2023___________________________________\P_0_____ej\Challenge42.py'], stdout=sys.stdout)

# ~ p.communicate()
# ~ exit()
'''
DESAFIO N~'43
 * TRUCO O TRATO
 * Dificultad: FÁCIL
 *
 * Enunciado: Este es un reto especial por Halloween.
 * Deberemos crear un programa al que le indiquemos si queremos realizar "Truco o Trato" y
 * un listado (array) de personas con las siguientes propiedades:
 * - Nombre de la niña o niño
 * - Edad
 * - Altura en centímetros
 *
 * Si las personas han pedido truco, el programa retornará sustos (aleatorios)
 * siguiendo estos criterios:
 * - Un susto por cada 2 letras del nombre por persona
 * - Dos sustos por cada edad que sea un número par
 * - Tres sustos por cada 100 cm de altura entre todas las personas
 * - Sustos: 🎃 👻 💀 🕷️🕸️ 🦇
 *
 * Si las personas han pedido trato, el programa retornará dulces (aleatorios)
 * siguiendo estos criterios:
 * - Un dulce por cada letra de nombre
 * - Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
 * - Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
 * - Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
'''
def truco_o_trato(tot,matriz):
    premios={   "Sustos":["🎃","👻","💀","🕷️","🕸️","🦇"],
                "Dulces":["🍰️","🍬️","🍡️","🍭️","🍪️","🍫️","🧁️","🍩"]}
    alturas = sum([alt for nom,edad, alt in matriz])*100
    if tot=="Truco":
        sustos= sum([int(len(nom)/2) for nom,edad, alt in matriz])
        sustos+= len([edad for nom,edad, alt in matriz if edad%2==0])*2
        sustos+= int(alturas/100)*3
        return f"{sustos=}  {random.choice(premios['Sustos'])}"
    elif tot=="Trato":
        dulce= sum([int(len(nom)) for nom,edad, alt in matriz])
        dulce+= sum([edad//3  if edad<=10 else 10 for nom,edad, alt in matriz])*2
        dulce+= int(alturas/100)*3
        return f"{dulce=}  {random.choice(premios['Dulces'])}"

import random
matriz=[
        ["Ana",7,1.10],
        ["Pepe",8,1.15],
        ["Luiz",9,1.20],
        ["Elena",10,1.25],
        ["Maria",11,1.30],
        ["Lucas",12,1.35],
        ["Hernana",13,1.40]
        ]
tot=["Trato","Truco"]
print(f'{truco_o_trato ("Trato",matriz)}')
print(f'{truco_o_trato ("Truco",matriz) }')
#https://unicode.org/emoji/charts/emoji-list.html
matriz2=list()
for i in matriz:
    matriz2.append([i[0],random.randint(5,15),random.uniform(1.0, 1.5)])
print(f'{truco_o_trato(random.choice(tot),matriz2 )}')
