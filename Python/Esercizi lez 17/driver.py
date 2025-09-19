from persona import Persona
from dottore import Dottore
from paziente import Paziente
from fattura import Fattura

# Creazione dei dottori (impostando età valide > 30)
dottore1 = Dottore("Mario", "Rossi", "Cardiologo", 45)
dottore2 = Dottore("Luisa", "Bianchi", "Pediatra", 38)

# Presentazione dei dottori
dottore1.doctorGreet()
dottore2.doctorGreet()

# Creazione liste pazienti
lista_pazienti1 = [Paziente("Paziente1", "Cognome1", "COD1"), 
                   Paziente("Paziente2", "Cognome2", "COD2"),
                   Paziente("Paziente3", "Cognome3", "COD3")]

lista_pazienti2 = [Paziente("Paziente4", "Cognome4", "COD4")]

# Creazione fatture
fattura1 = Fattura(dottore1, lista_pazienti1)
fattura2 = Fattura(dottore2, lista_pazienti2)

# Stampa salari iniziali
print(f"Salario Dottore1: {dottore1.getSalary()} euro!")
print(f"Salario Dottore2: {dottore2.getSalary()} euro!")

# Spostamento paziente
paziente_da_spostare = lista_pazienti1.pop(0)  # rimuove primo paziente
lista_pazienti2.append(paziente_da_spostare)   # aggiunge al secondo dottore

# Stampa salari dopo modifica
print(f"Salario Dottore1: {dottore1.getSalary()} euro!")
print(f"Salario Dottore2: {dottore2.getSalary()} euro!")

# Guadagno totale
totale = dottore1.getSalary() + dottore2.getSalary()
print(f"In totale, l'ospedale ha incassato: {totale} euro!")