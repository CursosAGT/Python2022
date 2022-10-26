
'''
DESAFIO N~'18
 * TRES EN RAYA
 * Fecha publicación enunciado: 02/05/22
 * Fecha publicación resolución: 09/05/22
 * Dificultad: DIFÍCIL
 *
 Enunciado: Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
  - "X" si han ganado las "X"
  - "O" si han ganado los "O"
  - "Empate" si ha habido un empate
  - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
 Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.
'''

fun main() {

    println(checkTicTacToe(arrayOf(
        arrayOf(TicTacToeValue.X, TicTacToeValue.O, TicTacToeValue.X),
        arrayOf(TicTacToeValue.O, TicTacToeValue.X, TicTacToeValue.O),
        arrayOf(TicTacToeValue.O, TicTacToeValue.O, TicTacToeValue.X))))

    println(checkTicTacToe(arrayOf(
        arrayOf(TicTacToeValue.EMPTY, TicTacToeValue.O, TicTacToeValue.X),
        arrayOf(TicTacToeValue.EMPTY, TicTacToeValue.X, TicTacToeValue.O),
        arrayOf(TicTacToeValue.EMPTY, TicTacToeValue.O, TicTacToeValue.X))))

    println(checkTicTacToe(arrayOf(
        arrayOf(TicTacToeValue.O, TicTacToeValue.O, TicTacToeValue.O),
        arrayOf(TicTacToeValue.O, TicTacToeValue.X, TicTacToeValue.X),
        arrayOf(TicTacToeValue.O, TicTacToeValue.X, TicTacToeValue.X))))

    println(checkTicTacToe(arrayOf(
        arrayOf(TicTacToeValue.X, TicTacToeValue.O, TicTacToeValue.X),
        arrayOf(TicTacToeValue.X, TicTacToeValue.X, TicTacToeValue.O),
        arrayOf(TicTacToeValue.X, TicTacToeValue.X, TicTacToeValue.X))))
}

private enum class TicTacToeValue {
    X, O, EMPTY
}

private enum class TicTacToeResult {
    X, O, DRAW, NULL
}

private fun checkTicTacToe(board: Array<Array<TicTacToeValue>>): TicTacToeResult {

    // Null

    if (board.count() != 3) {
        return TicTacToeResult.NULL
    }

    var xCount = 0
    var oCount = 0

    var flatBoard: Array<TicTacToeValue> = emptyArray()
    for (row in board) {
        flatBoard += row

        if (row.count() != 3) {
            return TicTacToeResult.NULL
        }

        for (col in row) {
            if (col == TicTacToeValue.X) {
                xCount += 1
            } else if (col == TicTacToeValue.O) {
                oCount += 1
            }
        }
    }

    if ((xCount - oCount).absoluteValue > 1) {
        return TicTacToeResult.NULL
    }

    // Win or Draw

    val winCombinations = arrayOf(
        arrayOf(0, 1, 2), arrayOf(3, 4, 5), arrayOf(6, 7, 8), arrayOf(0, 3, 6),
        arrayOf(1, 4, 7), arrayOf(2, 5, 8), arrayOf(0, 4, 8), arrayOf(2, 4, 6))

    var result = TicTacToeResult.DRAW

    for (winCombination in winCombinations) {

        if (flatBoard[winCombination[0]] != TicTacToeValue.EMPTY
                && flatBoard[winCombination[0]] == flatBoard[winCombination[1]]
                && flatBoard[winCombination[0]] == flatBoard[winCombination[2]]) {

            val winner = flatBoard[winCombination[0]]

            if (result != TicTacToeResult.DRAW
                    && (if (result == TicTacToeResult.O) TicTacToeValue.O else TicTacToeValue.X) != winner) {
                return TicTacToeResult.NULL
            }

            result = if (winner == TicTacToeValue.X) TicTacToeResult.X else TicTacToeResult.O
        }
    }

    return result
}
print("*"*50)

