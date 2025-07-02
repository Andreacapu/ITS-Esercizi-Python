def parentesi_bilanciate(s: str) -> bool:
    contatore = 0
    for carattere in s:
        if carattere == '(':
            contatore += 1
        elif carattere == ')':
            contatore -= 1
            if contatore < 0:
                return False
    return contatore == 0  