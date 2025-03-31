class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str, open: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open = open
        self.number_served = 0  # Inizializzato a 0
        
    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cuisine_type}, Aperto: {self.open}, Clienti serviti: {self.number_served}")
    
    def open_restaurant(self, open: str):
        self.open = open
        
    def set_number_served(self, new_number: int):
        self.number_served = new_number
    
    def increment_number_served(self, additional_served: int):
        self.number_served += additional_served
        

# Creazione istanze (ora con 3 parametri)
jinja = Restaurant("Jinjà", "Cucina Giapponese", "No")
wok = Restaurant("Wok", "Cucina Coreana", "No")

# Operazioni
jinja.describe_restaurant()
wok.describe_restaurant()

jinja.open_restaurant("Si")
wok.open_restaurant("Si")  # Corretto il typo

jinja.number_served = 15
wok.number_served = 20

jinja.set_number_served(45)
wok.set_number_served(55)

jinja.increment_number_served(16)
wok.increment_number_served(7)

# Stampa finale
print("\nStato finale:")
jinja.describe_restaurant()
wok.describe_restaurant()
