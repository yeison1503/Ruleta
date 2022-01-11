from conexion import obtener_conexion

def NEW_jugador(nombre, edad, dinero):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO juegos(nombre, descripcion, precio) VALUES (%s, %s, %s)",
                       (nombre, edad, dinero))
    conexion.commit()
    conexion.close()
