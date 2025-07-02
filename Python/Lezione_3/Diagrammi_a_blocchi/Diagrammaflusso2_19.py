n = int(input("inserire qui il numero: "))#necessario per ricevere l'input dall'utente
if n < 0:#verifica se il valore inserito è postivo
    print("errore, serve un valore positivo")
else:#inizio calcolo
    if n%2 == 0:
        somma = 0
        for i in range(1, n+1):#ciclo for per tutti i numeri fino ad "n"
            if i%4 == 0:
                somma +=1
                print(f"la somma da 1 a {n}, divisibile per 4 è: {somma}")
    
    else:
        prodotto = 1
        for i in range(1, n+1, 2):#ciclo for per itinerare su tutti i numeri pari
            prodotto *=1
            print(f"Il prodotto dei numeri dispari da 1 a {n} è: {prodotto}")



