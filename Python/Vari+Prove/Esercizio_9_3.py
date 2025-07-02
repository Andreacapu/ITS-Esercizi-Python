class User:
    def __init__ (self, first_name:str, last_name:str, age:int, eyes:str, sex:str, greet:str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.eyes = eyes
        self.sex = sex
        self.greet = greet
        
    def printInfo(self):
        print(f"{self.first_name}, {self.last_name}, {self.age}, {self.eyes}, {self.sex}, {self.greet}")
    def greet_user(self, greet:str):
        self.greet = greet
        
user1 = User("Andrea", "Capuani", 25, "Marroni", "Uomo", "da decidere")
user2 = User("Anastasia", "Mirucci", 42, "Verdi", "Donna", "da decidere")
user3 = User("Alessio", "Della Rocca", 18, "Blu", "Uomo", "da decidere")
user4 = User("Maria", "De Santis", 33, "Blu", "Donna", "da decidere")

user1.greet_user("Ciao Andrea")
user2.greet_user("Benvenuta Anastasia")
user3.greet_user("Bentornato Alessio")
user4.greet_user("Buongiorno Maria")
user1.printInfo()
user2.printInfo()
user3.printInfo()
user4.printInfo()


    
 
