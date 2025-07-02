#inzializzazione contatori
dispari = 0
pari = 0
negativi = 0
positivi = 0

#acquisizioni numeri utente
for i in range(10):#ci serve per i numeri individiuali nella sequenza
    n = int(input(f"Inserire il numero {i+1}: "))#necessario affinchè nell'output si possano digitare effettivamente 10 numeri

    if n > 0:
        positivi +=1
    else:
        negativi+=1
    if n%2 == 0:
        pari +=1
    else:
        dispari+=1
          

print(f"pari: {pari}, dispari: {dispari}, positivi: {positivi}, negativi: {negativi}")