numero:int = int(input("inserire il numero: "))

if numero < 0:
    print("errore, inserire un numero positivo")

elif numero <= 1:
    print("il numero inserito non è un numero primo")

elif numero == 2:
    print("il numero inserito è un numero primo")