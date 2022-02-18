class Menu:
    secuencia = 0 
    def menu(self, opciones, título):
        print("*"*20, título, "*"*20)
        for i in opciones: 
            print(i)
        alt = input("Elija una opción, 1 al {}: ".format(len(opciones)))
        return alt


        

    