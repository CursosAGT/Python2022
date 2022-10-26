
'''
DESAFIO N~9
 * CÓDIGO MORSE
 * Dificultad: MEDIA
Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
'''



def decoder(String): 
    morse=""
    for caracter in String:
        if caracter in Dict_morse.keys():
            morse+=(f"{Dict_morse[caracter]} ")
        elif caracter == ' ':
            morse+=" "
    return morse
def encoder(morse):
    cadena = morse.split(" ") 
    print(f"{cadena=}")
    String=""
    for caracter in cadena:
        for Cos_est,Cod_morse in Dict_morse.items():
            if caracter=="":
                String+=(f" ")
                break
            elif caracter == Cod_morse:    
                String+=(f"{Cos_est}")
                break
    return String

Dict_morse = {"A" : ".—", "N" : "—.", "0" : "—————",
                "B" : "—...", "Ñ" : "——.——", "1" : ".————",
                "C" : "—.—.", "O" : "———", "2" : "..———",
                "CH" : "————", "P" : ".——.", "3" : "...——",
                "D" : "—..", "Q" : "——.—", "4" : "....—",
                "E" : ".", "R" : ".—.", "5" : ".....",
                "F" : "..—.", "S" : "...", "6" : "—....",
                "G" : "——.", "T" : "—", "7" : "——...",
                "H" : "....", "U" : "..—", "8" : "———..",
                "I" : "..", "V" : "...—", "9" : "————.",
                "J" : ".———", "W" : ".——", "." : ".—.—.—",
                "K" : "—.—", "X" : "—..—", "," : "——..——",
                "L" : ".—..", "Y" : "—.——", "?" : "..——..",
                "M" : "——", "Z" : "——..", "\"" : ".—..—.", "/" : "—..—."}

salida = input("ingrese un texto :").upper()

morse = decoder(salida)
print (f"{morse=}")
salida = encoder(morse)
print (f"{salida=}")
