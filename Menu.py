import funciones


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
        nombre = str(input("Ingrese su nombre.\n"))
        edad = input("Ingrese la edad.\n")
        dinero = input("Ingrese el valor del dinero.\n")
        funciones.NEW_jugador(nombre, edad, dinero)
        print("Jugador Creado con Exito!")
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

    