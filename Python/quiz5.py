def accesso(username: str, password:int, active:True):
    while True:
        username = input("inserie lo username: ")
        passowrd = input(int("digitare la password: "))
        if username == "admin" and password == 12345 and is_active:
            print("accesso consentito")
        else:
            print("accesso negato")