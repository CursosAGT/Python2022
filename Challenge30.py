
'''
DESAFIO N~'30
 * MARCO DE PALABRAS
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba un texto y muestre cada palabra en una línea, formando
 * un marco rectangular de asteriscos.
 * - ¿Qué te parece el reto? Se vería así:
 *   **********
 *   * ¿Qué   *
 *   * te     *
 *   * parece *
 *   * el     *
 *   * reto?  *
 *   **********
'''

def drawFrame(text):
    palabras = text.split(" ")
    maxLength =max(len(palabra) for palabra in palabras)
    lineas = len(palabras)
    # ~ print (lineas)
    # ~ print (maxLength)
    print ("*"*(maxLength+4))
    for palabra in palabras:
        if palabra=='': continue
        print (f"*",palabra.center(maxLength),"*")
    print ("*"*(maxLength+4))
    print ("^"*100)
drawFrame("¿Qué te parece el reto?")
drawFrame("¿Qué te     parece el reto?")
drawFrame("¿Cuántos retos de código de la comunidad has resuelto?")
drawFrame("Your loop doesn't compare the different article_type values against each other, so you're not getting the maximum.")
