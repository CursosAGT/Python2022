
'''
DESAFIO N~5
 * ASPECT RATIO DE UNA IMAGEN
 * Dificultad: DIFÍCIL
Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.

  - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
  - Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.


'''
fun aspectRatio(url: String) {


    aspectRationStr: String? = null

    url = URL(url)
    bitmap = BitmapFactory.decodeStream(url.openStream())

    height = bitmap.height
    width = bitmap.width
    aspectRatio = rationalAspectRatio(height.toDouble() / width.toDouble())
    aspectRationStr = "${aspectRatio.second}:${aspectRatio.first}"

    aspectRationStr?.let { ratio ->
        print("El aspect ratio es ${ratio}")
    } ?: run {
        print("No se ha podido calcular el aspect ratio")


data class Quadruple(val h1: Int, val k1: Int, val h: Int, val k: Int)

private fun rationalAspectRatio(aspectRatio: Double): Pair<Int, Int> {
    val precision = 1.0E-6
    var x = aspectRatio
    var a = x.roundToInt()
    var q = Quadruple(1, 0, a, 1)

    while (x - a > precision * q.k.toDouble() * q.k.toDouble()) {
        x = 1.0 / (x - a)
        a = x.roundToInt()
        q = Quadruple(q.h, q.k, q.h1 + a * q.h, q.k1 + a * q.k)
    }
    return Pair(q.h, q.k)
}
