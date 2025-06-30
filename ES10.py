while True:
    lista = []
    somma = 0
    media_dispari = 0
    conteggio_pari = 0
    conteggio_dispari = 0

    for n in lista:
        n = int(input("inserisci i numeri, digita 0 per terminare: "))
        if n > 0:
            lista +=1
        else:
            for n in len(lista):
                if n %2 == 0:
                    conteggio_pari += 1
                    somma = sum(n for n in lista if n %2 == 0)
            
            for n in len(lista):
                if n%2 != 0:
                    somma+= n
                    conteggio_dispari +=1

