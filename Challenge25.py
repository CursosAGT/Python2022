
'''
DESAFIO N~'25
 * PIEDRA, PAPEL, TIJERA
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S")=}'), ("S","R")=}'), ("P","S")=}')]. Resultado: "Player 2".
'''
def rockScissorsPaper(*games):
        print ("*"*100)
        matriz=[]
        jugador_1=0
        jugador_2=0
        if not isinstance(games[0],tuple):
            matriz.append(games)
        else:
            matriz=list(games)
        for game in  matriz: 
            playerOneMove,playerTwoMove = game
            for Jugada_1,Jugada_2 in (("ROCK","SCISSORS"),("PAPER","ROCK"),("SCISSORS","PAPER")): 
                if (playerOneMove == Jugada_1 and playerTwoMove == Jugada_2):
                    jugador_1+=1
                    break
                elif (playerTwoMove == Jugada_1 and playerOneMove == Jugada_2):
                    jugador_2+=1
                    break
        if (jugador_1 > jugador_2):
            salida= "ganador Jugador 1"
        elif (jugador_1 < jugador_2):
            salida= "ganador Jugador 2"
        else:
            salida= "tablas / sin ganador tablas"
        return salida
print(f'{rockScissorsPaper("ROCK", "ROCK")=}')
print(f'{rockScissorsPaper("ROCK", "PAPER")=}')
print(f'{rockScissorsPaper("ROCK", "SCISSORS")=}')
print(f'{rockScissorsPaper("PAPER","SCISSORS")=}')
print(f'{rockScissorsPaper(("ROCK", "ROCK"),("SCISSORS", "SCISSORS"),("PAPER", "PAPER"))=}')
print(f'{rockScissorsPaper(("ROCK", "SCISSORS"),("SCISSORS", "PAPER"),("SCISSORS", "ROCK"))=}')
print(f'{rockScissorsPaper(("ROCK", "PAPER"), ("SCISSORS", "ROCK"),("PAPER", "SCISSORS"))=}')
