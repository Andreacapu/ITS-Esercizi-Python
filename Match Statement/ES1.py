'''
Esercizio 3C-00A. Scrivere un programma in Python che richieda all'utente di inserire un numero intero rappresentante il numero di neonati e utilizzi lo statement match per fornire una risposta appropriata:

- Se il numero inserito è 1, stampare "Congratulazioni!"
- Se il numero inserito è 2, stampare "Wow! Gemelli!"
- Se il numero inserito è 3, stampare "Wow! Tre!"
- Se il numero inserito è 4, stampare "Mamma mia Quattro! Wow!"
- Se il numero inserito è 5, stampare "Incredibile! Cinque!"
- Altrimenti, stampare "Non ci credo! n bambini!", sostituendo n con il numero inserito.
'''

neonati_nati = int(input("quanti sono i bambini?"))

match neonati_nati:
    case 1:
        print("Congratulazioni!")
    case 2:
        print("Wow, doppi!")
    case 3:
        print("Diamine, tripletta!")
    case 4:
        print("Quadrupla, wow!")
    case 5:
        print("Assurdo! Cinque!")
    case 6:
        print("Per Dio! Tombola!")
    case _:
        print(f"Immossibile {neonati_nati} bambini!")