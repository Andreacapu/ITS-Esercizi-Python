iterazione: int = 0
piumeno: int = 1
pi: float = 0.0
target: str = "3.14159"
denominatore = 1

while True:

    pi += piumeno * (4/denominatore)
    piumeno *= -1
    iterazione +=1
    denominatore += 2
    if str(pi)[:len(target)] == target:

        print(f"Per raggiungere {target} sono necessarie {iterazione} iterazioni!")
        break
    
    #print ("il valore prossimo a 3.1415 e' ",pi," raggiunto con ",iterazione," interazioni")