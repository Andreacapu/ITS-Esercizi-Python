sequenza:int = int(input("digitare un numero intero: "))

somma = 0

cont = 1

for sequenza in range (4):
    n = int(input("digitare un numero: "))
    if n > 0:
        somma = somma + n
        cont = cont + 1
    elif n < 0:
        cont = cont + 1

    print(f"il risultato è {somma}")