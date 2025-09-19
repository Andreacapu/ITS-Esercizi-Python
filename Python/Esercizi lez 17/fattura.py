# fatture.py
from typing import List, Optional, Any

class Fattura:
    """
    Gestisce le fatture (conteggio pazienti) e il salario del dottore.
    Attributi:
      - doctor: istanza di Dottore (o None se non valido)
      - patients: lista pazienti (o None se non valido)
      - fatture: int (numero di pazienti) o None se non valido
      - salary: int (parcella * numero pazienti) o None se non valido
    """

    # ---------------- COSTRUTTORE ----------------
    def __init__(self, patients: List[Any], doctor: Any):
        """
        init(patient, doctor):
        - Verifica doctor.isAValidDoctor()
        - Se valido:
            * fatture = numero pazienti del dottore
            * salary  = 0 (int)
            * imposta doctor/patients
        - Se NON valido:
            * assegna None a TUTTI e 4 gli attributi
            * stampa: "Non è possibile creare la classe fattura poichè il dottore non è valido!"
        """
        self.doctor: Optional[Any] = None
        self.patients: Optional[List[Any]] = None
        self.fatture: Optional[int] = None
        self.salary: Optional[int] = None

        # Controllo presenza e risultato di isAValidDoctor()
        is_valid = False
        if hasattr(doctor, "isAValidDoctor") and callable(getattr(doctor, "isAValidDoctor")):
            try:
                is_valid = bool(doctor.isAValidDoctor())
            except Exception:
                is_valid = False

        if is_valid:
            # Dottore valido: imposto attributi
            self.doctor = doctor

            # Mi assicuro che esista una lista pazienti sul dottore, e la sincronizzo
            doc_has_list = hasattr(doctor, "patients") and isinstance(getattr(doctor, "patients"), list)
            if doc_has_list:
                # Sovrascrivo la lista del dottore con quella passata, per coerenza
                doctor.patients = list(patients) if patients is not None else []
                self.patients = doctor.patients
            else:
                self.patients = list(patients) if patients is not None else []
                # Provo ad agganciarla anche al dottore (comodo per altre classi)
                try:
                    setattr(doctor, "patients", self.patients)
                except Exception:
                    pass

            # fatture = numero pazienti che ha il dottore
            self.fatture = len(self.patients)
            # salary parte da 0 (int)
            self.salary = 0
        else:
            # Dottore non valido: lascio tutti e 4 a None e stampo l'errore richiesto
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    # ---------------- METODI RICHIESTI ----------------
    def getSalary(self) -> int:
        """
        Ritorna il salario guadagnato dal dottore:
        salario = parcella del dottore * numero di pazienti (cast a int).
        """
        if not self.doctor or self.patients is None:
            return 0

        parcel = self._get_doctor_parcel()
        num = len(self._patients_list())
        self.salary = int(parcel * num)
        return self.salary

    def getFatture(self) -> int:
        """
        Aggiorna e ritorna l'attributo fatture come numero corrente di pazienti del dottore.
        """
        if self.patients is None:
            return 0
        self.fatture = len(self._patients_list())
        return self.fatture

    def addPatient(self, newPatient: Any) -> None:
        """
        Aggiunge un paziente alla lista del dottore, poi aggiorna fatture e salary.
        Stampa: "Alla lista del Dottor cognome è stato aggiunto il paziente {codice_identificativo}"
        """
        if not self.doctor or self.patients is None:
            print("Operazione non possibile: dottore non valido.")
            return

        lst = self._patients_list()
        lst.append(newPatient)

        cognome = self._doctor_last_name()
        pid = self._patient_id(newPatient) or "SENZA_ID"
        print(f"Alla lista del Dottor {cognome} è stato aggiunto il paziente {pid}")

        # Aggiorno conteggio e salario
        self.getFatture()
        self.getSalary()

    def removePatient(self, idCode: str) -> bool:
        """
        Rimuove il paziente con ID fornito.
        Stampa: "Alla lista del Dottor cognome è stato rimosso il paziente {codice_identificativo}"
        Aggiorna fatture e salary. Ritorna True se rimosso, False se non trovato.
        """
        if not self.doctor or self.patients is None:
            print("Operazione non possibile: dottore non valido.")
            return False

        lst = self._patients_list()
        idx = -1
        for i, p in enumerate(lst):
            if self._patient_id(p) == idCode:
                idx = i
                break

        cognome = self._doctor_last_name()
        if idx >= 0:
            lst.pop(idx)
            print(f"Alla lista del Dottor {cognome} è stato rimosso il paziente {idCode}")
            removed = True
        else:
            print(f"Nessun paziente con ID {idCode} nella lista del Dottor {cognome}")
            removed = False

        self.getFatture()
        self.getSalary()
        return removed

    # ---------------- SUPPORTO INTERNO ----------------
    def _patients_list(self) -> List[Any]:
        return self._patients_list()

    def _patients_list(self) -> List[Any]:
        """
        Accessor centralizzato per la lista pazienti.
        Preferisce doctor.patients se disponibile, altrimenti self.patients.
        """
        if self.doctor is not None and hasattr(self.doctor, "patients") and isinstance(self.doctor.patients, list):
            return self.doctor.patients
        return self.patients or []

    def _get_doctor_parcel(self) -> float:
        """
        Legge la parcella del dottore supportando sia 'parcel' che 'parcella'.
        """
        if hasattr(self.doctor, "parcel") and self.doctor.parcel is not None:
            return float(self.doctor.parcel)
        if hasattr(self.doctor, "parcella") and self.doctor.parcella is not None:
            return float(self.doctor.parcella)
        raise AttributeError("Il dottore non ha un attributo 'parcel'/'parcella' valido.")

    def _doctor_last_name(self) -> str:
        """
        Restituisce il cognome (supporta 'last_name' o 'cognome').
        """
        if hasattr(self.doctor, "last_name") and self.doctor.last_name:
            return str(self.doctor.last_name)
        if hasattr(self.doctor, "cognome") and self.doctor.cognome:
            return str(self.doctor.cognome)
        # fallback
        return getattr(self.doctor, "lastName", "Sconosciuto")

    def _patient_id(self, p: Any) -> Optional[str]:
        """
        Prova a leggere un identificativo paziente con più nomi campo tipici.
        """
        for attr in ("IDcode", "idCode", "codice_identificativo"):
            if hasattr(p, attr):
                val = getattr(p, attr)
                return None if val is None else str(val)
        return None
