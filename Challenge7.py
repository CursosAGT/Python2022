
'''
DESAFIO N~7
 * CONTANDO PALABRAS
 * Dificultad: MEDIA
Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
'''


def countWords(text) :

    word = {}
    lista = text.lower().split(" ")
    for palabra in lista:
        if palabra not in word.keys():# ver dic.get()
            word[palabra]=1
        else :
            word[palabra]+=1
    for palabra,cantidad in word.items():    
        print(f"la {palabra=} se ha repetido {cantidad} {'vez' if(cantidad == 1)  else 'veces'}")

countWords("Hola,Mundo este es un ejercicio en Python con strings")

