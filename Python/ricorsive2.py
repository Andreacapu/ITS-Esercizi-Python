def nomi():
    nomi = []

    while True:
        nome:str = str(input("digitare il nome:"))

        if len(nome) >= 20:
            print("Errore, il nome non può eccedere i 20 caratteri")
            continue
        if nome.lower() in [n.lower() for n in nome]:#list comprehansion
            break
        nomi.append(nome)

        if nomi:
            nome_lungo = max(nomi, key=len)
            print(f"il nome più lungo è {nome_lungo} con {len{nome_lungo}} caratteri")
            print("il totale di nomi inseriti sono:")
            for n in nomi:
                print(n)



