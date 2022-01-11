# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 17:34:16 2022

@author: yeiso
"""

import random

# Constantes para las opciones de la Ruleta
APUESTA_MINIMA = 500
DINERO_GANADO_PARTIDAD = 3000
NUMERO = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
COLOR = ["verde","rojo","negro","rojo","negro","rojo","negro","rojo","negro","rojo","negro","verde","rojo","negro","rojo","negro","rojo","negro","rojo","rojo","negro"]

sintesis_ruleta = """
Ruleta: se puede apostar por:
    
* Solo al Número: Si aciertas, la apuesta se multiplica por 10. Si no, se pierde la apuesta.
* Solo al color: si se acierta el color, la apuesta se multiplica por 15 si el color es verde, la apuesta se multiplica por 2 si el color es rojo o negro. Si no, pierde la apuesta.
* Solo paridad: si se acierta entre las opciones de número par o número impar, se gana 3000 pesos. Si no, se pierde la apuesta.
Los números van del 0 al 20 y los colores son rojo, negro y verde, cada número tiene un color asociado.\n"""

#funciones para la Ruleta
def Solicitar_numero():
    numero = -1
    while numero < 0 or numero > 20:
        numero = int(input("Elige un número entre 0 y 20: "))
    return numero

def solicitar_dinero_apostar(saldo):
    dinero_apostado = 0
    if saldo <= 1000:
       dinero_apostado = saldo
       print("Como tu saldo es menor o igual a 1000 pesos se apuesta todo.\n")
    else:
        while dinero_apostado < APUESTA_MINIMA or dinero_apostado > saldo:
            dinero_apostado = float(input("¿Cuánto apuestas? debe ser mínimo {} pesos y no debe superar el saldo: \n".format(APUESTA_MINIMA)))
    return dinero_apostado


def Juego_ruleta():
    # El saldo con el que inicia
    saldo_global = 10000
    #print(f"Dinero disponible: {saldo_global}")
    if saldo_global < APUESTA_MINIMA:
        print("Necesitas al menos {} pesos para jugar a la ruleta.\n".format(APUESTA_MINIMA))
    else:
        print(sintesis_ruleta)
        #dinero_apostado = solicitar_dinero_apostar(saldo_global)
        eleccion_ruleta = ""
        while eleccion_ruleta != "4":
            print("Dinero disponible: {}.\n".format(saldo_global))
            print("""
            1. Solo Número.
            2. Solo color (negro, rojo y verde).
            3. Paridad (par e impar).
            4. Volver.
            """)
            eleccion_ruleta = input("Elige:\n")
            #opción de Solo Número
            if eleccion_ruleta == "1":
                if saldo_global < APUESTA_MINIMA:
                    print("Necesitas al menos {} pesos para jugar a la ruleta.\n".format(APUESTA_MINIMA))
                    break
                dinero_apostado = solicitar_dinero_apostar(saldo_global)
                numero_usuario = Solicitar_numero()
                    
                # Elegir aleatoriamente
                numero_aleatorio = random.randint(0, 20)
                print("\nNúmero obtenido: " + str(NUMERO[numero_aleatorio]))
                #print("Color obtenido: " + str(COLOR[numero_aleatorio]))
                
                # Si el usuario Acierta o no
                if numero_aleatorio == numero_usuario:
                    print("Gana el dinero apostado multiplicado por 10.\n")
                    saldo_global += dinero_apostado * 10
                else:
                    print("Pierde lo apostado.\n")
                    saldo_global -= dinero_apostado
            #opción de Solo Color    
            elif eleccion_ruleta == "2":
                if saldo_global < APUESTA_MINIMA:
                    print("Necesitas al menos {} pesos para jugar a la ruleta.".format(APUESTA_MINIMA))
                    break
                dinero_apostado = solicitar_dinero_apostar(saldo_global)
                color_eleccion_usuario = input(" 1. Rojo\n 2. Negro\n 3. Verde \n Elige:")
                if color_eleccion_usuario == "1":
                    color_usuario = "Rojo"
                elif color_eleccion_usuario == "2":
                    color_usuario = "Negro"
                elif color_eleccion_usuario == "3":
                    color_usuario = "Verde"
                    
                # Elegir aleatoriamente   
                color_aleatorio = COLOR[random.randint(0, 20)]
                print("\nColor obtenido: " + color_aleatorio)
                if color_usuario == color_aleatorio:
                    # Si el usuario Acierta o no
                    if color_aleatorio == "verde":
                        print("la apuesta se multiplica por 15")
                        saldo_global += dinero_apostado * 15
                    else:
                        print("La apuesta se multiplica por 2")
                        saldo_global += dinero_apostado * 2
                else:
                    print("Pierde lo apostado")
                    saldo_global -= dinero_apostado
            #opción de paridad        
            elif eleccion_ruleta == "3":
                if saldo_global < APUESTA_MINIMA:
                    print("Necesitas al menos {} pesos para jugar a la ruleta".format(APUESTA_MINIMA))
                    break
                dinero_apostado = solicitar_dinero_apostar(saldo_global)
                paridad_eleccion = input(
                    " 1. Impar\n 2. Par\nElige: ")
                if paridad_eleccion == "1":
                    paridad_usuario = "Impar"
                else:
                    paridad_usuario = "Par"
                
                # Elegir aleatoriamente
                numero_aleatorio = random.randint(1, 20)
                print("\nNúmero obtenido: " + str(numero_aleatorio))
                # Si el usuario Acierta o no
                if numero_aleatorio % 2 == 0 and paridad_usuario == "Par":
                    print("\nEl número es par")
                    print("Gana {} pesos\n".format(DINERO_GANADO_PARTIDAD))
                    saldo_global += DINERO_GANADO_PARTIDAD - dinero_apostado
                elif numero_aleatorio % 2 != 0 and paridad_usuario == "Impar":
                    print("\nEl número es impar")
                    print("Gana {} pesos\n".format(DINERO_GANADO_PARTIDAD))
                    saldo_global += DINERO_GANADO_PARTIDAD - dinero_apostado
                else:
                    saldo_global -= dinero_apostado
                    print("\nPierde la apuesta\n")
    return int(saldo_global)