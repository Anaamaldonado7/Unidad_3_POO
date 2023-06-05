class TallerCapacitacion:
    __idTaller = int
    __nom = str
    __vacantes = int
    __montoInscripcion = int
    __listaInscripciones = []
    
    def __init__(self, idTaller, nom, vacantes, monto):
        self.__idTaller = str(idTaller)
        self.__nom = str(nom)
        self.__vacantes = int(vacantes)
        self.__montoInscripcion =int(monto)
        
    def getId(self):
        return self.__idTaller
    def getNom(self):
        return self.__nom
    def getVacantes (self):
        return self.__vacantes
    def getMonto (self):
        return self.__montoInscripcion
    def actualizarVacante (self):
        self.__vacantes -= 1
    def mostrarDatosTaller(self):
        print(f"id: {self.__idTaller}\n{self.__nom}\nVac. disponibles{self.__vacantes}\nPrecio: {self.__montoInscripcion}\n")