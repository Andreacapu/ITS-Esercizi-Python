class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)
andrea = Person("Andrea C.", 25)
luca = Person("Luca C.", 53)
adriano = Person("Adriano G.", 18)

people = [alice, bob, andrea, luca, adriano]


oldest=0
if bob.age > alice.age:
    oldest=bob.age
else:
    oldest=alice.age
    print(f"Bob is the oldest with {oldest} years")

youngest=120
for i in range(len(people)):
    if youngest > people[i].age:
            youngest=people[i].age
print(f"the youngest person has {youngest} years")
