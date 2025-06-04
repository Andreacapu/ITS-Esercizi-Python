def listino(prezzi:dict[str, int | float]) -> dict:
    nuova_lista: dict = {}

    for value in prezzi:
        if value <= 50:
            x = (value * 10) / 100
            x = round(x, 2)
            prezzi[value] = x
        else:
            continue

    return nuova_lista