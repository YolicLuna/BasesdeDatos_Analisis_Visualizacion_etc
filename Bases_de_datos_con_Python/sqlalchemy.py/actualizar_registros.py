import json
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy import update

engine = create_engine("postgresql://postgres:aqui_tu_contraseña@localhost/pythondb")
metadata = MetaData()

usuarios = Table(
    "usuarios",
    metadata,
    Column("id", Integer(), primary_key = True),
    Column("age", Integer),
    Column("country", String(20), nullable = False),
    Column("username", String(50), index = True, nullable = False),
    Column("email", String(50), nullable = False),
    Column("gender", String(6), nullable = False),
    Column("created_at", DateTime(), default = datetime.now)
)

if __name__ == "__main__":

    connection = engine.connect()

    with engine.connect() as connection:

#Lista todos los  usuarios cuyo genero sea female y país mexico y japon.

        trans = connection.begin()  # Iniciar una transacción
        try:

            update_query = update(usuarios).where(
                usuarios.c.id == 1
                
            ).values(
                username = "yolic"
            )

            result = connection.execute(update_query) #ResultProxy
            print(result.rowcount)
#                print(user.email)

            trans.commit()  # Confirmar la transacción
        except Exception as e:
            trans.rollback()  # Revertir la transacción en caso de error
            print(f"Error: {e}")