#rraccolta imput di quanti numeri l'utente vuole inserire
lista_num = int(input("inserire qui i seguenti numeri: "))
#settaggio parametri
numeri = []
somma = 0
somma_pari = 0
somma_dispari = 0

#analisi numeri
for n in range(lista_num):
    n = int(input("digitare un numero prego: "))
    numeri.append(n)
    somma +=n

media = somma/lista_num

for n in numeri:
    if n%2 == 0 and n > media:
        somma_pari+=n
    elif n%2 !=0:
        somma_dispari+=n

print(f"\nSomma totale: {somma}")#stampa dei risultati
print(f"Media: {media}")
print(f"Somma dei numeri pari maggiori della media: {somma_pari}")
print(f"Somma dei numeri dispari: {somma_dispari}")
    
if somma_pari > somma_dispari:
    print("somma pari è maggiore")
elif somma_dispari > somma_pari:
    print("somma dispari è maggiore")
else:
    print("entrambe le somme sono eque")


