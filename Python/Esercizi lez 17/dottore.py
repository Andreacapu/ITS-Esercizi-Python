# dottore.py
from persona import Persona
from typing import List, Optional, Any

class Dottore(Persona):
    def __init__(self, first_name: str, last_name: str, age: int,
                 specialization: str, parcel: float,
                 patients: Optional[List[Any]] = None):
        super().__init__(first_name, last_name, age)
        self.specialization: Optional[str] = None
        self.parcel: Optional[float] = None
        self.patients: List[Any] = list(patients) if patients is not None else []

        # usa i setter per validare
        self.setSpecialization(specialization)
        self.setParcel(parcel)

    # ---------- SETTER / GETTER ----------
    def setSpecialization(self, specialization: str) -> None:
        if not isinstance(specialization, str) or not specialization.strip():
            self.specialization = None
            print("La specializzazione deve essere una stringa non vuota")
        else:
            self.specialization = specialization.strip()

    def setParcel(self, parcel) -> None:
        # accetta int/float o stringhe numeriche
        value: Optional[float] = None
        if isinstance(parcel, bool):
            # (bool è sottoclasse di int: lo escludo esplicitamente)
            print("La parcella non può essere booleana")
            self.parcel = None
            return
        if isinstance(parcel, (int, float)):
            value = float(parcel)
        elif isinstance(parcel, str):
            try:
                value = float(parcel.replace(",", "."))
            except ValueError:
                value = None

        if value is None:
            print("La parcella va compilata come numero (float)")
            self.parcel = None
        elif value < 0:
            print("La parcella deve essere >= 0")
            self.parcel = None
        else:
            self.parcel = value

    def getSpecialization(self) -> Optional[str]:
        return self.specialization

    def getParcel(self) -> Optional[float]:
        return self.parcel

    # ---------- VALIDAZIONE ----------
    def isAValidDoctor(self) -> bool:
        """
        Regola semplice: età >= 30, specializzazione presente, parcella > 0.
        Ritorna True/False (niente print qui).
        """
        return (
            isinstance(self.age, int) and self.age >= 30 and
            isinstance(self.specialization, str) and len(self.specialization) > 0 and
            isinstance(self.parcel, (int, float)) and (self.parcel or 0) > 0
        )

    # ---------- ALTRO ----------
    def doctorGreet(self) -> str:
        base = super().greet()  # assume che Persona.greet() ritorni una stringa
        spec = self.specialization or "senza specializzazione"
        return f"{base}. Sono un medico {spec}"
