from ast import While
import os 
import time

from submenu import Menu
from Lista import flista
from Pila import pilas 
from Cola import colas

sub = Menu()
var = flista()

alternativa = ""

lista1 = ["1) Lista", "2) Pila", "3) Cola", "4) Salida"]

while alternativa !=4: 
    os.system("cls")
    alternativa = sub.menu(lista1, "Menú de Opciones")
    os.system("cls")

    if alternativa == "1":
        altern = ""
        while altern != "7":
            os.system("cls")
            altern = sub.menu(["1) Push", "2) Pop", "3) Show", "4) Eliminar ","5) Insertar", "6) Buscar", "7) Salir" ],"Funcioness de Lista")
            os.system("cls")

            if altern == "1":
                print("*"*5,"Ingreso de datos","*"*5)
                dato = input("Digite el dato a añadir: ")
                var.insertar(dato)
                time.sleep(0.5)

            elif altern == "2":
                var.eliminar()
                time.sleep(1)
            
            elif altern == "3":
                var.mostrar()
                time.sleep(1)

            elif altern == "4":
                while True:
                    pos = int(input("Ingrese la posición a eliminar: "))
                    os.system("cls")
                    po = var.eliminarPorPos(pos)
                    if po == True:
                        break
                    else:
                        print("El índice se encuentra fuera de los límites")
                        time.sleep(1)
                        os.system("cls")

            elif altern == "5":
                ind = int(input("Ingrese la posición que desea insertar: "))
                elem = int(input("Ingrese el elemento que quiere ingresar: "))
                var.insertarPorPos(ind,elem)
                time.sleep(1)
                
            elif altern == "6":
                while True:
                    
                    ele = input("Ingrese el elemento que desea conocer la posición: ")
                    eli = var.buscar(ele)
                    if eli == True:
                        break

                    else:
                        print("El índice se encuentra fuera de los límites")
                        time.sleep(1)
                        os.system("cls")

            
            elif altern == "7":
                print("Saliendo del menú...")
                time.sleep(2)

    if alternativa == "2":
        altern = ""
        tama = int(input("Digite el tamaño que tendrá la pila: "))
        sus = pilas(tama)
        while altern != "6":
            os.system("cls")
            altern = sub.menu(["1) Push", "2) Pop", "3) Show", "4) Buscar ","5) Longitud ", "6) Salir"],"Funciones de Pila")
            os.system("cls")
            
            if altern == "1":
                print("*"*5,"Ingreso de datos","*"*5)
                dato = input("Digite un valor a ingresar: ")
                sus.push(dato)
                time.sleep(1)

            elif altern == "2":
                print(sus.pop())
                time.sleep(1)

            elif altern == "3":
                sus.show()
            
            elif altern == "4":
                while True:
                    buscado = input("Ingrese el elemento que desea conocer la posición: ")
                    eli = sus.buscar(buscado)
                    if eli == True:
                        break

                    else:
                        print("El índice se encuentra fuera de los límites")
                        time.sleep(1)
                        os.system("cls")

            elif altern == "5":
                print(sus.longitud())
                time.sleep(1)

            elif altern == "6":
                print("Saliendo al menú...")

    if alternativa == "3":
        altern = ""
        tama = int(input("Digite el tamaño que tendrá la cola: "))
        col = colas(tama)
        while altern != "6":
            os.system("cls")
            altern = sub.menu(["1) Push", "2) Pop", "3) Show", "4) Buscar ","5) Longitud ", "6) Salir"],"Funciones de Pila")
            os.system("cls")
            
            if altern == "1":
                print("*"*5,"Ingreso de datos","*"*5)
                dato = input("Digite un valor a ingresar: ")
                col.push(dato)
                time.sleep(1)

            elif altern == "2":
                print(col.pop())
                time.sleep(1)

            elif altern == "3":
                col.show()
            
            elif altern == "4":
                while True:
                    buscado = input("Ingrese el elemento que desea conocer la posición: ")
                    eli = col.buscar(buscado)
                    if eli == True:
                        break

                    else:
                        print("El índice se encuentra fuera de los límites")
                        time.sleep(1)
                        os.system("cls")

            elif altern == "5":
                print(col.longitud())
                time.sleep(1)

            elif altern == "6":
                print("Saliendo al menú...")


                




    