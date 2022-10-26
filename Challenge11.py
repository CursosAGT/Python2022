
'''
DESAFIO N~'11'
 * ELIMINANDO CARACTERES
 * Dificultad: FÁCIL
Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
  - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
  - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
'''



def findNonCommon(str1, str2):
    str1=str1.lower()
    str2=str2.lower()
    out1 = ""
    out2 = ""
    
    for caracter_str1 in str1 :
        if (caracter_str1 not in str2):
            out1 += caracter_str1
    for caracter_str2 in str2 :
        if (caracter_str2 not in str1):
            out2 += caracter_str2
    return out1,out2
    





str1="Ariel come pizza" 
str2="la Tetera esta caliente"
out1,out2=findNonCommon(str1, str2)

print(f"out1: {out1}")
print(f"out2: {out2}")
out1,out2=findNonCommon(str2, str1)
print(f"out1: {out1}")
print(f"out2: {out2}")
