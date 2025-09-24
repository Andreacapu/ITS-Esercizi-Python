from film import Film
class Azione(Film):
    def __init__(self, id:int, title:str, genere:str, penale:float):
        super().__init__(id, title)
        if not isinstance(genere,str):
            genere = None
            print("La stringa non indica un genere riconosciuto")
        else: 
            self.genere = genere
        