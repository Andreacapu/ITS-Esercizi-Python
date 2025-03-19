#its bakery menu
#impostazione lista che funge da menù, con prezzi accanto ad ogni item
menù = {
        "pizza": 9.00,
        "pasta": 10.50,
        "zuppa": 7.00,
        "hamburger": 15.50,
        "cotoletta": 10.00,
        "salmone": 20.20,
        "patatine_fritte": 5.50,
       "patate_al_forno": 5.50,
        "verdura_del_giorno": 7.00,
        "cheesecake": 6.00,
        "tiramisù": 6.00,
        "focaccia_con_nutella": 6.00,
        "coca_cola": 3.50,
        "acqua": 1.50,
        "vino": 5.00,
    }
#seconda lista che funge da ordine (ricordarsi che le gaffe servono per l'elenco)
ordine = {
        "primo": "zuppa",
        "secondo": "cotoletta",
        "contorno": "patate_al_forno",
        "bevanda": "vino",
        "dolce": "cheesecake"
        }
      
#setting del conto mediante una indicizzazione con dizionari più i valori nei dizionari
conto = (
    menù[ordine["primo"]] +
    menù[ordine["secondo"]] +
    menù[ordine["contorno"]] +
    menù[ordine["bevanda"]] +
    menù[ordine["dolce"]]
    )
print (f"il totale è: {conto} grazie ed arrivederci")