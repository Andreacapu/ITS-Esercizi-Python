#dal modulo persona.py importo la classe Persona
from persona import Persona

class Studente(Persona):

    def __init__(self, name:str, lastname:str, age:int, matricola: str):
        super().__init__(name, lastname, age)
        self.setMatricola(matricola)

    def setMatricola(self, matricola:str) -> None:
        if matricola:
            self.matricola = matricola
        else:
            print("/Erorre")
        
    def getMatricola(self)-> str:
        return self.matricola

    def __str__(self) -> str:
        return f"\nNome: {self.name}\nCognome: {self.getLastname()}\nMatricola{self.getMatricola()}"