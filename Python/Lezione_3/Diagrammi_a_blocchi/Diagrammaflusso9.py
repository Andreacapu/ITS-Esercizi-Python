nome = input("inserire nome venditore. ")

vendite = float(input("inserisci il numero di vendite: "))

max_vendite = vendite
min_vendite = vendite
min_nome = nome
max_nome = nome

for cont in range(20):
    new_nome = input("inserire nome: ")
    new_vendite = float(input("inserire numero vendite: "))

    if new_vendite > max_vendite:
        max_vendite = new_vendite

    if new_nome > max_nome:
        max_nome > new_nome

print(f"il venditore con più vendite è: {max_nome} con oltre {max_vendite} vednite")
print(f"il venditore con meno vendite è: {min_nome} con {min_vendite} vendite")