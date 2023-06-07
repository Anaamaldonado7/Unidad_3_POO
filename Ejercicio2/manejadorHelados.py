from claseHelado import helado
from manejadorSabores import manejaSabores
from claseSabor import Sabor
class manejaHelado:
    __listaHelados = []
    
    def __init__ (self):
        self.__listaHelados = []
    
    
    def AñadirHelado(self,helado):#item1
        self.__listaHelados.append(helado)
        
            
    def RegistrarHelado(self,ManejadorSabores):#item1
        print("\n")
        saboresPorHelado = []
        id = -1
        ManejadorSabores.MostrarSabores()
        while id != 0 :
            print("Ingrese la id del ""Sabor"" a agregar al helado")
            print("Si la respuesta es == 0 (cero) Termina")
            id = input("Respuesta :  ")
            print("\n")
            while id.isdigit() == False:
                print("ERROR - no es un numero")
                print("Ingrese la id del ""Sabor"" a agregar al helado")
                print("Si la respuesta es == 0 (cero) Termina")
                ManejadorSabores.MostrarSabores()
                id = input("Respuesta :  ")
                print("\n")
            id = int(id)
            Respuesta = ManejadorSabores.BuscarSaborID(id)
            if type(Respuesta) == Sabor:
                saboresPorHelado.append(Respuesta)
            else:
                print(" - No se encontró el sabor buscado - o su opcion fue 0 (cero)")
        
        gramos = input("Ingrese los Gramos: ")
        precio = input("Ingrese el precio: ")
        Helao = helado(gramos,precio,saboresPorHelado)
        self.AñadirHelado(Helao)
        
    def ContarRepitenciaSabor(self,sabor):
        contadorTotal = 0
        for i in range(len(self.__listaHelados)):
            #contadorTotal = contadorTotal + self.__ListaHelados[i].contarRepitenciaSaborCH(sabor)
            contadorTotal = self.__listaHelados[i].contarSabores(sabor)
        print("Contador Total Helados : ",contadorTotal)
        return contadorTotal 
        
    def gramosVendidos (self, num):
        conta = 0
        for i in range(len(self.__listaHelados)):
              

        