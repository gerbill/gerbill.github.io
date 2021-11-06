# Kotlin
## Basics
```kotlin
fun main() {
    val n = 1
    
    if (n > 1) {
        println("[if statement] Value $n is greater than 1!")
    }
    
    when {
        n > 5 -> println("[when statement] Value $n is greater then 5!")
        n > 1 -> println("[when statement] Value $n is greater then 1!")
        else -> println("[when statement] Value $n is too small!")
    }
    
    for (i in 1..10) {
        print("$i ")
    }
    
    println("\n")
    
    for (i in 1 until 10) {
        print("$i ")
    }
    
    println("\n")
    
    for (i in 10 downTo 1 step 2) {
        print("$i ")
    }
}
```
