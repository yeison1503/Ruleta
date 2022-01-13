# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 23:00:50 2022

@author: yeison
"""
#Prueba de Programación - Casino Ruleta

import Ruleta

new_jugador = list()
costo = 10000

class Jugador():
    def init(self, name="", age="", cash=""):
        self.name = name
        self.age = age
        self.cash = cash

#Guardar nuevo jugador
def NEW_jugador():
    n_jugador = Jugador()       #Se crea el jugador
    n_jugador.name = str(input("Ingrese su nombre.\n"))
    x=True
    while x:
        x=False
        for i in range(len(new_jugador)):
            if new_jugador[i].name == n_jugador.name:
                print("El nombre ingresado ya se encuentra en uso.\n")
                n_jugador.name = input("Ingrese otro nombre.\n")
                x=True
                break
    n_jugador.age = input("Ingrese la edad.\n")
    n_jugador.cash = input("Ingrese el valor del dinero.\n")
    new_jugador.append(n_jugador) 
    print("Jugador Creado con Exito!")

#juego de la ruleta
def RULETA():
    print("El costo para jugar a la RULETA es de {} pesos.".format(costo))
    usr = str(input("Ingrese el nombre del usuario que desea jugar.\n"))
    for i in range(len(new_jugador)):
        if usr == new_jugador[i].name:
            costo_usr = int(new_jugador[i].cash)
            if int(new_jugador[i].cash) <= costo:
                print("{}, No puedes jugar a la RULETA, saldo insifuciente {}!\n".format(new_jugador[i].name,new_jugador[i].cash))
            elif int(new_jugador[i].age) <= 18:
                print("{}, No puedes jugar a la RULETA, eres menor de edad!\n".format(new_jugador[i].name))
            else:
                print("{}, Su dinero actual es {}, se le descontaran 10000 para jugar a la RULETA\n".format(new_jugador[i].name,new_jugador[i].cash))
                costo_usr -= costo
                win = Ruleta.Juego_ruleta()
                costo_usr += win
                new_jugador[i].cash = str(costo_usr)
        else:
            print("El usuario no EXISTE!")

#Modificar y eliminar jugador
def Delete_jugador():
    print ("""
    1.Modificar Jugador.
    2.Eliminar Jugador.
    3.Atras.
    """)
    opt=input("Elige: \n") 
    #Modificar jugador
    if opt=="1": 
        print("Para poder modificar los datos de un jugador se debe ingresar el nombre y la edad por seguridad\n")
        d_jugador = str(input("Ingrese el nombre del jugador que desea modificar.\n"))
        d_edad = str(input("Ingrese la edad.\n"))
        for i in range(len(new_jugador)):
            if d_jugador == new_jugador[i].name and d_edad == new_jugador[i].age:
                print("¿{}, Desea cambiar su nombre?\n".format(new_jugador[i].name))
                mod = str(input("Ingrese 'si' para modificar o 'no' para continuar\n"))
                if mod == "si":
                    nombre = str(input("Ingrese nuevo nombre\n"))
                    new_jugador[i].name = nombre
                    edad = str(input("Ingrese la edad\n"))
                    new_jugador[i].age = edad
                    dinero = str(input("Ingrese el nuevo valor del dinero\n"))
                    new_jugador[i].cash = dinero
                elif mod == "no":
                    edad = str(input("Ingrese la edad\n"))
                    new_jugador[i].age = edad
                    dinero = str(input("Ingrese el nuevo valor del dinero\n"))
                    new_jugador[i].cash = dinero
                print("Jugador Modificado con Exito!.")
                #print(new_jugador[i].name,new_jugador[i].age,new_jugador[i].cash)
            else:
                print("Nombre del jugador incorrecto o jugador no existente!.\n")
    #Eliminar jugador
    elif opt=="2":
        d_jugador = str(input("Ingrese el nombre del jugador que desea eliminar\n"))
        for i in range(len(new_jugador)):
            if new_jugador[i].name == d_jugador:
                d_edad = input("Ingrese la edad de {}\n".format(new_jugador[i].name))
                if new_jugador[i].age == d_edad:
                    new_jugador.pop(i)
                    print("Jugador Eliminado  correctamente!\n")
                    break
                else:
                    print("Edad incorrecta!\n")
    elif opt=="3":
        pass
    elif opt !="1" or opt !="2" or opt !="3" or opt !=" " :
      print("\n Elección no válida!, Inténtelo de nuevo\n")

#listar base de datos de los jugadores 
def Listar_jugador():
    if not new_jugador:
        print("Todavia no hay jugadores creados.\n")
    else:
        for i in range(len(new_jugador)):
            print("Nombre Edad Dinero")
            print(new_jugador[i].name,new_jugador[i].age,new_jugador[i].cash)

#menu de Inicio
print('*' * 50)
print("\n Bienvenido al CASINO RULETA Inter-Telco \n")
print('*' * 50)
menu = ""
ans=True
while ans:
    print ("""
    1.Agregar Jugador.
    2.Jugar a la Ruleta.
    3.Eliminar o modificar Jugador.
    4.Listar Jugadores Guardados.
    5.Salir/Exit.
    """)
    ans=input("¿Qué te gustaría hacer? \n") 
    if ans=="1": 
        NEW_jugador()
    elif ans=="2":
        RULETA()
    elif ans=="3":
        Delete_jugador()
    elif ans=="4":
        Listar_jugador()
    elif ans=="5":
        print("\n Goodbye") 
        ans = False
    elif ans !="1" or ans !="2" or ans !="3" or ans !="4" or ans !="5" or ans !=" ":
      print("\n Elección no válida!, Inténtelo de nuevo\n")
      ans=True


















