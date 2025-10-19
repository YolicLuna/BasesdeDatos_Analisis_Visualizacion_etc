import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from main import create_user, list_users, update_user, delete_user
from decouple import config
import psycopg2

try:
    DATABASE_URL = config("DATABASE_URL")
    connect = psycopg2.connect(DATABASE_URL)
    cursor = connect.cursor()
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
    exit()

def agregar_usuario():
    username = entry_nombre.get()
    email = entry_correo.get()

    if username and email:
        create_user(connect, cursor, username, email)
        actualizar_tabla()
        entry_nombre.delete(0, tk.END)
        entry_correo.delete(0, tk.END)
        messagebox.showinfo("Éxito", "Usuario agregado correctamente")
    else:
        messagebox.showwarning("Error", "Todos los campos son obligatorios")

def actualizar_tabla():
    for row in tabla.get_children():
        tabla.delete(row)

    cursor.execute("SELECT id, username, email FROM users")
    for id, username, email in cursor.fetchall():
        tabla.insert("", "end", values=(id, username, email))

# Configuración de la ventana principal
root = tk.Tk()
root.title("Gestion de Base de Datos")

# Campos de entrada
tk.Label(root, text="Nombre").grid(row=0, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1)

tk.Label(root, text="Correo").grid(row=1, column=0)
entry_correo = tk.Entry(root)
entry_correo.grid(row=1, column=1)


# Botón para agregar usuarios
btn_agregar = tk.Button(root, text="Agregar Usuario", command=agregar_usuario)
btn_agregar.grid(row=3, column=0, columnspan=2)

# Tabla para mostrar usuarios
tabla = ttk.Treeview(root, columns=("ID", "Nombre", "Correo"), show="headings")
tabla.heading("ID", text="ID")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Correo", text="Correo")
tabla.grid(row=4, column=0, columnspan=2)

actualizar_tabla()

# Ejecutar la interfaz
root.mainloop()
