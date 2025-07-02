voto = int(input("inserire il voto: "))

match voto:
    case 10:
        print("eccellente")

    case 8|9:
        print("molto buono")
    
    case 6|7:
        print("sufficente")

    case 4|5:
        print("insufficente")

    case 1|3:
        print("gravemente insufficente")

    case _:
        print("voto non valido")