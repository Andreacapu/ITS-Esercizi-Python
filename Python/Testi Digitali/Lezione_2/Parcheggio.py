def calculateCharges(hours):
    # Tariffa base: 2.00€ per le prime 3 ore o meno
    base_fee = 2.00
    
    # Tariffa extra: 0.50€ per ogni ora oltre le 3 ore
    extra_fee = 0.50
    
    # Numero massimo di ore coperte dalla tariffa base
    max_base_hours = 3
    
    # Tariffa massima giornaliera (24 ore)
    max_charge = 10.00
    
    # Se le ore di parcheggio sono <= 3, restituisci solo la tariffa base
    if hours <= max_base_hours:
        return base_fee
    else:
        # Calcola quante ore extra ci sono oltre le 3 ore base
        extra_hours = hours - max_base_hours
        
        # Calcola la tariffa totale: base + extra (0.50€ per ogni ora extra)
        charge = base_fee + (extra_fee * extra_hours)
        
        # Restituisce la tariffa calcolata, ma non più del massimo (10.00€)
        return min(charge, max_charge)
            