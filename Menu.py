import funciones

def Ingresar_jugador():
    nombre = str(input("Ingrese su nombre.\n"))
    # if nombre == funciones.consultar(nombre):
    #     print("El nombre ingresado ya se encuentra en uso.\n")
    # else:
    edad = input("Ingrese la edad.\n")
    dinero = input("Ingrese el valor del dinero.\n")
    funciones.NEW_jugador(nombre, edad, dinero)
    print("Jugador Creado con Exito!")

def Eli_Mod_jugador():
    print ("""
    1.Modificar Jugador.
    2.Eliminar Jugador.
    3.Atras.
    """)
    opt=input("Elige: \n") 
    #Modificar jugador
    if opt=="1": 
        print("Se debe ingresar el id para poder modificar los datos del usuario.\n")
        id = str(input("Ingrese el id del jugador que desea modificar.\n"))
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
        Ingresar_jugador()
    elif ans=="2":
        print("RULETA()")
    elif ans=="3":
        Eli_Mod_jugador()
    elif ans=="4":
        funciones.Listar_jugador()
    elif ans=="5":
        print("\n Goodbye") 
        ans = False
    elif ans !="1" or ans !="2" or ans !="3" or ans !="4" or ans !="5" or ans !=" ":
      print("\n Elección no válida!, Inténtelo de nuevo\n")
      ans=True

    