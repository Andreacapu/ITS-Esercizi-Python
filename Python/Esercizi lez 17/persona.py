class Persona:
    def __init__(self, first_name:str, last_name:str, age:int):
        if not isinstance(first_name,str):
            first_name = None
            print("Il nome deve essere una stringa")
        if not isinstance(last_name,str):
            last_name = None
            print("Il cognome deve essere una stringa")
        if isinstance(last_name,str) and isinstance(first_name,str):
            self.first_name = first_name
            self.last_name = last_name

    def setName(self, first_name:str):
        if not isinstance(first_name,str):
            first_name = None
            print("Il nome deve essere una stringa")
        else:
            self.first_name = first_name
    
    def setlastName(self, last_name:str):
        if not isinstance(last_name,str):
            self.last_name = None
            print("Il cognome deve essere una stringa")
        else:
            self.last_name = last_name
    def setAge(self, age:int):
        if not isinstance(age, int):
            self.age = None
            print ("L'età deve essere un numero")
        else:
            self.age = age
    
    def getName(self)-> str:
        return self.first_name
    def getLastname(self)-> str:
        return self.last_name
    def getAge(self)-> int:
        return self.age
    def greet(self):
        print (f"Ciao! sono {self.first_name} {self.last_name} e ho {self.age} anni!")
    
    