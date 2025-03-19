lista_oggetti = []

n = 0

#settando il ciclo usando il while
while n <3:
    item = input("inserire  elemento: ")
    lista_oggetti.append(item)
    n = n+1 #settando il contatore così non va oltre i tre elementi

print(lista_oggetti)#in questo modo possiamo scrivere in output gli oggetti

match lista_oggetti:
    case ["penna", "matita", "quaderno"]:
        print("materiale scolastico")
   
    case ["pane", "latte", "uova"]:
        print("Prodotti alimentari")
    
    case ["sedia", "tavolo", "armadio"]:
        print("Mobili")

    case ["telefono", "computer", "tablet"]:
        print("Dispositivi elettronici")

    case _:
        print ("Categoria sconosciuta")