class helado:
    __gramos = float
    __precio = float
    __sabores = []
    
    def __init__ (self, gramos, precio, sabores):
        self.__gramos = gramos
        self.__precio = precio
        #self.__sabores = [] 
        
    def getGramos (self):
        return self.__gramos
    def getPrecio (self):
        return self.__precio
           
    def contarSabores(self,sabor):
        contador = 0
        for i in range(len(self.__sabores)):
            if sabor == self.__sabores[i]:
                contador = contador + 1
        valor = contador
        print("Contador helado : ",contador)
        return valor       