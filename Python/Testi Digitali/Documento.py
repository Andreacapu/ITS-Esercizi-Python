class Documento:
    def __init__(self, text:str):
        self.setText(text)
    def setText(self, text:str):
        self.__text = text
    def getText(self)->str:
        return self.__text
    def isInText(self, word:bool) -> bool:
        if word in self.getText():
            return True
        else:
            return False

class Email(Documento):
    def __init__(self, text, mittente:str, destinatario:str, titolo:str, messaggio:str):
        super().__init__(text)
    def mittente(self, mittente:str):
        self._mittente = mittente
    def destinatario(self, destinatario:str):
        self._destinatario = destinatario
    def GetMittente(self)->str:
        return self._mittente
    def GetDestinatario(self) ->str:
        return self._destinatario
    def setTitolo(self,titolo:str):
        self._titolo = titolo
    def GetTitolo(self) -> str:
        return self._titolo
    def getText(self) -> str:
        return f"\nDa: {self.mittente} \nA: {self.destinatario} \nTitolo: {self.setTitolo} \nMessaggio: {self.__text}"
    def __repr__(self):
        return f"{self.getText()}"

class File(Documento):
    def __init__(self, text, path_file:str):
        super().__init__(self.ReadToTextFile())
    def setPath_File(self, path_file:str):
        self.path_file = path_file
    def getPath_FIle(self, path_file:str)->str:
        return self.path_file
    def ReadToTextFile(self, path_file:str):
        with open(path_file, "r") as reader:
            return reader.readlines()
    def getText(self, ext, mittente:str, destinatario:str, titolo:str, messaggio:str)->str:
        return f"\nDa: {self.mittente} \nA: {self.destinatario} \nTitolo: {self.setTitolo} \nMessaggio: {self.__text}"
        
        