fun min(x: Int, y: Int): Int = if (x <= y) x else y


fun main(){
    val A: Int = readLine()!!.toInt()
    val B: Int = readLine()!!.toInt()
    val C: Int = readLine()!!.toInt()
    val D: Int = readLine()!!.toInt()

    var ans: Int = 0
    ans += min(A, B) + min(C, D)
    println(ans)
}