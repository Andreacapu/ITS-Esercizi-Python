class Persona:
    def __init__(self):
        self.name = ""
        self.lastname =  ""
        self.age = 0
      
    def displayData(self)-> None:
        print(f"Nome: {self.name}\nCognome {self.lastname}\nEtà: {self.age}")

    def setName(self, name:str) -> None:
        self.name = name


    def setLastname(self, lastname:str) -> None:
        self.lastname = lastname

    def setAge(self, age:int) -> None:
        self.age = age
        if age < 0 or age > 130:
            self.age = 0

    def getName(self):
        return self.name
    def getLastname(self):
        return self.lastname
    def getAge(self):
        return self.age