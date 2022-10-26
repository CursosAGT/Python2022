
'''
DESAFIO N~6
 * INVIRTIENDO CADENAS
 * Dificultad: FÁCIL
Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
'''



def reverse(text):
    reversedText = ""
    textCount=len(text)
    for index in range(0,textCount): 
        reversedText += text[(textCount -1) - index]
    return reversedText
print(reverse("Hola mundo"))
###############################################################################################
# Sin un bucle, mediante una función recursiva
def recursiveReverse(text, index = 0, reversedText= ""):
    textCount = len(text) - 1
    reversedText += text[textCount - index]
    if (index < textCount) :
        reversedText = recursiveReverse(text, index + 1, reversedText)
    return reversedText


print(recursiveReverse("Hola mundo"))
