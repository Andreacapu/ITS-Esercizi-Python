def lista_tuple_dizionario(lista_tuple):
    dizionario = {}

    for chiave, valore in lista_tuple:
        if chiave in dizionario:
            dizionario[chiave] += valore
        else:
            dizionario[chiave] = valore
    return valore

