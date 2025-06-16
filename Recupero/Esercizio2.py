'''
def ritorna_sequenza():
    numero = int(input("inserire il numero qui: "))
    sequenza = [3, 4, 5, 3, 6, 3, 7, 8, 5, 4, 1, 2 ,8]
    ripetizioni = sequenza.count(numero)#ripetizioni di quante volte numero appare
    risultato = sum(x for x in sequenza if x!=numero)#necessario per escludere tutti i numeri esclusi da "numeri" per la somma
    return ripetizioni, risultato
'''

def ritorna_sequenza():
    numero = int(input("inserire il numero: "))
    sequenza = [3, 4, 5, 3, 6, 3, 7, 8, 5, 4, 1, 2 ,8]
    ripetizioni = 0
    risultato = 0

    for x in sequenza:
        if x == numero:
            ripetizioni+=1
        else:
            risultato += x
    return ripetizioni, risultato
            