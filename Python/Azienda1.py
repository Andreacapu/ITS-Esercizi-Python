from enum import Enum
import re

class TipiTelefono(Enum):
    cellulare = "cellulare"
    fisso = "fisso"

class Indirizzo:
    def __init__(self, via: str, cap: str, civ: str):
        if not isinstance(via, str) or not isinstance(cap, str) or not cap.isdigit():
            raise ValueError("Dati non corretti")
        self.via = via
        self.cap = cap
        self.civ = civ

    def get_via(self) -> str:
        return self.via
    
    def get_cap(self) -> str:
        return self.cap
    
    def get_civ(self) -> str:
        return self.civ
    def __hash__(self) ->int:
        return hash(self.via(), self.cap(), self.civ())
    def __eq__(self, other:any)-> bool:
        if other is None or \
            not isinstance(other, type(self)) or \
            hash(self) != hash(other)
            return False
        return(self.via(), self.civ(), self.cap()) == (other.via(), other.civ(), other.cap())
    
class Telefono:
    def __init__(self, telefono.str) -> None:
        if telefono != re('^\d{10}$'):
            raise TypeError("Numero non valido")
        self.telefono = telefono

    def get_telefono(self) -> str:
        return self.telefono
    
    def __hash__(self) -> int:
        return hash((self.telefono()))
    
    def __eq__(self, other:any) -> bool:
        if other is None or \
            not isinstance(other, type(self)) or \
            hash(self != hash(other)):
            return False
        return (self.telefono()) == (other.telefono())

class Stipendio:
    def __init__(self):
        pass
        
        