sequenza = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_precedente =  0

for i in sequenza:
    risultato = numero_precedente + i
    print("numero attuale", i, "numero precedente", numero_precedente, " somma: ", risultato)
    numero_precedente = i
    print(risultato)