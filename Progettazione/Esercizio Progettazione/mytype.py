@dataclass
class Studente:
    matricola: TipoMatricola       # Formato personalizzato (es: "S12345")
    nome: str
    cognome: str
    genere: Genere                 # Scelta vincolata
    anno_iscrizione: int           # Anno accademico (es: 2023)
    corsi_iscritti: List['Corso']  # Relazione molti-a-molti
    esami_sostenuti: List['Esame'] # Relazione uno-a-molti



class Email:
    """Classe per la gestione di un indirizzo email con validazione."""
    
    __email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    
    def __init__(self, indirizzo: str):
        if not self.__class__.is_valid(indirizzo):
            raise ValueError(f"Formato email non valido: {indirizzo}")
        self._indirizzo = indirizzo.lower()  # Normalizza in lowercase