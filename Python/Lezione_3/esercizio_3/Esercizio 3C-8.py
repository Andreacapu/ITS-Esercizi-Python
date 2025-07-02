frase = input("frase: ")

#impstazione match statesment per impostare le variabili
match frase:
    case frase if frase.endswith ("?") and len (frase)%2 == 0: #statement con .endswith, len e stringa con numeri pari
        print("si")

    case frase if frase.endswith ("?") and len (frase)%2 != 0: #statement con .endswith, len e stringa con numeri dispari
        print("no")

    case frase if frase.endswith ("!"):
        print("wow!")

    case _:
        print(f"tu dici {frase}")