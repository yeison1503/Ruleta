# Ruleta-CRUD-con-python-y-MySQL.

En este repositorio se desarrolló un programa para la creación de usuarios, donde también se podían modificar, eliminar y editar estos, para la base de datos se trabajó con MySQ.
También tiene una opción para que un usuario pueda jugar a la Ruleta, y en este juego puede optar por elegir varias opciones de apuesta.




Para iniciar la ejecución se debe crear la base de datos de MySQL, para cual se debe instalar XAMPP con anterioridad.
los siguientes comandos son para la creación de la base de datos y la tabla.

######## CREATE DATABASE jugadores;
######## USE jugadores;
######## CREATE TABLE IF NOT EXISTS jugadores(
########  	id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL,
######## 	 name VARCHAR(255) NOT NULL,
######## 	 age SMALLINT NOT NULL,
########   cash SMALLINT NOT NULL,
######## 	PRIMARY KEY(id)
######## );

Para la ejecución del programa solo basta con ejecutar el archivo Menu.py en cualquier terminal de un sistema operativo que tenga instalado Python, con el siguiente comando python "python .\Menu.py" por ejemplo un framework como anaconda o visual studio code.

