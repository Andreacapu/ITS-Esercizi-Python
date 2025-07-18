def inserimentoNomi():
    raccolta_nomi = []  # Usiamo una lista per mantenere l'ordine di inserimento
    
    while len(raccolta_nomi) < 30:  # Continua finché non raggiungiamo 30 nomi
        nome = input("Digita i nomi qua: ").strip()
        
        # Controllo stringa vuota
        if not nome:
            print("ERRORE, IMPOSSIBILE NON INSERIRE UN NOME")
            continue
            
        # Controllo lunghezza nome
        if len(nome) > 20:
            print("ERRORE: UN NOME NON PUÒ SUPERARE I 20 CARATTERI")
            continue
            
        # Controllo nome duplicato
        if nome in raccolta_nomi:
            print(f"Il nome '{nome}' è già stato inserito")
            break
            
        raccolta_nomi.append(nome)  # Aggiungi il nome alla lista
    
    # Stampa i risultati finali
    if raccolta_nomi:
        nome_lungo = max(raccolta_nomi, key=len)
        print(f"\nSono stati inseriti {len(raccolta_nomi)} nomi in totale!")
        print(f"Il nome più lungo è '{nome_lungo}' con {len(nome_lungo)} caratteri!")
    else:
        print("Nessun nome valido inserito.")

# Esegui la funzione
inserimentoNomi()