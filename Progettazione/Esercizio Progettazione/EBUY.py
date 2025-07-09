from types.numbers import (
    realGEZ,
    intGEZ
)
from time import datatime
from abc import *

class PostOggetto:
    _prezzo:RealGEZ
    _anni_garanzia: IntGEZ
    _descrizione: str
    _is_nuovo: datatime
    _condizione: Condizione