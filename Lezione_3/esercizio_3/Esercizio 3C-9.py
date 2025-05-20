#impostazione asse x e y (con int prima e int(input) dopo)
asse_x:int = int(input("inserire coordinata x: "))
asse_y:int = int(input("inserire coordinata y: "))
coordinata = (asse_x, asse_y)

#inizializzazione del match
match (asse_x, asse_y):
    case (0, 0):
        print(f"Il punto ({asse_x}, {asse_y}) si trova nell'origine.")

    case (x, y) if x > 0 and y > 0:#onde evitare problemi, inserisco una tupla, con x e y senza mettere l'asse
        print(f"il punto ({asse_x}, {asse_y}) si trova nel primo quadrante")#print del punto, usando questa volta le condizioni stabilite all'inizio

    case (x, y) if x < 0 and y > 0:
        print(f" il punto ({asse_x}, {asse_y}) si trova nel secondo quadrante")
    
    case (x, y) if x < 0 and y < 0:
        print (f"il punto ({asse_x}, {asse_y}) si trova nel terzo quadrante")

    case (x, y) if x > 0 and y < 0:
        print(f"il punto ({asse_x}, {asse_y}) si trova nel quarto quadrante")
    
    case (asse_x, 0):
        print("il punto ({asse_x}, {asse_y}) si trova nell' asse x")

    case (0, asse_y):
        print("il punto ({asse_x}, {asse_y}) si trova nell'asse y")

    case _:
        print("coordinate non trovate")