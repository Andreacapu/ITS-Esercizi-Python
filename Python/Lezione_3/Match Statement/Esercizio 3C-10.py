#inizializzazione inputo, con giorno e mese settati con un integer, e la data con l'output delle due variabili
giorno:int = int(input("inserire il giorno: "))
mese:int = int(input("inserire il mese: "))
data = (giorno, mese)

#inizializzazione match statement, usiamo quindi le precise date come punto di riferimento per il programma
match data:
    case(1, 1):
        print(f"il giorno {data} è capodanno")
    case(14, 2):
        print(f"il giorno {data} è san valentino")
    case(2, 6):
        print(f"il giorno {data} è la festa della repubblica")
    case(15, 8):
        print(f" il giorno {data} è ferragosto")
    case(31, 10):
        print(f"il giorno {data} è halloween")
    case(25, 12):
        print(f"il giorno {data} è natale")
    case _:
        print ("nessuna data rilevante")

