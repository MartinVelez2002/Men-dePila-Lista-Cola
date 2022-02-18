import time

class flista:
    def __init__(self, datos=[]):

        self.datos=[]

    def insertar (self,dato):
        self.datos.append(dato)

        print("La lista actualizada es: {} ".format(self.datos))


    def eliminar (self):
        eli = self.datos.pop()
        print("Se eliminó el dato el último dato que es: {}".format(eli))

    def mostrar (self):
        print("La lista actual es: {} ".format(self.datos))

    def eliminarPorPos (self, pos):
        try:
            if pos <= len(self.datos):
                self.datos.pop(pos)
                print("La nueva lista quedaría: {} ".format(self.datos))
                time.sleep(1)
                return True
        except ValueError:
            return False

    def insertarPorPos (self, ind, elem):
        self.datos.insert(ind,elem)
        print("La nueva lista quedaría: {} ".format(self.datos))
    
    def buscar (self,ele):
        try:
            if ele in self.datos:
                print("El elemento seleccionado se encuentra en la posición: {} ".format(self.datos.index(ele)))
                time.sleep(1)
                return True
                
        except ValueError:
            return False



        

    