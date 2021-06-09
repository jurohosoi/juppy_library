fun main(){
    val N: Int = readLine()!!.toInt()
    val (D: Int, X: Int) = readLine()!!.split(" ").map{ it.toInt() }

    var ans: Int = X
    for (i in 1..N){
        val A: Int = readLine()!!.toInt()
        ans += (D-1)/A + 1
    }

    println(ans)
}