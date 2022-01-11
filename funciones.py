from conexion import obtener_conexion

def NEW_jugador(nombre, edad, dinero):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO jugadores(name, age, cash) VALUES (%s, %s, %s);",
                       (nombre, edad, dinero))
    conexion.commit()
    conexion.close()

def consultarNom(nombre):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        
        consulta = "SELECT id, name, age, cash FROM jugadores WHERE name = %s;"
        vnombre = cursor.execute(consulta, nombre)
        vnombre = cursor.fetchall()
        
        for vnombre in vnombre:
            if nombre == vnombre[1]:
                #print(vnombre[1])
                return vnombre[1]
    conexion.close()
    
def consultarId(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        
        consulta = "SELECT id, name, age, cash FROM jugadores WHERE id = %s;"
        vid = cursor.execute(consulta, id)
        vid = cursor.fetchall()
        
        for vid in vid:
            if id == vid[0]:
                return vid[0]
    conexion.close()

def consultarEdad(nombre):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        
        consulta = "SELECT id, name, age, cash FROM jugadores WHERE name = %s;"
        vedad = cursor.execute(consulta, nombre)
        vedad = cursor.fetchall()
        
        for vedad in vedad:
            if nombre == vedad[1]:
                return vedad[2]
    conexion.close()
    
def consultarSaldo(nombre):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        
        consulta = "SELECT id, name, age, cash FROM jugadores WHERE name = %s;"
        vdin = cursor.execute(consulta, nombre)
        vdin = cursor.fetchall()
        
        for vdin in vdin:
            if nombre == vdin[1]:
                return vdin[3]
    conexion.close()    

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

def modificarSaldo(nombre, dinero):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        consulta = "UPDATE jugadores SET cash = %s WHERE name = %s;"
        cursor.execute(consulta, (dinero, nombre))
    conexion.commit()
    conexion.close()

def Listar_jugador():
    conexion = obtener_conexion()
    lista = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, name, age, cash FROM jugadores;")
        #cursor.execute("SELECT * FROM jugadores ORDER BY name ASC")
        lista = cursor.fetchall()
    conexion.close()
    return lista
