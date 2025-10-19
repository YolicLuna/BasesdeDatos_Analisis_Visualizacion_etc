import json
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, DateTime
from datetime import datetime 
from sqlalchemy import desc, asc, and_, or_, not_

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

        trans = connection.begin()  # Iniciar una transacción
        try:

#Listar de forma decendente el nombre de los primeros 10 usuarios cuyo genero sea femenino y posea por pais mexico y japon

            select_query = usuarios.select().where(
                and_(
                    usuarios.c.gender == "Female",
                or_(
                    usuarios.c.country == "Mexico",
                    usuarios.c.country == "Japon"
                    )
                )
            ).order_by(
                asc(usuarios.c.username)
            ).limit(10)
            
            result = connection.execute(select_query) #ResultProxy

            for user in result.fetchall():
                print(user.username)
#                print(user.email)

            trans.commit()  # Confirmar la transacción
        except Exception as e:
            trans.rollback()  # Revertir la transacción en caso de error
            print(f"Error: {e}")