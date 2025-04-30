oggetti = []
n = 0
while n < 3:
    item = input("inserire gli oggetti: ")
    oggetti.append(item)
    n = n+1
    print(oggetti)

match oggetti:
    case ["penna", "matita", "quaderno"] :
        print("Materiale didattico")
    case ["pane", "latte", "uova"] :
        print("Alimentari")
    case ["sedia", "tavolo", "armadio"]:
        print("Arredo")
    case _:
        print("Errore, lista non identificata")
