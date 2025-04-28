from persona import Persona
from alieno import Alieno

#creare un oggetto p della classe Persona

p: Persona = Persona("Andrea", "Capuani", 26)

#visualizzare le informazione dell' oggetto p

print(p)

#creare un oggetto et nella classe Alieno

et: Alieno = Alieno("Andromeda")

#visualizzare le informazione dell'oggetto et

print(et)

#l'oggetto p invochi il metodo speak()

p.speak()

et.speak()
