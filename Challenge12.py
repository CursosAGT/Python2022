
'''
DESAFIO N~'12
 * ¿ES UN PALÍNDROMO?
 * Dificultad: MEDIA
 Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
'''

def isPalindrome(text):
    text=text.lower()
    text=text.replace(" ","").replace(".","").replace(",","").replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
    return text == text[::-1]
print(f'{isPalindrome("Neuquen")=}')
print(f'{isPalindrome("Ana lleva al oso la avellana.")=}')
print(f'{isPalindrome("Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, de pánico camina, ónice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nómina y ánimo de mortecina, ya ni giros elimina, ya ni poeta, ya ni vida")=}')
print(f'{isPalindrome("¿Qué os ha parecido el reto?")=}')
