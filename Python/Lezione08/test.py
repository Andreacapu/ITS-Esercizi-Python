from persona import Persona
from studente import Studente

p: Persona = Persona("Federico", "March", 29)

print (p)

studente1: Studente = Studente("Mario", "Rossi", 20, "0123456")

print(studente1)
#funzione isistance(obj, class) -< controlla sel'oggetto obj sia istanza della classe Class,
#se si -> True, se falso -> False

if isinstance(studente1, Studente):
    print("\nstudente 1 è istanza della classe Studente-")

if isinstance(studente1, Persona):
    print("\nstudente1 è un oggetto della classe Studente e della classe persona")

if isinstance(p, Persona):
    print("\np è un oggetto della classe Persona")
#controllare se oggetto p sia an che instanza della classe studente

if isinstance(p, Studente):
    print("\np è oggetto della classe Persona e studente")


#issubclass(Class1, Class2) -> controlla se Class1 è sottoclasse della classe Classe2
#in caso affermativo -> true, in caso negativo -> False
if issubclass(Studente, Persona):
    print("\nla classe Studente è sottoclasse di Persona45 0")