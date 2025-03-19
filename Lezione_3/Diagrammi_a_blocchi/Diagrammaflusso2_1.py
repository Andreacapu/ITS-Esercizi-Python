max_posti = 20  # Numero massimo di posti disponibili
liberi = max_posti  # Inizialmente tutti i posti sono liberi

while True:
    opzione = input("Inserire l'opzione: ").strip().lower()  # Rimuove spazi e converte in minuscolo

    match opzione:
        case "ingresso":
            if liberi > 0:
                liberi -= 1
                print("Posto occupato")
            else:
                print("Non ci sono posti disponibili")

        case "uscita":
            if liberi < max_posti:  # Verifica che ci siano posti occupati da liberare
                liberi += 1
                print("Posto liberato")
            else:
                print("Nessun posto occupato")

        case "stato":
            print(f"Posti liberi: {liberi}")
            occupati = max_posti - liberi
            print(f"Posti occupati: {occupati}")

        case "esci":
            print("Uscita dal programma.")
            break

        case _:
            print("Opzione non valida. Riprova.")
