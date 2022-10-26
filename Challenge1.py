
'''
DESAFIO N~01
 * ¿ES UN ANAGRAMA?
 * Dificultad: MEDIA

Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
NO hace falta comprobar que ambas palabras existan.
Dos palabras exactamente iguales no son anagrama.
    1) Imprime cada dato en una misma linea
    2) crea una lista con tres sub listas string_1 , string_2 y salida, e imprimela al final
nota:
    verifica las mayusculas/minusculas
    verifica las acentos
'''


    
matriz =[]
def isAnagram(wordOne, wordTwo):
    wordOne=wordOne.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    wordTwo=wordTwo.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    if (wordOne.lower() == wordTwo.lower()):
        salida = False
    elif (sorted(wordOne.lower()) == sorted(wordTwo.lower())):
        salida = True
    else:
        salida = False

    matriz.append([salida,wordOne, wordTwo])
    return salida
print(isAnagram("amor", "roma"))
print(isAnagram("pepe", "sopa"))
print(isAnagram("España","apañes"))
print(isAnagram("Enrique","quieren"))
print(isAnagram("Ballena","llenaba"))
print(isAnagram("Reposaré","Reposera"))
print (matriz)
'''
Alegan – Ángela                         Nepal – Panel                           Nacionalista – Altisonancia
Valora – Álvaro                         Raza – Zara                             Frase – Fresa
Colinas – Nicolás                       Pagar – Praga                           Integrarla – Inglaterra
Quieren – Enrique                       Cornisa – Narciso                       Acuerdo – Ecuador
Japonés – Esponja                       Amparo – Páramo                         Deudora – Eduardo
Ramón – Norma                           Camino – Mónica                         Fotolitografía – Litofotografía
Animal – Lámina                         Matar – Marta                           Saco – Cosa
Mora – Roma                             Brasil – Silbar                         Sentido – Destino
Saunas – Susana                         Croacia – Arcaico                       Tinieblas – Sibilante
Aretes – Teresa                         Andalucía – Alucinada                   Cronista – Cortinas
Ventilan – Valentín                     Aparcamiento – Metacarpiano             Calienta – Alicante
Trama – Marta                           Ballena – Llenaba                       Reposaré – Reposera
Cardiografía – Radiográfica             Conejo – Encojo                         Demostración –  Domesticaron
Desamparador – Desparramado             Polonia – Opalino                       Sopera – Sopear
Conservadora – Conversadora             Ardientemente – Retenidamente           Áspero – Espora
Irónicamente – Renacimiento             Riesgo – Sergio                         Aires – Aries
Escandalizar – Zascandilear             Agonista – Santiago                     Presa – Pesar
Enfriamiento – Refinamiento             Calor – Colar                           Esta – Ates
Romina – Marino                         Prisa – París                           Astringencia – Transigencia
Materialismo – Memorialista             Poder – Pedro                           Resto – Retos
Enérgicamente – genéricamente           Necrófila – Florencia                   Reías – Ríase
Presuposición – Superposición           Armonía – Mariano                       Terso – Teros
Enamoramientos – Armoniosamente         Salario – Rosalía                       Caracas – Cáscara
Rectificable – Certificable             Ovoide – Oviedo                         España – Apañes
Reconquistados – Conquistadores         Camelia – Micaela                       Alondra – Ladrona
Escabullimiento – Bulliciosamente       Enlodar – Leandro                       Conservación – Conversación
Electromagnético – Magnetoeléctrico     Delira – Lidera                         Derrocamiento – Recordamiento
Imponderable – imperdonable             Agranda – Granada                       Manila – Animal
Armonización – Romanización             Licúa – Lucía                           Ruanda – Anudar
Pronosticación – Contraposición         Amor – Roma                             Protesta – Portaste


'''
