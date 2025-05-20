user = {"nome": input("inserire nome: "), "ruolo": input('inserire ruolo: '), "età": int(input("inserire età: "))}

match user:
    case user if user["età"] >= 18:
        print("Accesso completo a tutte le funzionalità")

    case user if user["età"] <= 18:
        print("Accesso limitato! Alcune funzionalità sono limitate")

    case user if user["ruolo"] == "admin":
        print("Accesso completo a tutte le funzionalità")

    case user if user["ruolo"] == "moderatore":
        print("Puoi gestire i contenuti ma non modificare le impostazioni")

    case user if user["ruolo"] == "utente":
        print("Accesso limitato! Alcune funzionalità sono limitate")

    case user if user["ruolo"] == "ospite":
        print("Accesso limitato! Alcune funzionalità sono limitate")

    case _:
        print ("Ruolo non riconosciuto, accesso negato")


