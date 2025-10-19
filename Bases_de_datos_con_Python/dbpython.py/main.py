import pymysql

"""
Se declara una constante, donde se almacena una sentencia sql. Para cada sentencia se crea una constante.
"""
DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"
#Constante para la sentencia que borra una tabla, se añade IF EXISTS para que ese elimine la tabla solo si existe la misma.

USERS_TABLE = """CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""
#Constante para la sentencia que crea una tabla llamada users, con los campos id, username, password, email y created_at.

users = [
    ("Gaby", "12758", "Gaby@codigo facilito.com"),
    ("Marta", "hdlahoed", "marta@ejemplo.com"),
    ("Pedro", "ifguaw", "pedro@ejemplo.com"),
    ("Luis", "gjwq", "luis@ejemplo.com"),
    ("Ana", "7161968", "ana@ejemplo.com")
]
#Se crea una variable values que almacena una tupla con los valores que se insertaran en la tabla users.


if __name__ == "__main__":
#Se crea un bloque try para manejar las excepciones que se puedan presentar en la conexión.
    try:
        connect = pymysql.connect(host = "127.0.0.1",
                                port = 3306, user = "root",
                                passwd = "aqui_tu_contraseña", db = "python_db")
#Se crea una variable connect que almacena la conexión a la base de datos, se le pasan los parametros necesarios para la conexión.

        with connect.cursor() as cursor:
#Se crea una variable cursor que almacena el cursor de la conexión a la base de datos.

            cursor.execute(DROP_TABLE_USERS)
#Se ejecuta la sentencia DROP_TABLE_USERS para borrar la tabla users si existe.
            cursor.execute(USERS_TABLE)
#Se ejecuta la sentencia USERS_TABLE para crear la tabla users.

            query = "INSERT INTO users(username, password, email) VALUES(%s, %s, %s)"
           #Se crea una variable query que almacena la sentencia que inserta un registro en la tabla users.

#Se crea una variable que ejecuta la sentencia query y se le pasa la variable values.
            """cursor.execut(query, values)
            #connect.commit()"""
#Se ejecuta el metodo commit para que los cambios se guarden en la base de datos.

            cursor.executemany(query, users)
#Se ejecuta el metodo executemany para insertar varios registros en la tabla users.
            connect.commit()

            '''query = "SELECT * FROM users"'''
#Se crea una variable query que almacena la sentencia que selecciona todos los registros de la tabla users.
            '''query = "SELECT id, username, email FROM users"'''
#Se crea una variable query que almacena la sentencia que selecciona los campos id, username y email de la tabla users.
            '''query = "SELECT id, username, email FROM users ORDER BY id DESC"'''
#Se crea una variable query que almacena la sentencia que selecciona los campos id, username y email de la tabla users y los ordena de forma descendente.
            '''query = "SELECT id, username, email FROM users WHERE id >= 3"'''
#Se crea una variable query que almacena la sentencia que selecciona los campos id, username y email de la tabla users donde el id sea mayor o igual a 3.
#Se puede crear cualquier sentencia sql modificando la variable query con la sentencia deseada.
            '''query = "SELECT * FROM users LIMIT 3"'''

            query = "SELECT * FROM users"


            rows = cursor.execute(query)
#Se crea una variable rows que ejecuta la sentencia query.
            """print(cursor)"""
#Se imprime la variable rows.
            """print(cursor.fetchall())"""
#Se imprime el resultado de la variable rows.
            """for user in cursor.fetchall():
                print(user)"""
#Se recorre el resultado de la variable rows y se imprime cada registro.

            """for user in cursor.fetchmany(3):
                print(user)"""
#Se recorre el resultado de la variable rows y se imprime los primeros 3 registros.
#Se puede ejecutar fetchone para imprimir solo un registro.

            query = "UPDATE users SET username = %s WHERE id = %s"
#Se crea una variable query que almacena la sentencia que actualiza el campo username de la tabla users donde el id sea igual al elegido.
            values = ("Luisa", 4)
#Se crea una variable values que almacena los valores que se actualizaran en la tabla users.
            cursor.execute(query, values)
#Se ejecuta la variable query con la variable values.
            connect.commit()
#Se ejecuta el metodo commit para que los cambios se guarden en la base de datos.

            query = "DELETE FROM users WHERE id = %s"
#Se crea una variable query que almacena la sentencia que elimina un registro de la tabla users donde el id sea igual al elegido.
            cursor.execute(query, (5,))
#Se ejecuta la variable query con el id del registro a eliminar.
            connect.commit()

    except pymysql.err.OperationalError as err:
        print("No fue posible realizar la conexión.")
        print(err)
#Se crea un bloque except para manejar las excepciones que se puedan presentar en la conexión.

    finally:
        connect.close()
#Se cierra la conexión a la base de datos.
        print("¡Conexión finalizada de manera correcta!")


