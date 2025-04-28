nome = str(input("digitare il nome: "))

genere = str(input("inserire il genere:m per Maschio o f per Femmina: "))

match genere:
    case "m":
        print(f"nome: {nome}, sesso: Maschio")
    case "f":
        print(f"nome: {nome}, sesso: Femmina")
    case _:
        print("Errore, digitare m o f")
