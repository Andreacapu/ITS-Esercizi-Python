class Student:
    def __init__(self, name:str, studyProgram:str, age:int, gender:str):
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender

    def printInfo(self):
        print(f"{self.name}: {self.studyProgram}: anni {self.age}: sesso {self.gender}")
andr = Student("Andrea","Cybersec", 25, "M")
rach = Student("Rachele", "Cybersec", 27, "F")
edo = Student("Edoardo", "Cybersec", 21, "M")

andr.printInfo()
rach.printInfo()
edo.printInfo()
