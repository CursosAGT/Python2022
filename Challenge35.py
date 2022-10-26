
'''
DESAFIO N~'35
 * BATALLA POKÉMON
 * Dificultad: MEDIA
Enunciado: Crea un programa que calcule el daño de un ataque durante una batalla Pokémon.
  - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
  - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
  - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico (buscar su efectividad)
  - El programa recibe los siguientes parámetros:
  - Tipo del Pokémon atacante.
  - Tipo del Pokémon defensor.
  - Ataque: Entre 1 y 100.
  - Defensa: Entre 1 y 100.
'''



def PokemonType(name) :
    WATER=("Agua"),
    FIRE=("Fuego"),
    GRASS=("Planta"),
    ELECTRIC=("Eléctrico")


def battle(attacker, defender, attack, defense): 
    print("*"*50)

    if (attack <= 0 or attack > 100 or defense <= 0 or defense > 100) :
        print("El ataque o la defensa contiene un valor incorrecto")
        return "Error"
    typeChart = {
                    "WATER":    {"effective":"FIRE", "not_effective":"GRASS"},
                    "FIRE":     {"effective":"GRASS", "not_effective":"WATER"},
                    "GRASS":    {"effective":"WATER", "not_effective":"FIRE"},
                    "ELECTRIC": {"effective":"WATER","not_effective": "GRASS"}
                }
    effectivity = 1.0
    if (attacker == defender or typeChart[attacker]["not_effective"]  == defender) :
        effectivity = 0.5
        salida=f"resultado: No es muy efectivo"
    elif (typeChart[attacker]["effective"]  == defender) :
        effectivity = 2.0
        salida="resultado: Es súper efectivo"
    else :
        salida="resultado: Es neutro"
    salida+=f"\n{attacker=} \t puntos: {attack}\n{defender=} \t puntos: {defense} "
    salida+=f"\ndaño: {round(50 * attack / defense * effectivity,2)}"
    return salida

print(f'{battle("WATER", "FIRE",     attack= 50, defense= 30)} ')
print(f'{battle("WATER", "FIRE",     attack=101, defense=-10)} ')
print(f'{battle("FIRE" , "WATER",    attack= 50, defense= 30)} ')
print(f'{battle("FIRE" , "FIRE",     attack= 50, defense= 30)} ')
print(f'{battle("GRASS", "ELECTRIC", attack= 30, defense= 50)} ')
