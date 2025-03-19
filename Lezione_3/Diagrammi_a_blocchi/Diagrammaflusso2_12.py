x = int(input("inserire un valore x: "))
y = int(input("inserire un valore y: "))

if x <= 0 and y <= 0:
    print("errore inserire valori positivi")

if x > 0 and y > 0:
    prodotto = x * y
    print(f"il prodotto di x e y è: {prodotto}")

if (x < 0 and y > 0) or (x > 0 and y < 0):
    risultato = x - y
    print(f"il risultato è: {risultato}")