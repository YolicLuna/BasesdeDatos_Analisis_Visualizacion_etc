import pymysql

"""
Se declara una constante, donde se almacena una sentencia sql. Para cada sentencia se crea una constante.
"""

# Constante para la sentencia que borra una tabla, se añade IF EXISTS para que ese elimine la tabla solo si existe la misma.
DROP_TABLE_USERS = "DROP TABLE IF EXISTS users"

# Constante para la sentencia que crea una tabla llamada users, con los campos id, username, password, email y created_at.
USERS_TABLE = """CREATE TABLE users(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""

# Se crea una variable values que almacena una tupla con los valores que se insertaran en la tabla users.
users = [
    ("Gaby", "12758", "Gaby@codigo facilito.com"),
    ("Marta", "hdlahoed", "marta@ejemplo.com"),
    ("Pedro", "ifguaw", "pedro@ejemplo.com"),
    ("Luis", "gjwq", "luis@ejemplo.com"),
    ("Ana", "7161968", "ana@ejemplo.com")
]

# Se crea un bloque try para manejar las excepciones que se puedan presentar en la conexión.
if __name__ == "__main__":
    try:
        # Se crea una variable connect que almacena la conexión a la base de datos, se le pasan los parametros necesarios para la conexión.
        connect = pymysql.connect(host = "127.0.0.1",
                                port = 3306, user = "root",
                                passwd = "aqui_tu_contraseña", db = "python_db")
        # Se crea una variable cursor que almacena el cursor de la conexión a la base de datos.
        with connect.cursor() as cursor:
            # Se ejecuta la sentencia DROP_TABLE_USERS para borrar la tabla users si existe.
            cursor.execute(DROP_TABLE_USERS)
            # Se ejecuta la sentencia USERS_TABLE para crear la tabla users.
            cursor.execute(USERS_TABLE)
            # Se crea una variable query que almacena la sentencia que inserta un registro en la tabla users.
            query = "INSERT INTO users(username, password, email) VALUES(%s, %s, %s)"

            # Se crea una variable que ejecuta la sentencia query y se le pasa la variable values.
            # El codigo comentado es para insertar un solo registro.
            """cursor.execut(query, values)
            connect.commit()"""

            # Se ejecuta el metodo executemany para insertar varios registros en la tabla users.
            cursor.executemany(query, users)
            # Se ejecuta el metodo commit para que los cambios se guarden en la base de datos.
            connect.commit()

            # Se crean varias consultas para seleccionar datos de la tabla users.
            # La unica que se ejecutara es la ultima, sin las comillas triples.
            # Si desea ejecutar otra consulta, solo debe quitar las comillas triples de la consulta deseada y ponerlas en la consulta que no se desea ejecutar.
            '''query = "SELECT * FROM users"'''
            '''query = "SELECT id, username, email FROM users"'''
            '''query = "SELECT id, username, email FROM users ORDER BY id DESC"'''
            '''query = "SELECT id, username, email FROM users WHERE id >= 3"'''
            '''query = "SELECT * FROM users LIMIT 3"'''
            query = "SELECT * FROM users"

            # Se crea una variable rows que ejecuta la sentencia query.
            rows = cursor.execute(query)
            # ESte codigo comentado es para mostrar diferentes formas de obtener los datos.
            # EL primero imprime lo mismo que la valiable rows.
            """print(cursor)"""
            # Esto imprime todos los registros obtenidos.
            """print(cursor.fetchall())"""
            # Esto recore el resultado de la variable rows e imprime cada registro.
            """for user in cursor.fetchall():
                print(user)"""
            # Esto imprime los primero 3 registros.
            """for user in cursor.fetchmany(3):
                print(user)"""
            
            # Se crea una variable query que almacena la sentencia que actualiza el campo username de la tabla users donde el id sea igual al elegido.
            query = "UPDATE users SET username = %s WHERE id = %s"
            # Se crea una variable values que almacena los valores que se actualizaran en la tabla users.
            values = ("Luisa", 4)
            # Se ejecuta la variable query con la variable values.
            cursor.execute(query, values)
            # Se ejecuta el metodo commit para que los cambios se guarden en la base de datos.
            connect.commit()
            # Se crea una variable query que almacena la sentencia que elimina un registro de la tabla users donde el id sea igual al elegido.
            query = "DELETE FROM users WHERE id = %s"
            # Se ejecuta la variable query con el id del registro a eliminar.
            cursor.execute(query, (5,))
            connect.commit()
    # Se crea un bloque except para manejar las excepciones que se puedan presentar en la conexión.
    except pymysql.err.OperationalError as err:
        print("No fue posible realizar la conexión.")
        print(err)
    # Se cierra la conexión a la base de datos.
    finally:
        connect.close()
        print("¡Conexión finalizada de manera correcta!")


