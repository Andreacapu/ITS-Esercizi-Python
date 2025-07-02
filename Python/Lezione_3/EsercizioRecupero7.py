class ContactManager:
    def __init__(self):
        self.contacts:dict[str,list[str]] = {}

    def create_contatc(self, nome: str, phone_number: list[str]) -> dict[str, list[str]]:
        new_contracts:dict = {}
        new_contracts[nome] = phone_number
        if nome not in self.contacts:
            self.contacts[nome] = phone_number

        else:
            raise ValueError("Errore: il contatto esiste già.")
        return new_contracts
        
    def add_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:
        new_phone_numb: dict={}
        new_phone_numb[contact_name]= phone_number

        if contact_name not in self.contacts.keys():
            raise ValueError("Errore: il contatto non esiste.")
        elif phone_number not in self.contacts(contact_name):
            raise ValueError("Errore: il numero di telefono esiste già.")

        else:
            self.contacts[contact_name].append(phone_number)
        return new_phone_numb
    
    def remove_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:
        self.contacts[contact_name].remove[phone_number]
        new_remove_phone_number = {}
        new_remove_phone_number[contact_name] = self.contacts[contact_name]

        if contact_name not in self.contacts.keys():
            raise ValueError("Errore: il contatto non esiste.")
        elif phone_number not in self.contacts(contact_name):
            raise ValueError("Errore: il numero di telefono non è presente.")
        else: 
            self.contacts[contact_name].remove(phone_number)
            new_remove_phone_number:dict = {}
            new_remove_phone_number[contact_name]=self.contacts[contact_name]

    def update_phone_number(self, contact_name: str, old_phone_number: str, new_phone_number: str) -> dict[str, list[str]]:
        if contact_name not in self.contacts.keys():
            raise ValueError("Errore: il contatto non esiste.")
        elif old_phone_number not in self.contacts[contact_name]:
            raise ValueError("Errore: il numero di telefono non è presente.")
        else:
            self.contacts[contact_name].remove(old_phone_number)
            self.contacts[contact_name].append(new_phone_number)
            new_phone_number:dict = {}
            new_phone_number[contact_name] = self.contacts(contact_name)

    def list_contacts(self) -> list: 
        list_contacts:list = []
        for contact in self.contacts.keys():
            list_contacts.append(contact)
        return list_contacts
    
    def list_phone_numbers(self, contact_name: str) -> list: 
        new_list_phone_numbers:list = []
        if contact_name not in self.contacts.keys():
            raise ValueError ("Errore: il contatto non esiste.")
        
        else:
            for value in self.contacts[contact_name]:
                new_list_phone_numbers.append(value)

    def search_contact_by_phone_number(self, phone_number: str) -> list: 
        new_search_phone: list = []
        for key, value in self.contacts.items():
            if phone_number not in self.contacts.keys():
                raise ValueError("Nessun contatto trovato con questo numero di telefono.")
        else:
            for key, phone_number in self.contacts.items():
                if phone_number is self.contacts(key):
                    new_search_phone.append(key)
        return new_search_phone
