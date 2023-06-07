class Sabor:
    __idSabor = 0
    __ingredientes = str
    __nombreSabor = str
    
    def __init__ (self, idSabor, ingredientes, nombreSabor):
        self.__idSabor = idSabor
        self.__ingredientes = ingredientes
        self.__nombreSabor = nombreSabor
        
    def getId (self):
        return self.__idSabor
    def getIngredientes (self):
        return self.__ingredientes
    def getNombreSabor (self):
        return self.__nombreSabor    