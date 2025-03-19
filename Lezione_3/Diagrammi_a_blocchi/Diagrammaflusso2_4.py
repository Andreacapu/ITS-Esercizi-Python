tutor = 10
lista_attesa = 0

while True:
    opzione = input("Desideri un tutor assegnato?: ").strip().lower()

    match opzione:
        case "si":
            if tutor > 0:
                tutor -= 1
                lista_attesa += 1
                print("Tutor assegnato")
            else:
                print("Nessun tutor disponibile")

            # Condizione per terminare il ciclo
            if tutor == 0 and lista_attesa == 50:
                print("Lista d'attesa piena e nessun tutor disponibile.")
                break

        case "no":
            print("Programma terminato.")
            break

        case _:
            print("Inserire un'opzione valida ('si' o 'no').")