voti = int(input("Prego inserire i voti: "))

match voti:
    case 106|107|108|109|110:
        print("il tuo Gpa è 4.0")
    case 101|102|103|104|105:
        print ("il tuo GPA è 3.7")
    case 96|97|98|99|100:
        print("il tuo GPA è 3.0")
    case 