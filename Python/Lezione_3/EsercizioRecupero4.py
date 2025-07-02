def numeri(lista:list[int]) -> int:
    thereshold:int = 10
    risultato = 1
    for i in lista:
        if i < thereshold:
            risultato *= i
    return risultato

    