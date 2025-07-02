n = None

for cont in range(7):
    soglia = int(input("Inserire il numero: "))
    if n is None or soglia > n:
        n = soglia

print(f"Il numero maggiore è: {n}")
