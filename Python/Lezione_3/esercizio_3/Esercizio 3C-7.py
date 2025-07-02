#impostazione contatori per ciclo e per testa e croce
contatore  = 1

testa = 0

croce = 0

#impostazione del range per assicurarci che faccia esattamente 8 lanci
for i in range (8):
    risultato:str = input("lancia ma moneta, T per testa, C per croce: ")

#impostazione del match per il risultato
    match risultato:
        case risultato if risultato == "C" or risultato == "c":
            croce += 1
            contatore += 1

        case risultato if risultato == "T" or risultato == "t":
            testa += 1
            contatore += 1

        case _:
            print ("per favore inserire testa o croce. ")

#impostazione per calcolare la percentuale
    percentuale_testa:float = (testa/contatore)*100
    percentuale_testa:float = (round(percentuale_testa, 2))
    print(f" la percentuale testa è: {percentuale_testa}%")

    percentuale_croce:float = (croce/contatore)*100
    percentuale_croce:float = (round(percentuale_croce, 2))
    print(f"la percentuale croce è: {percentuale_croce}%")