from custom_types import *
from progetto import * 
from impiegato import Impiegato
from types import Any
from datetime import datetime
from dipartimento import *

class Coinvolto:
    def __init__(self, impiegato:Impiegato, diparitmento:Dipartimento, data_afferenza:datetime):
        self._impiegato: Impiegato = impiegato
        self._dipartimento:Dipartimento = diparitmento
        self._data_afferenza:datetime = data_afferenza

    def data_afferenza(self, data_afferenza:datetime)-> datetime:
        return data_afferenza
    def