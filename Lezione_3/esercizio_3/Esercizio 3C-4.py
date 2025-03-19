

animale = input("dimmi l'animale: ")

match animale:
        case "cane" | "gatto"| "cavallo" | "elefante" |"leone":
            print(f"{animale} appartiene ai mamiferi")
    
        case "serpente" |"lucertola" | "tartaruga" | "coccodrillo":
            print(f"{animale} appartiene ai rettili")

        case "aquila" | "pappagallo" | "gufo" | "falco":
              print(f"{animale} appartiene agli uccelli")

        case "squalo" | "trota" | "salmone" | "carpa":
                print(f"{animale} appartiene ai pesci")

        case _:
                print(f"mi spiace, non posso identificare in quale categioria sia {animale}")
