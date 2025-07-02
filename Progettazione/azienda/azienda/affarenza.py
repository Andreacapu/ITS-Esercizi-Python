from impiegato import Impiegato
from custom_types import *
from dipartimento import *
from progetto import Progetto
from typing import Set

class Afferenza:
    _data_afferenza: set[int]
    
    def __init__(self, data_afferenza: int):
        self.set_data(data_afferenza)

    def set_data(self, data: int) -> None:
        self._data_afferenza = data 
    
    def get_data(self) -> Set[int]:  
        return self._data_afferenza
    
    def add_data(self, data_afferenza:"Afferenza")-> None:
        self._data_afferenza.add(data_afferenza.get_data())

    def remove_data(self, data_afferenza:"Afferenza") -> None:
        self._data_afferenza.remove(data_afferenza.get_data())
