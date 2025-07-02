from custom_types import *
from impiegato import Impiegato

class Progetto:
    _nome: str
    _budget: RealGEZ
    _impiegati: set[Impiegato]

    def __init__(self, nome: str, budget: RealGEZ):
        self.set_nome(nome)
        self.set_budget(budget)
        self._impiegati: set[Impiegato] = set()

    def set_nome(self, nome:str) -> None:
        self._nome = nome
    
    def set_budget(self, budget:RealGEZ) -> None:
        self._budget = budget

    def nome(self) -> str:
        return self._nome
    
    def budget(self) -> RealGEZ:
        return self._budget
    
    def add_impiegato(self, impiegato:Impiegato) -> None:
        # errore se l'impiegato era già coinvolto
        self._impiegati.add(impiegato)

    def remove_impiegato(self, impiegato:Impiegato) -> None:
        # errore se l'impiegato non era  coinvolto
        self._impiegati.remove(impiegato)


    def impiegati(self, impiegato:Impiegato) -> Impiegato:
        return Impiegato
    



if __name__ == "__main__":
    pegaso: Progetto = Progetto("Pegaso", RealGEZ(45000))