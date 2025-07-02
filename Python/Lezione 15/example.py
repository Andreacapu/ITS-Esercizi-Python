PATH: str = "Lezione 15/example.txt"
mode: str = "r"
encoding: str = "utf-8"

file = open(PATH, mode)

print(file)
message: str = "Hello World!\n"
output: str = file.read()
print(output)


with open("Lezione 15/example.txt", "w") as file:
    print(file.read(à))