voti= int(input("inserire il voto: "))

match voti:
    case 106|107|108|109|110:
        print("il tuo GPA è 4.0")
    
    case  101|102|103|104|105:
        print("il tuo GPA è 3.7")

    case 96|97|98|99|100:
        print ("il tuo GPA è 3.3")
    
    case 91|92|93|94|95:
        print("il tuo GPA è 3.0")

    case 86|87|88|89|90:
        print("il tuo GPA è 2.7")

    case 81|82|83|84|85:
        print ("il tuo GPA è 2.3")

    case 76|77|78|79|80:
        print ("il tuo GPA è 2.0")

    case 70|71|72|73|74|75:
        print("il tuo GPA è 1.7")

    case 66|67|68|69:
        print("il tuo GPA è 1.0")

    case _:
        print("voto non valido")