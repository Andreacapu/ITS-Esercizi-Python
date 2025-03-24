class Animal:
    def __init__(self, name:str, specie:str, habitat:str, zampe:int):
        self.name = name
        self.specie= specie
        self.habitat = habitat
        self.zampe = zampe

    def printInfo(self):
        print(f"{self.name}, {self.specie}, {self.habitat}, {self.zampe}")

    def setLegs(self, a:int):
        self.zampe = a

tigre= Animal("Tigre", "Mammifero", "Giungla", 3)
serpente= Animal("Serpente", "Rettile", "Terra", 1)
pinguino=Animal("Pinguino", "Volatile", "Artico", 3)


tigre.printInfo()
serpente.printInfo()
pinguino.printInfo()
tigre.setLegs(4)
serpente.setLegs(0)
pinguino.setLegs(2)
tigre.printInfo()
serpente.printInfo()
pinguino.printInfo()