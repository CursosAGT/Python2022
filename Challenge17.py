
'''
DESAFIO N~'17
 * LA CARRERA DE OBSTÁCULOS
 * Dificultad: MEDIA
 *
 * Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no
 *        variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
'''





def checkRace(athlete, track) : 
    lista_salida = []
    if len(athlete)!= len(track):
        print("error en la cantidad ")
        lista_salida.append( False )
    else:
        for accion, pista in zip(athlete, track):
            print()
            # ~ print("J",accion.upper()=="JUMP" , pista=="|",'  >>>>>>>>> ',(accion.upper()=="JUMP" and pista=="|"))
            # ~ print("R",accion.upper()=="RUN" , pista=="_",'  >>>>>>>>> ',(accion.upper()=="RUN" and pista=="_"))
            if ((accion.upper()=="JUMP" and pista=="|") or\
                (accion.upper()=="RUN" and pista=="_")):
                lista_salida.append( True )
                print (f"  ok   > {accion.upper()} = {pista}", end=",")
            else:
                lista_salida.append( False )
                print (f" error > {accion.upper()} = {pista}", end=",")
        print()
    print(lista_salida)
    if all(lista_salida) is True:
        print("felicitaciones")
        track = True
    else:
        print("la proxima")
        track = False
    return track

athleta = ['RUN','JUMP','RUN','JUMP','RUN']
pista = "_|_|_"
print(checkRace(athleta,pista))
print("*"*50)
athleta = ['RUN','RUN','RUN','JUMP','RUN']
pista = "_|_|_"
print(checkRace(athleta,pista))
print("*"*50)
athleta = ['RUN','RUN','JUMP','JUMP','RUN']
pista = "_|_|_"
print(checkRace(athleta,pista))
print("*"*50)
athleta = ['RUN','RUN','JUMP','JUMP','RUN']
pista = "_|_|_|_"
print(checkRace(athleta,pista))
print("*"*50)
athleta = ['RUN','JUMP','RUN','JUMP']
pista = "_|_|_"
print(checkRace(athleta,pista))
print("*"*50)
athleta = ['RUN','JUMP','RUN','JUMP','RUN','JUMP','RUN']
pista = "_|_|_"
print(checkRace(athleta,pista))
print("*"*50)
athleta = ['JUMP','JUMP','JUMP','JUMP','JUMP']
pista = "|||||"
print(checkRace(athleta,pista))
print("*"*50)
athleta = ['JUMP','JUMP','JUMP','JUMP','JUMP']
pista = "||?||"
print(checkRace(athleta,pista))
print("*"*50)

