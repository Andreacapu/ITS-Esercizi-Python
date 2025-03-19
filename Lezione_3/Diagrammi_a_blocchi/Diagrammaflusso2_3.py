# Inizializzazione delle variabili
max_posti = 100  # Numero massimo di posti disponibili
iscritti = 0      # Numero di iscritti attuali

while True:
    # Mostra lo stato attuale dei posti
    print(f"\nPosti disponibili: {max_posti - iscritti}")
    print(f"Iscritti attuali: {iscritti}")

    # Richiedi l'input all'utente
    iscrizione = input("Prego digitare una opzione (iscrivi, annulla, elimina, esci): ").strip().lower()

    # Gestione delle opzioni
    if iscrizione == "iscrivi":
        if iscritti < max_posti:
            iscritti += 1
            print("Iscrizione confermata.")
        else:
            print("Spiacente, il corso è al completo.")

    elif iscrizione == "annulla":
        if iscritti > 0:
            iscritti -= 1
            print("Iscrizione annullata.")
        else:
            print("Nessuna iscrizione da annullare.")

    elif iscrizione == "elimina":
        if iscritti > 0:
            iscritti -= 1
            print("Disiscrizione completata.")
            risposta = input("Desideri iscriverti ad un altro corso? (sì/no): ").strip().lower()
            if risposta == "sì":
                if iscritti < max_posti:
                    iscritti += 1
                    print("Iscrizione al nuovo corso confermata.")
                else:
                    print("Spiacente, il corso è al completo.")
        else:
            print("Nessuna iscrizione da eliminare.")

    elif iscrizione == "esci":
        print("Buona giornata!")
        break

    else:
        print("Opzione non valida. Riprova.")
