import os
#Se importa el módulo os para poder ejecutar comandos de la terminal desde el script de Python, en este caso "cls" para limpiar la terminal.
import psycopg2
#Se importa el módulo psycopg2 para poder realizar la conexión a la base de datos PostgreSQL.
from decouple import config
#Se importa el módulo config para cargar la URL de nuestros datos de conexión desde las variables de entorno
import tkinter as tk
from tkinter import messagebox

DROP_USERS_TABLE = "DROP TABLE IF EXISTS users"
#Se elimina la tabla de usuarios si ya existe

USERS_TABLE = """CREATE TABLE IF NOT EXISTS users(
    id SERIAL,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)"""
#Se crea la tabla de usuarios

def system_clear(function):
    def wrapper(*args, **kwargs):
        connect, cursor = args[:2]

        # Ejecuta cls en windows o clear en linux/mac
        os.system("cls" if os.name == "nt" else "clear")

        function(*args, **kwargs)

        os.system("cls" if os.name == "nt" else "clear")
    
    wrapper.__doc__ = function.__doc__
    return wrapper

'''Se actualiza el decorador para limpiar la terminal, se crea la función wrapper que recibe cualquier cantidad de argumentos y parámetros clave, se extraen connect y cursor de los argumentos, se ejecuta el comando "clear" para limpiar la terminal, se ejecuta la función con todos los argumentos y parámetros clave, se solicita al usuario que presione la tecla "enter" para continuar, la documentación de la función decorada se le pasa a __doc__ y por último se agrega un return wrapper al final de la función para retornar la función wrapper.'''

@system_clear
def create_user(connect, cursor, username, email): 
    #Se crea la función para crear un nuevo usuario, se agregan los parámetros connect y cursor para realizar la conexión a la base de datos.

    """A) Crear un nuevo usuario"""
    
    query = "INSERT INTO users(username, email) VALUES(%s, %s)"
    values = (username, email)

    cursor.execute(query, values)
    connect.commit()

    print(">>> Usuario creado correctamente. <<<")

'''En esta función se crea un nuevo usuario, se reciben los parámetros username y email, se crea una consulta para insertar los datos en la tabla de usuarios y se confirman los cambios.'''

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

    def wrapper(id, connect, cursor, *args, **kwargs):
        query = "SELECT id FROM users WHERE id = %s"
        cursor.execute(query, (id,))

        user = cursor.fetchone()
        if user:
            function(id, connect, cursor, *args, **kwargs)
        else:
            print(">>> No existe un usuario con el id proporcionado, intenta de nuevo. <<<")

    wrapper.__doc__ = function.__doc__
    return wrapper

'''Se crea un decorador para verificar si un usuario existe, se crea la función wrapper que recibe como parámetro id, connect y cursor, se crea una consulta para seleccionar el usuario con el id proporcionado, se ejecuta la consulta y se obtiene el usuario, si el usuario existe se ejecuta la función con el id, connect y cursor, si no existe se imprime un mensaje en pantalla, la documentación de la función decorada se le pasa a __doc__ y por ultimo se agrega un return wrapper al final de la función para retornar la función wrapper.'''

@system_clear
@user_exists
def update_user(id, connect, cursor, username, email):
    """C) Actualizar un usuario"""

    query = "UPDATE users SET username = %s, email = %s WHERE id = %s"
    values = (username, email, id)

    cursor.execute(query, values)
    connect.commit()

    print(">>> Usuario actualizado correctamente. <<<")

'''Para la funcion de actualizar usuario también podemos realizarla mediante el decorador creado anteriormente. Al principio de la función se agrega el decorador @user_exists, que recibe como parámetro la función update_user, se reciben los parámetros id, username y email, se crea una consulta para actualizar los datos del usuario y se confirman los cambios en la base de datos.'''

@system_clear
@user_exists
def delete_user(id, connect, cursor):
    """D) Eliminar un usuario"""

    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (id,))
    connect.commit()

    print(">>> Usuario eliminado correctamente. <<<")

'''En esta función se elimina un usuario, se recibe el parámetro id, se crea una consulta para eliminar el usuario con el id proporcionado y se confirman los cambios.'''

#Se crean las funciones para las opciones del menú

def default(*args):
    print("Opción no válida")

def run_interface():
    # Función para manejar la creación de un nuevo usuario
    def on_create_user():
        username = username_entry.get()
        email = email_entry.get()
        if username and email:
            create_user(connect, cursor, username, email)
            messagebox.showinfo("Success", "Usuario creado correctamente.")
        else:
            messagebox.showwarning("Input Error", "Por favor ingresa todos los datos.")

    # Función para manejar la lista de todos los usuarios
    def on_list_users():
        query = "SELECT id, username, email FROM users"
        cursor.execute(query)
        users = cursor.fetchall()
        user_list.delete(0, tk.END)
        for id, username, email in users:
            user_list.insert(tk.END, f"{id} - {username} - {email}")

    # Función para manejar la actualización de un usuario
    def on_update_user():
        id = id_entry.get()
        username = username_entry.get()
        email = email_entry.get()
        if id and username and email:
            update_user(id, connect, cursor, username, email)
            messagebox.showinfo("Success", "Usuario actualizado correctamente.")
        else:
            messagebox.showwarning("Input Error", "Por favor ingresa todos los datos.")

    # Función para manejar la eliminación de un usuario
    def on_delete_user():
        id = id_entry.get()
        if id:
            query = "SELECT id FROM users WHERE id = %s"
            cursor.execute(query, (id,))
            user = cursor.fetchone()
            if user:
                confirm = messagebox.askyesno("Confirmar", f"¿Estás seguro de eliminar el usuario con id {id}?")
                if confirm:
                    delete_user(id, connect, cursor)
                    messagebox.showinfo("Success", "Usuario eliminado correctamente.")
            else:
                messagebox.showwarning("Input Error", "No existe un usuario con el id proporcionado.")
        else:
            messagebox.showwarning("Input Error", "Por favor ingresa el id del usuario.")

    # Función para manejar el guardado de cambios en la base de datos
    def on_save_changes():
        connect.commit()
        messagebox.showinfo("Success", "Cambios guardados correctamente.")

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Moon Database")
    root.configure(bg='#1c1c1c')

    # Configurar la cuadrícula para que se expanda
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_rowconfigure(4, weight=1)
    root.grid_rowconfigure(5, weight=1)
    root.grid_rowconfigure(6, weight=1)

    # Crear y colocar etiquetas y campos de entrada para id, nombre de usuario y correo electrónico
    tk.Label(root, text="ID del Usuario:", bg='#1c1c1c', fg='white').grid(row=0, column=0, padx=10, pady=5)
    id_entry = tk.Entry(root)
    id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Nombre de Usuario:", bg='#1c1c1c', fg='white').grid(row=1, column=0, padx=10, pady=5)
    username_entry = tk.Entry(root)
    username_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(root, text="Correo Electrónico:", bg='#1c1c1c', fg='white').grid(row=2, column=0, padx=10, pady=5)
    email_entry = tk.Entry(root)
    email_entry.grid(row=2, column=1, padx=10, pady=5)

    # Crear y colocar botones para cada acción
    tk.Button(root, text="Crear Usuario", command=on_create_user, bg='#333333', fg='white').grid(row=3, column=0, padx=10, pady=5)
    tk.Button(root, text="Listar Usuarios", command=on_list_users, bg='#333333', fg='white').grid(row=3, column=1, padx=10, pady=5)
    tk.Button(root, text="Actualizar Usuario", command=on_update_user, bg='#333333', fg='white').grid(row=4, column=0, padx=10, pady=5)
    tk.Button(root, text="Eliminar Usuario", command=on_delete_user, bg='#333333', fg='white').grid(row=4, column=1, padx=10, pady=5)
    tk.Button(root, text="Guardar Cambios", command=on_save_changes, bg='#333333', fg='white').grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    # Crear y colocar la lista para mostrar los usuarios
    user_list = tk.Listbox(root, bg='#1c1c1c', fg='white', width=50)
    user_list.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

    # Iniciar el bucle de eventos de Tkinter
    root.mainloop()

if __name__ == '__main__':

    options = {
        "a" : create_user,
        "b" : list_users,
        "c" : update_user,
        "d" : delete_user
    }
#Se crea un diccionario con las opciones del menú

    try:
        DATABASE_URL = config("DATABASE_URL")
        connect = psycopg2.connect(DATABASE_URL)
        cursor = connect.cursor()
#Se realiza la conexión a la base de datos
        with connect.cursor() as cursor:

           # cursor.execute(DROP_USERS_TABLE)
           # cursor.execute(USERS_TABLE)
#Se crea la tabla de usuarios

            connect.commit()
#Se la confirmación de los cambios realizados en nuestra base de datos

            run_interface()

            function = options.get(options, default)

            function(connect, cursor)

            '''Se obtiene la función correspondiente a la opción seleccionada por el usuario y se ejecuta la función 
con los parámetros obtenidos, además se realiza la conexión a la base de datos y se crea el cursor para ejecutar las consultas.'''

        connect.close()

    except psycopg2.OperationalError as err:
        print("No fue posible realizar la conexión")
        print(err)
#Se aplican excepciones en caso de que no se pueda realizar la conexión
