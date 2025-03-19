valori = []#lista valori vuota per la raccolta
cont = 0

for _ in range(10):
    n = int(input("digitare almeno 10 valori: "))
    if n <= 0:
        print("errore inserire numeri postivi")
        quit()

    valori.append(n)

N = int(input("Inserire un valore per la divisibilità: "))

for valore in valori:
    if valore%N == 0:
        cont += 1
    print(f"I numeri divisibili per {N} sono: {cont}")



