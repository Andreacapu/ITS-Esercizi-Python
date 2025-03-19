def send_messages(messaggi, sent_messages):
    """
    Stampa ogni messaggio e lo sposta nella lista sent_messages.
    """
    while messaggi:
        messaggio_corrente = messaggi.pop()  # Rimuove l'ultimo messaggio dalla lista
        print(f"Sto inviando il messaggio: {messaggio_corrente}")
        sent_messages.append(messaggio_corrente)  # Aggiunge il messaggio alla lista sent_messages

# Lista dei messaggi da inviare
messaggi = [
    "richiamami asap",
    "ciao, sei libero stasera?",
    "mi raccomando, presente al colloquio domani",
    "Tim, servizio telefonico",
    "COngratulazioni, la sua posta è arrivata"
]

# Lista per memorizzare i messaggi inviati
sent_messages = []

# Chiamata alla funzione send_messages
send_messages(messaggi, sent_messages)

# Verifica delle liste
print("\nLista dei messaggi originali:", messaggi)
print("Lista dei messaggi inviati:", sent_messages)