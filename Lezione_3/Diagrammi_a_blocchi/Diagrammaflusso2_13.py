x = int(input("inserire il valore x: "))
y = int(input("inserire il valore y: "))
z = int(input("inserire il valore z: "))

while True:
    if x < 0 and y < 0 and z < 0:
        print("errore, inserire numeri positivi")

    elif (x+z+y == 0) and (x%2 == 0) and (y%5 == 0) and (z%7 == 0):
        print("regole rispettate")

    else:
        print("regole non rispettate")
