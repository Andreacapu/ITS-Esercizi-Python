soglia = 70
nord_sud = int(input("Inserire numero macchine direzione NS: "))
est_ovest = int(input("Inserire numero macchine direzione EO: "))

# Logica di controllo
if nord_sud > soglia and est_ovest > soglia:
    time_ns = 50
    time_eo = 50
elif nord_sud > soglia:
    time_ns = 60
    time_eo = 40
elif est_ovest > soglia:
    time_ns = 40
    time_eo = 60
else:
    totale = nord_sud + est_ovest
    if totale == 0:  # Evita la divisione per zero
        time_ns = 50
        time_eo = 50
    else:
        time_ns = (nord_sud / totale) * 100
        time_eo = (est_ovest / totale) * 100

# Stampa dei risultati
print(f"Il tempo per il semaforo nord_sud è: {time_ns}")
print(f"Il tempo per il semaforo est_ovest è: {time_eo}")
soglia_veicoli = 70
nord_sud = int(input("Inserire il numero di veicoli in zona NS: "))
est_ovest = int(input("Inserire il numero di veicoli in zona EO: "))

soglia_ns = 50
soglia_eo = 50

if nord_sud > soglia_veicoli and est_ovest > soglia_veicoli:
    soglia_ns = 50
    soglia_eo = 50

if nord_sud > soglia_veicoli:
    soglia_ns = 60
    soglia_eo = 40

if est_ovest > soglia_veicoli:
    soglia_ns = 40
    soglia_eo = 60

if nord_sud < 0 and est_ovest < 0:
    total = nord_sud+ est_ovest
    if total!= 0:
        soglia_ns = (nord_sud / total) * 100
        soglia_eo = (est_ovest / total) * 100

    else:
        soglia_ns = 50
        soglia_eo = 50

print(f"il tempo dedicato al semaforo nord_sud è: {soglia_ns:.2f}%")
print(f"il tempo dedicato al semafor est_ovest è: {soglia_eo:.2f}%")
