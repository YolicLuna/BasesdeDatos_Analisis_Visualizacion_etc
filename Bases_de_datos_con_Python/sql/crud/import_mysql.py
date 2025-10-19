import mysql.connector
import json
import os
from decouple import config

 # Crear tabla si no existe
users_table = """CREATE TABLE IF NOT EXISTS users(
               id INT AUTO_INCREMENT PRIMARY KEY,
               username VARCHAR(50) NOT NULL,
               email VARCHAR(50) NOT NULL,
               created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
               """


# Cargar configuración desde config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Función para limpiar la terminal
def system_clear(function):
    def wrapper(connect, cursor):
        os.system("cls")
        function(connect, cursor)
        input("Presiona enter para continuar...")
        os.system("cls")
    wrapper.__doc__ = function.__doc__
    return wrapper

@system_clear
def create_user(connect, cursor):
    """A) Crear un nuevo usuario"""
    username = input("Ingresa un nombre de usuario: ")
    email = input("Ingresa un correo electronico: ")
    query = "INSERT INTO users(username, email) VALUES(%s, %s)"
    values = (username, email)
    cursor.execute(query, values)
    connect.commit()
    print(">>> Usuario creado correctamente. <<<")

@system_clear
def list_users(connect, cursor):
    """B) Listar todos los usuarios"""
    query = "SELECT id, username, email FROM users"
    cursor.execute(query)
    for id, username, email in cursor.fetchall():
        print(id, '-', username, '-', email)
    print(">>> Usuarios listados correctamente. <<<")

def user_exists(function):
    def wrapper(connect, cursor):
        id = input("Ingresa el id del usuario: ")
        query = "SELECT id FROM users WHERE id = %s"
        cursor.execute(query, (id,))
        user = cursor.fetchone()
        if user:
            function(id, connect, cursor)
        else:
            print(">>> No existe un usuario con el id proporcionado, intenta de nuevo. <<<")
    wrapper.__doc__ = function.__doc__
    return wrapper

@system_clear
@user_exists
def update_user(id, connect, cursor):
    """C) Actualizar un usuario"""
    username = input("Ingresar nuevo nombre de usuario: ")
    email = input("Ingresar el nuevo correo electrónico: ")
    query = "UPDATE users SET username = %s, email = %s WHERE id = %s"
    values = (username, email, id)
    cursor.execute(query, values)
    connect.commit()
    print(">>> Usuario actualizado correctamente. <<<")

@system_clear
def delete_user(connect, cursor):
    """D) Eliminar un usuario"""
    id = input("Ingresa el id del usuario que deseas eliminar: ")
    query = "SELECT id FROM users WHERE id = %s"
    cursor.execute(query, (id,))
    user = cursor.fetchone()
    if user:
        print("Estás seguro de eliminar el usuario con id", id)
        confirm = input("Si/No: ").lower()
        if confirm == "si":
            query = "DELETE FROM users WHERE id = %s"
            cursor.execute(query, (id,))
            connect.commit()
            print(">>> Usuario eliminado correctamente. <<<")
        else:
            print(">>> Operación cancelada. <<<")
    else:
        print(">>> No existe un usuario con el id proporcionado, intenta de nuevo. <<<")

def default(*args):
    print("Opción no válida")

if __name__ == '__main__':
    options = {
        "a": create_user,
        "b": list_users,
        "c": update_user,
        "d": delete_user
    }

    try:
        # Conexión a la base de datos MySQL
        connect = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"],
            port=config["port"]
        )
        cursor = connect.cursor()

        while True:
            for function in options.values():
                print(function.__doc__)
            print('Escribe "quit" o "q" para salir')
            option = input("Selecciona una opción valida: ").lower()
            if option == "quit" or option == "q":
                break
            function = options.get(option, default)
            function(connect, cursor)

        connect.close()

    except mysql.connector.Error as err:
        print("No fue posible realizar la conexión")
        print(err)


