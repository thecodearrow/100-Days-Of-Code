//https://codeforces.com/contest/1346/problem/A

fun main() {
    var t = readLine()!!.toInt();
    while(t!=0){
        t-=1;
        var arr= readLine()!!.split(" ").map { it.toInt() }
        var n=arr[0];
        var k=arr[1];
        var n1=n/(Math.pow(k.toDouble(),3.toDouble())+Math.pow(k.toDouble(),2.toDouble())+k+1);
        var n2=k*n1;
        var n3=k*n2;
        var n4=k*n3;
        print(n1.toInt())
        print(" ")
        print(n2.toInt())
        print(" ")
        print(n3.toInt())
        print(" ")
        print(n4.toInt())
        println()
    }
}