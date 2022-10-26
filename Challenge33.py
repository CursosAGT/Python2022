
'''
DESAFIO N~'33
 * CICLO SEXAGENARIO CHINO
 * Dificultad: MEDIA
 *
Enunciado: Crea un función, que dado un año, indique el elemento y animal correspondiente
en el ciclo sexagenario del zodíaco chino.
 - Información: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
 - El ciclo sexagenario se corresponde con la combinación de 
 elementos:      madera, fuego, tierra, metal, agua y 
 animales:       rata, buey, tigre, conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo (en este orden).
 - Cada elemento se repite dos años seguidos.
 - El último ciclo sexagenario comenzó en 1984 (Madera Rata).
'''



def chineseZodiac(year) :
    elements = ("madera", "fuego", "tierra", "metal", "agua")
    animals = ("rata", "buey", "tigre", "conejo", "dragón", "serpiente", "caballo", "oveja", "mono", "gallo", "perro", "cerdo")

    if (year < 604) :
        return "El ciclo sexagenario comenzó en el año 604."
    sexagenaryYear = (year - 4) % 60
    element = elements[int((sexagenaryYear % 10) / 2)]
    animal = animals[sexagenaryYear % 12]
    return f"{year}: {element} {animal}"

print(chineseZodiac(1924))
print(chineseZodiac(1946))
print(chineseZodiac(1984))
print(chineseZodiac(604))
print(chineseZodiac(603))
print(chineseZodiac(1987))
print(chineseZodiac(2020))
print(chineseZodiac(2022))
