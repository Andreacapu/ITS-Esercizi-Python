#dal file persona.py importa la classe Persona
#from persona import Persona

#ac:Persona = Persona("Andrea", "Capuani", 25)
#print (ac)
#print (ac.name, ac.lastname, ac.age)#corretto modo di printare

#sfrutto la funzione displayData per mostrare in output i relativi dati di una persona

#ac.displayData()

#dal file persona2.py importa il file Persona
from persona2 import Persona

ac:Persona = Persona()

ac.displayData()

#imposto il nome della persona ac:

ac.setName("Andrea")
ac.displayData()

#imposto il cognome della persona ac:

ac.setLastname("Capuani")
ac.displayData

#imposto età ac:
ac.setAge(25)
ac.displayData

print("-------------------")

ac.displayData()



print(ac.getName(), ac.getLastname(), ac.getAge())