#settaggio conteggio
def countdown (n:int) -> None:
    #inizializzazione count down
    if n >= 0:
        while n:
            print(n)
            n = n-1
    #settagio caso errore
    else:
        print("numero negativo")

countdown(-5)

countdown(5)
