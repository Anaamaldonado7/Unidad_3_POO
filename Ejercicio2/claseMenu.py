from manejadorSabores import manejaSabores
from manejadorHelados import manejaHelado
class menu: 
    __opcion=None
    
    def mostrarmenu(self):
        Obj1= manejaSabores ()
        Obj2= manejaHelado ()
        Obj1.carga()
        Salir = True
        while Salir:
            print('[1] Registrar un helado vendido ')
            print('[2] Mostrar los 5 sabores mas pedidos ')
            print('[3]  ')
            print('[4] Salir ')
            self.__opcion=input('\nIngrese una opcion: ')
            if self.__opcion=='0':
                Salir = False
            if self.__opcion=='1':
                Obj2.RegistrarHelado(Obj1)
            if self.__opcion=='2':
                Obj1.ordenar(Obj2)   