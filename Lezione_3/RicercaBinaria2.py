def bin_search(lista:list) -> None:

    mid: int = len(lista) // 2
    if lista[mid] == num:
        print(f"Numero trovato in posizione {mid}")
    elif len(lista) == 1:
        print("numero non trovato")
    elif lista[mid] > num:
        bin_search(lista[:mid],num)
    elif lista[mid]< num:
        bin_search(lista[mid + 1:],num)