while True:
    num = int(input("Digitare un numero positivo: ")) 

    if num < 0:
        print("Errore, digitare un numero positivo.")  
    else:
        sum = 0 
        i = 4    

        while i <= num:  # Continua finché i è minore o uguale a num
            sum += i * i 
            i += 1        

        print(f"Il risultato per il numero inserito è: {sum}")  
        break  