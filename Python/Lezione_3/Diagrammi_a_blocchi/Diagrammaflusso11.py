liberi = 20  # Inizializza il numero di posti liberi

while True:
    opzione = input("Digitare l'opzione: ").strip().lower()  # Rimuove spazi bianchi e converte in minuscolo

    match opzione:
        case "prenota":
            if liberi > 0:
                liberi -= 1
                print("Posto prenotato")
            else:
                print("Posti tutti occupati")

        case "libera":
            if liberi < 20:  # Assicurati che non ci siano più posti liberi del totale
                liberi += 1
                print("Posto disdetto")
            else:
                print("Nessun posto occupato")

        case "visualizza":
            print(f"Liberi: {liberi}")
            occupati = 20 - liberi
            print(f"Occupati: {occupati}")

        case "esci":
            break

        case _:
            print("Opzione non valida. Riprova.")
