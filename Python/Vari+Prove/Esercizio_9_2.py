class Restaurant:
    def __init__ (self, restaurant_name:str, cuisine_type:str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cuisine_type}")
    
    def open_restaurant(self, open:str):
         self.open = ("Aperto")
        

restaurant1= Restaurant("Jinjà", "Cucina Giapponese")
restaurant2 = Restaurant("Wok", "Cucina Coreana")
restaurant3 = Restaurant("Da Marcello", "Cucina Italiana")

restaurant1.open_restaurant("Aperto")
restaurant2.open_restaurant("Aperto")
restaurant3.open_restaurant("Aperto")
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
