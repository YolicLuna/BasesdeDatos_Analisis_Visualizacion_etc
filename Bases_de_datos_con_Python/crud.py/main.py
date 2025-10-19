import os
# Se importa el módulo os para poder ejecutar comandos de la terminal desde el script de Python, en este caso "cls" para limpiar la terminal.
import psycopg2
# Se importa el módulo psycopg2 para poder realizar la conexión a la base de datos PostgreSQL.
from decouple import config
# Se importa el módulo config para cargar la URL de nuestros datos de conexión desde las variables de entorno

DROP_USERS_TABLE = "DROP TABLE IF EXISTS users"
# Se elimina la tabla de usuarios si ya existe

USERS_TABLE = """CREATE TABLE IF NOT EXISTS users(
    id SERIAL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""
# Se crea la tabla de usuarios


def system_clear(function):
    def wrapper(connect, cursor):
        # Ejecuta cls en windows o clear en linux/mac
        os.system("cls" if os.name == "nt" else "clear")

        function(connect, cursor)

        input("Presiona enter para continuar...")

        os.system("cls" if os.name == "nt" else "clear")

    wrapper.__doc__ = function.__doc__
    return wrapper


'''Se crea un decorador para limpiar la terminal, se crea la función wrapper que recibe como parámetro connect y cursor, se ejecuta el comando 
"clear" para limpiar la terminal, se ejecuta la función con el cursor y se solicita al usuario que presione la tecla "enter" para continuar, 
la documentación de la función decorada se le pasa a __doc__ y por ultimo se agrega un return wrapper al final de la función para retornar la 
función wrapper.'''


@system_clear
def create_user(connect, cursor):
    # Se crea la función para crear un nuevo usuario, se agregan los parámetros connect y cursor para realizar la conexión a la base de datos.
    """A) Crear un nuevo usuario"""

    username = input("Ingresa un nombre de usuario: ")
    email = input("Ingresa un correo electronico: ")

    query = "INSERT INTO users(username, email) VALUES(%s, %s)"
    values = (username, email)

    cursor.execute(query, values)
    connect.commit()

    print(">>> Usuario creado correctamente. <<<")


'''En esta función se crea un nuevo usuario, se solicita al usuario que ingrese un nombre de usuario y un correo 
electrónico, se crea una consulta para insertar los datos en la tabla de usuarios y se confirman los cambios.'''


@system_clear
def list_users(connect, cursor):
    """B) Listar todos los usuarios"""

    query = "SELECT id, username, email FROM users"
    cursor.execute(query)

    for id, username, email in cursor.fetchall():
        print(id, '-', username, '-', email)

    print(">>> Usuarios listados correctamente. <<<")


'''En esta función se listan todos los usuarios, se crea una consulta para seleccionar todos los usuarios de 
la tabla de usuarios y se recorren los resultados para imprimirlos en pantalla.'''


def user_exists(function):

    def wrapper(connect, cursor):
        id = input("Ingresa el id del usuario: ")

        query = "SELECT id FROM users WHERE id = %s"
        cursor.execute(query, (id,))

        user = cursor.fetchone()
        if user:
            function(id, connect, cursor)
        else:
            print(
                ">>> No existe un usuario con el id proporcionado, intenta de nuevo. <<<")

    wrapper.__doc__ = function.__doc__
    return wrapper


'''Se crea un decorador para verificar si un usuario existe, se crea la función wrapper que recibe como parámetro connect,
 cursor y id, se crea una consulta para seleccionar el usuario con el id proporcionado, se ejecuta la consulta y se obtiene
 el usuario, si el usuario existe se ejecuta la función con el id, connect y cursor, si no existe se imprime un mensaje en 
 pantalla, la documentación de la función decorada se le pasa a __doc__ y por ultimo se agrega un return wrapper al final 
 de la función para retornar la función wrapper.'''

# system_clear
# def update_user(connect, cursor):
# """C) Actualizar un usuario"""

# id = input("Ingresa el id del usuario que deseas actualizar: ")

# query = "SELECT id FROM users WHERE id = %s"
# cursor.execute(query, (id,))

# user = cursor.fetchone()
# if user:

# username = input("Ingresar nuevo nombre de usuario: ")
# email = input("Ingresar el nuevo correo electrónico: ")

# query = "UPDATE users SET username = %s, email = %s WHERE id = %s"
# values = (username, email, id)

# cursor.execute(query, values)
# connect.commit()

# print(">>> Usuario actualizado correctamente. <<<")

# else:
# print("No existe un usuario con el id proporcionado, intenta de nuevo.")

'''En esta función se actualiza un usuario, se solicita al usuario que ingrese el id del usuario que desea actualizar, 
se crea una consulta para seleccionar el usuario con el id proporcionado, se solicita al usuario que ingrese el nuevo 
nombre de usuario y el nuevo correo electrónico, se crea una consulta para actualizar los datos del usuario y se confirman los cambios'''


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


'''Para la funcion de actualizar usuario también podemos realizarla mediante el decorador creado anteriormente. Al principio 
de la función se agrega el decorador @user_exists, que recibe como parámetro la función update_user, se solicita al usuario 
que ingrese el id del usuario que desea actualizar, se solicita al usuario que ingrese el nuevo nombre de usuario y el nuevo 
correo electrónico, se crea una consulta para actualizar los datos del usuario y se confirman los cambios en la base de datos.'''


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


'''En esta función se elimina un usuario, se solicita al usuario que ingrese el id del usuario que desea eliminar, 
se crea una consulta para seleccionar el usuario con el id proporcionado, se pregunta al usuario si está seguro 
de eliminar el usuario, si la respuesta es si, se crea una consulta para eliminar el usuario y se confirman los cambios'''

# Se crean las funciones para las opciones del menú


def default(*args):
    print("Opción no válida")


if __name__ == '__main__':

    options = {
        "a": create_user,
        "b": list_users,
        "c": update_user,
        "d": delete_user
    }
# Se crea un diccionario con las opciones del menú

    try:
        DATABASE_URL = config("DATABASE_URL")
        connect = psycopg2.connect(DATABASE_URL)
        cursor = connect.cursor()
# Se realiza la conexión a la base de datos
        with connect.cursor() as cursor:

           # cursor.execute(DROP_USERS_TABLE)
           # cursor.execute(USERS_TABLE)
            # Se crea la tabla de usuarios

            connect.commit()
# Se la confirmación de los cambios realizados en nuestra base de datos

            while True:
                for function in options.values():
                    print(function.__doc__)

                print('Escribe "quit" o "q" para salir')

                option = input("Selecciona una opción valida: ").lower()

                if option == "quit" or option == "q":
                    break

                '''Se crea un ciclo while que se ejecutará mientras el usuario no seleccione la opción de salir, 
se recorren las funciones, se imprime la descripción de cada función y se solicita al usuario que seleccione una opción, 
si la opción es salir, se rompe el ciclo.'''

                function = options.get(option, default)

                function(connect, cursor)

                '''Se obtiene la función correspondiente a la opción seleccionada por el usuario y se ejecuta la función 
con los parámetros obtenidos, además se realiza la conexión a la base de datos y se crea el cursor para ejecutar las consultas.'''

        connect.close()

    except psycopg2.OperationalError as err:
        print("No fue posible realizar la conexión")
        print(err)
# Se aplican excepciones en caso de que no se pueda realizar la conexión
