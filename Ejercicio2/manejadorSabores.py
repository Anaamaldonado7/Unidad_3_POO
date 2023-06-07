import csv
from claseSabor import Sabor
class manejaSabores:
    __listaSabores = []
    
    def __init__ (self):
        self.__listaSabores = []
        
    def carga (self):
        archivo = open("sabores.csv")
        reader = csv.reader(archivo,delimiter=";")
        for fila in reader:
            num = int(fila[0])
            ing = str(fila[1])
            nom = str(fila[2])
            s = Sabor (num,ing,nom)
            self.__listaSabores.append(s)    
            
    def MostrarSabores(self):
        for i in range(len(self.__listaSabores)):
            print(self.__listaSabores[i].getId(), "-" ,self.__listaSabores[i].getNombreSabor())

    
    def BuscarSaborID(self,id):
        i = 0
        band = False
        while i < len(self.__listaSabores) and band == False:
            if id == self.__listaSabores[i].getId():
                band = True
                return self.__listaSabores[i]
            else:
                i = i + 1  
    
    def saboresMasPedidos (self,ManejadorHelados):
        listaContadores = []
        for i in range(len(self.__listaSabores)):
            CantidadTotal = ManejadorHelados.ContarRepitenciaSabor(self.__listaSabores[i])
            nombre = self.__listaSabores[i].getNombreSabor()
            ambos = (nombre, CantidadTotal) #tupla
            listaContadores.append(ambos)
        return listaContadores    

    def ordenar (self, manejadorHelados):
        lista = self.saboresMasPedidos(manejadorHelados)
        lista.sort(reverse = True)
        if len(lista) >= 5:
            print("Los 5 sabores más pedidos son : ")
            for i in range(5):
                print(lista[i][0])
        else :
            print("Los 5 sabores más Pedidos : (No llegan a 5)") 
            for i in lista:
                print(lista[i][0])




           