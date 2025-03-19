def recursiveSum(n: int) -> int:
    # Se n è negativo, stampa un messaggio di errore e restituisce None
    if n < 0:
        print("Error! Inserted number is negative!")
        return None
    
    # Caso base: se n è 0, la somma è 0
    elif n == 0:
        return 0
    
    # Caso ricorsivo: somma n con il risultato di recursiveSum(n-1)
    else:
        return n + recursiveSum(n - 1)

# Esempi di chiamata corretta
print(recursiveSum(-5))  # Output: Error! Inserted number is negative! None
print(recursiveSum(5))   # Output: 15 (1 + 2 + 3 + 4 + 5)