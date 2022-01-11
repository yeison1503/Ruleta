from conexion import obtener_conexion

def NEW_jugador(nombre, edad, dinero):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO jugadores(name, age, cash) VALUES (%s, %s, %s);",
                       (nombre, edad, dinero))
    conexion.commit()
    conexion.close()

def consultar(nombre):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        consulta = ("SELECT name FROM jugadores WHERE name = %s;",(nombre))
        #nom = cursor.execute(consulta, nombre)
        nom = cursor.fetchone()
    conexion.close()
    return nombre

def eliminar(nombre):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM jugadores WHERE name = %s;",(nombre))
    conexion.commit()
    conexion.close()

def modificar(nombre, edad, dinero, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        consulta = "UPDATE jugadores SET name = %s, age = %s, cash = %s WHERE id = %s;"
        cursor.execute(consulta, (nombre, edad, dinero, id))
        # cursor.execute("UPDATE jugadores SET name = %s, age = %s, cash = %s WHERE id = %s",
        #                (nombre, edad, dinero, id))
    conexion.commit()
    conexion.close()
    
def Listar_jugador():
    conexion = obtener_conexion()
    jugadores = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, name, age, cash FROM jugadores;")
        jugadores = cursor.fetchall()
		
        for jugadores in jugadores:
            print(jugadores)
    conexion.close()
    return jugadores
