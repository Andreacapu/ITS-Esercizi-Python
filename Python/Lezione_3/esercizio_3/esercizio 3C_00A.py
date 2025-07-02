#inserire lista neonati

neonati_nati = int(input("quanti neonati sfornati?"))
#controllo del match

match neonati_nati:

#impsostazione dei vari match
    case 1:
        print("Congratulazioni!")
    
    case 2:
        print("Doppia!")

    case 3:
        print("Tris!")

    case 4:
        print("Quadrupla!")

    case 5:
        print("Tombola!")


    case _:
        print("non è possibile!!!! n bambini")
