x = int(input("Digitare un numero postivo: "))
sum = 0
if x > 0:
    for i in range(10):#impostazione ciclo for in range
        n = int(input("prego digitare un numero:  "))

        if x%2 == 0:
            if  n > x/2:
                sum = sum + n

        elif n < x:
            sum = sum + n
    print(f"il risultato è: {sum}")

else: 
    print("inserire un valore positivo")

