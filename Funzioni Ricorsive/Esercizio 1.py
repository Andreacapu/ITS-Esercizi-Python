def recursivepower(base, exponent):#inizializzazione funzione per le potenze
    if exponent == 0:#condizione del ciclo affinche possa terminare e non andare in loop
        return 1
    else:
        return base*recursivepower(base, exponent-1)

 #print gli esponenti   
print(recursivepower(3,4))
print(recursivepower(4,3))
print(recursivepower(2,5))
print(recursivepower(5,2))
