import modulo

print("\nImportazione del modulo:")
modulo.favourite_book()  # Aggiunto le parentesi per chiamare la funzione

import Esercizio8_2
from Esercizio8_10 import send_messages
send_messages()
print("\nImportazione del modulo Esercizio8_2:")
Esercizio8_2()  # Corretto il typo nel nome della funzione

from modulo import Esercizio8_2 as fn

print("\nImportazione con 'from modulo import Esercizio8_2 as fn':")
fn()

import modulo as mn

print("\nImportazione con 'import modulo as mn':")
mn.Esercizio8_2()  # Chiamata corretta della funzione Esercizio8_2

from modulo import *

print("\nImportazione con 'from modulo import *':")
Esercizio8_2()