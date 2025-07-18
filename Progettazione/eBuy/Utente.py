from custom_types import *
from datetime import datetime

class Utente:
    _username: str # immutabile, noto alla nascita
    _registrazione: datetime # immutabile, noto alla nascita

    def __init__(self, username: str, registrazione: datetime):
        self._username = username
        self._registrazione = registrazione
        
    def get_username(self)->str:
        return self._username
    
    def get_regisrazione(self)-> datetime:
        return self._registrazione
    

