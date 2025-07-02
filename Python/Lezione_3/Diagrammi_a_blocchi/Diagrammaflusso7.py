
pari = 0
dispari = 0

for cont in range(10):
    n = int(input("inserisci un numero: "))
    if n%2 == 0:
        pari += 1
    else:
        dispari +=1

print(f"numeri pari inseriti: {pari}")
print(f"numeri dispari inseriti: {dispari}")

