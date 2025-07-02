class Alieno:
    '''
    ci interessa sapere la sua galassia di provenienza
    self.galaxy:str
    '''
    #iniziallizare un oggetto classe alieno
    def __init__(self, galaxy:str):
        self.setGalaxy(galaxy)
    
    def setGalaxy(self, galaxy:str) -> None:
        if galaxy:
            self.galaxy = galaxy
        else:
            print("Errore la galassia di provenienzanon puo essere una stringa vuota!")
        
    def getGalaxy(self) -> str:
        return self.galaxy
    
    def speak(self) -> None:
        print("\niaisaiodfwni")
    
    def __str__(self) -> str:
        return f"\nAlieno proveniente dalla galassia {self.getGalaxy()}!\n"
        