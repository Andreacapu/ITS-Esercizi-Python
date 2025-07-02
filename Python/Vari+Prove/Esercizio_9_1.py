class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str, open: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open = open
        
    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cuisine_type}, Aperto: {self.open}")
    
    def open_restaurant(self, open: str):
        self.open = open
        

jinja = Restaurant("Jinjà", "Cucina Giapponese", "No")
wok = Restaurant("Wok", "Cucina Coreana", "No")

jinja.open_restaurant("Si")
wok.open_restaurant("Si")
jinja.describe_restaurant()
wok.describe_restaurant()