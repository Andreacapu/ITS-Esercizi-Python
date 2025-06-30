def calcolo_pi_approssimazione(soglia):
    pi_approssimato = 0
    termini = 0
    denominatore = 1
    segno = 1

    while True:
        termine = segno * (4/denominatore)
        pi_approssimato += termine
        denominatore += 2
        segno *= 2

                # Verifica se l'approssimazione ha raggiunto la soglia desiderata
        if abs(pi_approssimato - 3.14159) < 0.000005:
            print(f"Per π ≈ 3.14159 servono {termini} termini")
            break
        elif abs(pi_approssimato - 3.1415) < 0.00005 and not has_reached_3_1415:
            print(f"Per π ≈ 3.1415 servono {termini} termini")
            has_reached_3_1415 = True
        elif abs(pi_approssimato - 3.141) < 0.0005 and not has_reached_3_141:
            print(f"Per π ≈ 3.141 servono {termini} termini")
            has_reached_3_141 = True
        elif abs(pi_approssimato - 3.14) < 0.005 and not has_reached_3_14:
            print(f"Per π ≈ 3.14 servono {termini} termini")
            has_reached_3_14 = True

# Chiamata alla funzione
calcola_pi_approssimazione()