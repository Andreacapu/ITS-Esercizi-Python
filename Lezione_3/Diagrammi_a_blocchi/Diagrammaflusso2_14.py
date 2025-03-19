punteggio = 0

# Funzione per validare l'input
def valida_input(valore):
    return valore > 0 and valore <= 6

# Input dei valori
D_1 = int(input("Inserire il valore di D1: "))
D_2 = int(input("Inserire il valore di D2: "))

# Controllo validità input
if not valida_input(D_1) or not valida_input(D_2):
    print("Errore: i valori devono essere compresi tra 1 e 6.")
else:
    sum = D_1 + D_2

    # Calcolo del punteggio
    if D_1 % 2 == 0 and D_2 % 2 == 0 and sum > 8:
        punteggio += 100

    if D_1 == 6 or D_2 == 6 or sum == 7:
        punteggio += 10

    # Determinazione del risultato
    if punteggio >= 100:
        print("Vittoria")
    else:
        print("Sconfitta")

    # Stampa del punteggio ottenuto
    print(f"Punteggio ottenuto: {punteggio}")