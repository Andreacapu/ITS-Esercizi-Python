while True:
    a = int(input("digitare il valore a: "))
    b = int(input("digitare il valore b: "))
    if a < 0 or b < 0:
        print("Errore, i valori devono essere positivi")

    elif a >= b:
        print("errore, A deve essere minore di B")

    else:
        somma = 0
        for numero in range (a, b + 1):
            somma += numero
            print(f"il risultato di {a} e {b} è: {somma}")