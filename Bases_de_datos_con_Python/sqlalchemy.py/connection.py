import psycopg2
from psycopg2 import sql

# Datos de conexión
conn = psycopg2.connect(
    dbname="pythondb",
    user="postgres",
    password="aqui_tu_contraseña",
    host="localhost",
    port="5432"
)

# Crear un cursor
cur = conn.cursor()

# Ejecutar la consulta
cur.execute("SELECT * FROM usuarios;")

# Obtener los resultados
rows = cur.fetchall()

# Imprimir los resultados
for row in rows:
    print(row)

# Cerrar el cursor y la conexión
cur.close()
conn.close()