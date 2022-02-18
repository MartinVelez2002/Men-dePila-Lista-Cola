import time
class colas:

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
            print("Cola está Llena")
   
    def pop(self):
        if self.empty():
            return "Cola está Vacía"
        else:
            top = self.lista[0]
            self.tope -= 1
            self.lista = self.lista[1:]
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
            for i in range(0,self.tope):
                print('[{}]'.format(self.lista[i]))
            time.sleep(1)