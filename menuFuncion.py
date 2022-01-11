# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 16:41:32 2022

@author: yeiso
"""
import funciones

costo = 10000


def Ingresar_jugador():
    condicion = False
    while(not condicion):
        print("\nEl tamaño del nombre no puede ser mayor a 10 dígitos\n")
        nombre = str(input("Ingrese su nombre.\n"))
        if len(nombre) <= 10:
            vnombre = funciones.consultarNom(nombre)
            #print(vnombre)
            if nombre == vnombre:
                 print("\nEl nombre ingresado ya se encuentra en uso!.\n")
            else:
                condiEdad = False
                while(not condiEdad):
                    print("La edad no puede superar 2 dígitos\n")
                    edad = input("Ingrese la edad.\n")
                    if edad.isnumeric():
                        edad = int(edad)
                        if edad > 0 and edad < 100:
                            condiEdad = True
                    else:
                        print("\nEdad incorrecta.")
                condinero = False
                while(not condinero):
                    print("Ingrese el dinero en números.\n")
                    dinero = input("Ingrese el valor del dinero.\n")
                    if dinero.isnumeric():
                        dinero = int(dinero)
                        condinero = True                
                    else:
                        print("\nIncorrecta.")
                funciones.NEW_jugador(nombre, edad, dinero)
                print("Jugador Creado con Exito!")
                condicion = True
        else:
            print("\nNombre incorrecto.")    
        

def RULETA():
    print("El costo para jugar a la RULETA es de {} pesos.".format(costo))
    usr = str(input("Ingrese el nombre del usuario que desea jugar.\n"))
    vnombre = funciones.consultarNom(usr)
    if usr == vnombre:
         #print("El nombre ingresado ya se encuentra en uso!.\n")
         costo_usr = funciones.consultarSaldo(usr)
         edadUsr = funciones.consultarEdad(usr)
         print(type(costo_usr),type(edadUsr))
         if int(costo_usr) <= costo:
             print("{}, No puedes jugar a la RULETA, saldo insifuciente {}!\n".format(usr,costo_usr))
         elif int(edadUsr) <= 18:
             print("{}, No puedes jugar a la RULETA, eres menor de edad!\n".format(usr))
         else:
            print("{}, Su dinero actual es {}, se le descontaran 10000 para jugar a la RULETA\n".format(usr,costo_usr))
            costo_usr -= costo
            #win = Ruleta.Juego_ruleta()
            #costo_usr += win
            funciones.modificarSaldo(usr, costo_usr)
    else:
        print("El usuario no EXISTE!")
        

def Eli_Mod_jugador():
    print ("""
    1.Modificar Jugador.
    2.Eliminar Jugador.
    3.Atras.
    """)
    opt=input("Elige: \n") 
    #Modificar jugador
    if opt=="1": 
        print("Debe ingresar el id para poder modificar los datos del usuario.\n")
        id = input("Ingrese el id del jugador que desea modificar.\n")
        vid = funciones.consultarId(id)
        if id == vid:
             print("El ID ingresado es Incorrecto!.\n")
        else:
            nombre = input("Ingrese el nuevo nombre.\n")
            edad = input("Ingrese la nueva edad.\n")
            dinero = input("Ingrese el nuevo valor del dinero.\n")
            funciones.modificar(nombre, edad, dinero, id)
            print("Jugador Modificado con Exito!.")
    #Eliminar jugador
    elif opt=="2":
        nombre = str(input("Ingrese el nombre del jugador que desea eliminar\n"))
        funciones.eliminar(nombre)
        print("Jugador Eliminado  correctamente!\n")
    elif opt=="3":
        pass
    elif opt !="1" or opt !="2" or opt !="3" or opt !=" " :
      print("\n Elección no válida!, Inténtelo de nuevo\n")


def Listar():
    listaJug = funciones.Listar_jugador()
    if not listaJug:
        print("No hay jugadores inscritos en la Base de Datos!.\n")
    else:
        #print("ID: - Nombre: - Edad - Dinero: \n")
        for listaJug in listaJug:
            print("Nombre: {1} - Edad: {2} - Dinero: {3} | ID: {0}".format(listaJug[0],listaJug[1],listaJug[2],listaJug[3]))