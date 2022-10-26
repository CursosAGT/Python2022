
'''
DESAFIO N~'37
 * LOS LANZAMIENTOS DE "THE LEGEND OF ZELDA"
 * Dificultad: MEDIA
 *
Enunciado: ¡Han anunciado un nuevo "The Legend of Zelda"! 
    Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023.
    Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos "The Legend of Zelda" de la historia?
    Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda que tú selecciones.
    Debes buscar cada uno de los títulos y su día de lanzamiento (si no encuentras el día exacto
    puedes usar el mes, o incluso inventártelo)
'''


ZeldaGame= {
            "THE_LEGEND_OF_ZELDA":"The Legend of Zelda",
            "THE_ADVENTURE_OF_LINK":"Zelda II: The Adventure of Link",
            "A_LINK_TO_THE_PAST":"The Legend of Zelda: A Link to the Past",
            "LINKS_AWAKENING":"The Legend of Zelda: Link's Awakening",
            "OCARINA_OF_TIME":"The Legend of Zelda: Ocarina of Time",
            "MAJORAS_MASK":"Zelda: Majora's Mask",
            "ORACLE_OF_SEASONS":"The Legend of Zelda: Oracle of Seasons",
            "ORACLE_OF_AGES":"The Legend of Zelda: Oracle of Ages",
            "FOUR_SWORDS":"The Legend of Zelda: Four Swords",
            "THE_WIND_WAKER":"The Legend of Zelda: The Wind Waker",
            "FOUR_SWORDS_ADVENTURES":"The Legend of Zelda: Four Swords Adventures",
            "THE_MINISH_CUP":"The Legend of Zelda: The Minish Cap",
            "TWILIGHT_PRINCES":"The Legend of Zelda: Twilight Princess",
            "PHANTHOM_HOURGLASS":"The Legend of Zelda: Phantom Hourglass",
            "SPIRIT_TRACKS":"The Legend of Zelda: Spirit Tracks",
            "SKYWARD_SWORD":"The Legend of Zelda: Skyward Sword",
            "A_LINK_BETWEEN_WORLDS":"The Legend of Zelda: A Link Between Worlds",
            "TRI_FORCE_HEROES":"The Legend of Zelda: Tri Force Heroes",
            "BREATH_OF_THE_WILD":"The Legend of Zelda:  Breath of the Wild",
            "TEARS_OF_THE_KINGDOM":"The Legend of Zelda: Tears of the Kingdom"} 

Z_date= {
            "THE_LEGEND_OF_ZELDA":"21/02/1986",
            "THE_ADVENTURE_OF_LINK":"14/01/1987",
            "A_LINK_TO_THE_PAST":"21/11/1991",
            "LINKS_AWAKENING":"06/06/1993",
            "OCARINA_OF_TIME":"21/11/1998",
            "MAJORAS_MASK":"27/04/2000",
            "ORACLE_OF_SEASONS":"27/02/2001",
            "ORACLE_OF_AGES":"27/02/2001",
            "FOUR_SWORDS":"03/12/2002",
            "THE_WIND_WAKER":"13/12/2002",
            "FOUR_SWORDS_ADVENTURES":"18/03/2004",
            "THE_MINISH_CUP":"04/11/2004",
            "TWILIGHT_PRINCES":"19/11/2006",
            "PHANTHOM_HOURGLASS":"23/06/2007",
            "SPIRIT_TRACKS":"07/12/2009",
            "SKYWARD_SWORD":"18/11/2011",
            "A_LINK_BETWEEN_WORLDS":"23/11/2013",
            "TRI_FORCE_HEROES":"11/10/2015",
            "BREATH_OF_THE_WILD":"03/03/2017",
            "TEARS_OF_THE_KINGDOM":"12/05/2023"
        }

from datetime import datetime, date, time, timedelta
def timeBetweenRelease(first,second):
    print("*"*50)
    if not(Z_date.get(first,False) or Z_date.get(second,False) ):
        return "Ingreso un juego no valido"
    elif (first==second) :
        return "Se está intentando comparar el mismo juego"
    else:
        fecha_first  = datetime.strptime( Z_date[first],"%d/%m/%Y")
        fecha_second = datetime.strptime( Z_date[second],"%d/%m/%Y")
        delta=abs(fecha_second-fecha_first)
        delta=delta.days
        years, days = divmod(delta, 365)
        return f"Entre la fecha de lanzamiento de {first} ({datetime.strftime(fecha_first,'%d/%m/%Y')})\n y {second} ({datetime.strftime(fecha_second,'%d/%m/%Y')}) hay {years} años y {days} días"
    return f"No se ha podido calcular el tiempo entre fechas de lanzamiento"

print(timeBetweenRelease("THE_LEGEND_OF_ZELDA","TEARS_OF_THE_KINGDOM"))
print(timeBetweenRelease("TEARS_OF_THE_KINGDOM","THE_LEGEND_OF_ZELDA"))
print(timeBetweenRelease("THE_LEGEND_OF_ZELDA","THE_ADVENTURE_OF_LINK"))
print(timeBetweenRelease("THE_ADVENTURE_OF_LINK","THE_LEGEND_OF_ZELDA"))
print(timeBetweenRelease("THE_LEGEND_OF_ZELDA","THE_LEGEND_OF_ZELDA"))
print(timeBetweenRelease("ORACLE_OF_SEASONS","ORACLE_OF_AGES"))

