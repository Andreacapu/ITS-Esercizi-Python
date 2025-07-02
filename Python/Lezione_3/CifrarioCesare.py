from string import ascii_lowercase
def cifrario(frase: str, chiave: int)-> str:
    #stringa che contiene il risultato
    risultato: str= ""
    #codificazione codice carattere per carattere
    for carattere in frase:
        if carattere in ascii_lowercase:
            #ricerca indice corrispondete al  carratere corrispondente: carattere 0 ?= "a" = idx = 0
            #ascii_lowercase = ["a,b,c,d"]
            idx: int = ascii_lowercase.index[carattere]#ritorna la prima occorrenzadell'elemento passato
            idx += (idx + chiave) % len(ascii_lowercase)
            risultato += ascii_lowercase[idx]


    return risultato


