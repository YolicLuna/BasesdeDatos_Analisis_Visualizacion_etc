import mysql.connector
import json

# Cargar configuración desde config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

try:
    # Intentar conectar a la base de datos
    conexion = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"],
        port=config["port"]
    )
    if conexion.is_connected():
        print(">>> Conexión exitosa a la base de datos MySQL <<<")
        conexion.close()
except mysql.connector.Error as err:
    print(">>> Error al conectar a la base de datos <<<")
    print(err)

    