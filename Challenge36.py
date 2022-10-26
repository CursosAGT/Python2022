
'''
DESAFIO N~'36
 * LOS ANILLOS DE PODER
 * Dificultad: MEDIA
 *
 * Enunciado: ¡La Tierra Media está en guerra! En ella lucharán razas leales a Sauron
 * contra otras bondadosas que no quieren que el mal reine sobre sus tierras.
 * Cada raza tiene asociado un "valor" entre 1 y 5:
 * - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3), Númenóreanos (4), Elfos (5)
 * - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2), Huargos (3), Trolls (5)
 * Crea un programa que calcule el resultado de la batalla entre los 2 tipos de ejércitos:
 * - El resultado puede ser que gane el bien, el mal, o exista un empate. Dependiendo de la
 *   suma del valor del ejército y el número de integrantes.
 * - Cada ejército puede estar compuesto por un número de integrantes variable de cada raza.
 * - Tienes total libertad para modelar los datos del ejercicio.
 * Ej: 1 Peloso pierde contra 1 Orco, 2 Pelosos empatan contra 1 Orco, 3 Pelosos ganan a 1 Orco.
'''

Kind={
        "HARFOOT":1,
        "SOUTHERNER":2,
        "DWARF":3,
        "NUMENOREAN":4,
        "ELF":5
        }


Evil= {
        "SOUTHERNER":2,
        "ORC":2,
        "GOBLIN":2,
        "WARG":3,
        "TROLL":5
        }

def battleForTheMiddleEarth(kindArmy, evilArmy) :
    print("*"*50)
    kindArmyPoints = 0
    evilArmyPoints = 0
    for army,quant in kindArmy:
        kindArmyPoints += Kind.get(army,0) * quant
    for army,quant in evilArmy:
        evilArmyPoints += Evil.get(army,0) * quant

    if (kindArmyPoints > evilArmyPoints):
        print(f"Gana el bien kind:{kindArmyPoints} evil:{evilArmyPoints}")
    elif (evilArmyPoints > kindArmyPoints) :
        print(f"Gana el mal kind:{kindArmyPoints} evil:{evilArmyPoints}")
    else :
        print(f"Empate kind:{kindArmyPoints} evil:{evilArmyPoints}")


battleForTheMiddleEarth(kindArmy=(("ELF", 1),),
                        evilArmy=(("TROLL", 1),)
                        )

battleForTheMiddleEarth(kindArmy=(("ELF", 1),("HARFOOT", 1)),
                        evilArmy=(("TROLL", 1),))

battleForTheMiddleEarth(kindArmy=(("ELF", 1),("HARFOOT", 1)),
                        evilArmy=(("TROLL", 1),("ORC", 1))
                        )

battleForTheMiddleEarth(kindArmy=(("ELF", 56),("HARFOOT", 80),("DWARF", 5)),
                        evilArmy=(("TROLL", 17),("ORC", 51),("WARG", 10),("SOUTHERNER", 2))
                        )

