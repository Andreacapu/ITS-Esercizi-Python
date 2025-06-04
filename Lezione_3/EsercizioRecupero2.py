def funzione(lista, dizionario):
    lista:list = []
    dizionario:dict = {}
    positivi:list = []
    negativi: list = []
    
    for i in lista:
        if i %2 == 0:
            positivi.append(i)
        else:
            negativi.append(i)

    """for key, value, key2, value2 in dizionario.items():
        dizionario(key)= "pari"
        dizionario(value)= pari
        dizionario(key2)= "dispari"
        dizionario(value2)= dispari"""
    
    dizionario["positivi"] = positivi
    

    
    return dizionario