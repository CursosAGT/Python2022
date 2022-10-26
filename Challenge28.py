
'''
DESAFIO N~'28
 * MÁQUINA EXPENDEDORA
 * Dificultad: MEDIA
 *
 * Enunciado: Simula el funcionamiento de una máquina expendedora creando una operación
 * que reciba dinero (array de monedas) y un número que indique la selección del producto.
 * - El programa retornará el nombre del producto y un array con el dinero de vuelta (con el menor
 *   número de monedas).
 * - Si el dinero es insuficiente o el número de producto no existe, deberá indicarse con un mensaje
 *   y retornar todas las monedas.
 * - Si no hay dinero de vuelta, el array se retornará vacío.
 * - Para que resulte más simple, trabajaremos en céntimos con monedas de 5, 10, 50, 100 y 200.
 * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
'''


enum class Money(val money: Int) {

    FIVE(5),
    TEN(10),
    FIFTY(50),
    ONEHUNDRED(100),
    TWOHUNDRED(200)

}

private fun buy(code: Int, money: Array<Money>): Pair<String, Array<Money>> {

    val products = mapOf<Int, Pair<String, Int>>(
        1 to Pair("Agua", 50),
        2 to Pair("Coca-Cola", 100),
        4 to Pair("Cerveza", 155),
        5 to Pair("Pizza", 200),
        10 to Pair("Donut", 75)
    )

    products[code]?.let { product ->

        var totalMoney = 0
        money.forEach { coin ->
            totalMoney += coin.money
        }

        if (totalMoney < product.second) {
            return Pair("El producto con código [${code}] tiene un coste ${product.second}. Has introducido ${totalMoney}.", money)
        }

        val pendingMoney = totalMoney - product.second

        return Pair(product.first, returnMoney(pendingMoney))
    }

    return Pair("El producto con código [${code}] no existe.", money)
}

private  fun returnMoney(pendingMoney: Int, money: Array<Money> = arrayOf()): Array<Money> {

    if (pendingMoney == 0) {
        return money
    }

    var newPendingMoney = pendingMoney
    val newMoney = money.toMutableList()

    for (coin in Money.values().reversed()) {
        if (coin.money <= pendingMoney) {
            newPendingMoney -= coin.money
            newMoney.add(coin)
            break
        }
    }

    return returnMoney(newPendingMoney, newMoney.toTypedArray())

print(buy(1, arrayOf(Money.FIVE, Money.FIVE, Money.TEN, Money.TEN, Money.TEN, Money.FIVE)))
print(buy(3, arrayOf(Money.FIVE, Money.FIVE, Money.TEN, Money.TEN, Money.TEN, Money.FIVE)))
print(buy(1, arrayOf(Money.FIVE, Money.FIVE, Money.TEN, Money.TEN, Money.TEN, Money.FIVE, Money.FIFTY)))
print(buy(5, arrayOf(Money.TWOHUNDRED)))
