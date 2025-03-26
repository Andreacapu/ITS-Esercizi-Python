
lista_numeri = [5, 6, 7, 8, 9]
numeri_eliminati = [5, 6, 7]
res = []
for num in lista_numeri:
    if num not in numeri_eliminati:
        res.append(num)
    print(res)