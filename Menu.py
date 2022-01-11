import menuFuncion
   
    
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
        menuFuncion.Ingresar_jugador()
    elif ans=="2":
        print("RULETA()")
        menuFuncion.RULETA()
    elif ans=="3":
        menuFuncion.Eli_Mod_jugador()
    elif ans=="4":
        menuFuncion.Listar()
    elif ans=="5":
        print('*' * 50)
        print("\n Gracias por usar nuestro servicio!\n")
        print('*' * 50)
        ans = False
    elif ans !="1" or ans !="2" or ans !="3" or ans !="4" or ans !="5" or ans !=" ":
      print("\n Elección no válida!, Inténtelo de nuevo\n")
      ans=True

    