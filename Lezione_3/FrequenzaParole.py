import string

def frequenza_parole(testo:str) -> dict[str, int]:
    traduttore = str.maketrans('', "", string.punctuation)

    parole:dict [dict, str] = {}
    tokens = testo.split()

    for token in tokens:
        parola = token.lower().translate(traduttore).strip()

        if parola:
            parole[parola]= parole.get(parola, 0) +1
    
    return parole

testo = "Hello world, Hello Andrea"
print(frequenza_parole(testo))