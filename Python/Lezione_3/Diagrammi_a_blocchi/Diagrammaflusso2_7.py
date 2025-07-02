cont = 0
sum = 0
while True:
    scelta = str(input("Desideri calcolare la media?: "))#inserito per dare l'input all'utente
    match scelta:
            case "si":
                    voto = float(input("Inersici un voto: "))#necessario affinchè dia scelta all'utente di continuare a inserire voti o fare la media
                
                    if voto > 0:
                        cont = cont +1
                        sum = sum + voto

                    else:
                        print("errore") 
            case "no":
                if cont > 0:
                    media = sum / cont
                    print(f"La media totale è: {media:.2f}")

            case _:
                print("Inserire una scelta valida ('si' o 'no').")