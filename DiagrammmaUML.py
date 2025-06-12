from enum import Enum
from typing import TypeVar
from datetime import datetime

RealGEZ = TypeVar('RealGEZ', bound=float)
date = TypeVar("date", bound = int)

class Impiegato:
    _nome: str
    _cognome: str
    _nascita: date  # immutabile
    _stipendio: RealGEZ

    def __init__(self, nome: str, cognome: str, nascita: date, stipendio:RealGEZ):
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)

    def set_nome(self, nome: str):
        self._nome = nome
        
    def get_nome(self, nome:str):
        return nome
    def set_cognome(self, cognome:str):
        self._cognome = cognome
    def get_cognome(self, cognome:str):
        return cognome

    def get_nascita(self, nascita:date):
        return nascita
    
    def set_stipendio(self, stipendio: RealGEZ):
        self._stipendio = stipendio


class Progetto:
    _nome:str
    _budget:float
    def __init__(self, nome: str, budget: float):
        self.nome = nome
        self.budget = budget
        self.impiegati_coinvolti: list[Impiegato] = []

    def aggiungi_impiegato(self, impiegato: str):
        self.impiegato = impiegato
    def give_impiegato(self, impiegato:str):
        return impiegato
    def set_budget(self, budget: float):
        self._budget = budget
    def give_budget(self, budget: float):
        return budget
    def get_impiegati_convolti(self, impiegato: str, impiegati: list[Impiegato]) -> None:
        if impiegato not in impiegati:
            return ValueError("Nome non trovato")
        else:
            

class Telefono:
    def __init__(self, numero:int):
        self.numero = numero
        self.rubrica = list[]


    def get_telefono(self, numero:int, rubrica = list):
        if numero not in


class Dipartimento:
    def __init__(self, nome: str, telefono:int):
        self.nome = nome
        self.impiegati: list[Impiegato] = []
        self.progetti: list[Progetto] = []
        self.telefono: list[]

    def assumi_impiegato(self, impiegato: Impiegato):
        self.impiegati.append(impiegato)

    def avvia_progetto(self, progetto: Progetto):
        self.progetti.append(progetto)


        