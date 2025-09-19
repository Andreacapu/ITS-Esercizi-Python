from persona import Persona

class Paziente(Persona):
    def __init__(self, first_name, last_name, age, IDcode:str):
        super().__init__(first_name, last_name, age)
        self.IDcode = IDcode

    def setIdCode(self, IDcode:str):
        if not isinstance(IDcode, str):
            self.IDcode = None
            print("ID non riconosciuto")
        else:
            self.IDcode = IDcode
    def getIdCode(self)-> str:
        return self.IDcode
    
    def patientInfo(self):
        base =super().greet
        return f"{base} | ID: {self.IDcode}"