max_posti = 100
liberi = 0
while True:
    opzione = input("digitare l'opzione: ")
    match opzione:
        case "ingresso":
          if liberi > 0:
                liberi -= 1
                print("Posto prenotato. Posti liberi rimanenti:", liberi) 
          else:
                print("non ci sono posti liberi")
        case "uscita":
          if liberi < max_posti:
             liberi += 1
             print("posto liberato")
          else:
             print("nessun posto occupato")
        case "stato":
          liberi = max_posti-liberi
          print(f"i posti disponibili sono: {max_posti}")

        case "esci":
            break
        
        case _:
            print("inserire un opzione valida")


