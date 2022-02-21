import os
import time
class pilas:

    def __init__(self, tama):
        self.lista=[]
        self.tope=0
        self.size = tama

    def empty(self):
        return self.tope == 0
    
    def push(self,dato):
        if self.tope < self.size:
            self.lista += [dato]
            self.tope += 1
        else:
            print("La Pila está Llena")
   
    def pop(self):
        if self.empty():
            return "Lista Vacía"
        else:
            top = self.lista[-1]
            self.tope -= 1
            self.lista = self.lista[:-1]
            return top

    def buscar(self,buscado):
        try:
            if buscado in self.lista:
                print("El elemento seleccionado se encuentra en la posición: {} ".format(self.lista.index(buscado)))
                time.sleep(1)
                return True

        except ValueError:
            return False

    def longitud(self):
        return self.tope
        
    def show(self):
        if self.empty():
            print("Lista vacia")
        else:                    
            for i in reversed(self.lista):
                print('Los elementos de la pila en reversa sería: [{}]'.format(i))
            time.sleep(1)
   
    