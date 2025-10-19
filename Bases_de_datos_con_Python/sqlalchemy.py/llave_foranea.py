import json
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import (Table, Column, Integer, 
                        String, DateTime, 
                        Float, ForeignKey
                        )
from datetime import datetime
from sqlalchemy import update, delete, select

engine = create_engine("postgresql://postgres:aqui_tu_contraseña@localhost/pythondb")
metadata = MetaData()

orders = Table(
    "orders",
    metadata,
    Column("id", Integer(), primary_key = True)
)

products = Table(
    "products",
    metadata,
    Column("id", Integer(), primary_key = True),
    Column("title", String()),
    Column("price", Float(5, 2)),
    Column("order_id", Integer, ForeignKey("orders.id"))
)

if __name__ == "__main__":

    metadata.drop_all(engine)
    metadata.create_all(engine)

    with engine.connect() as connection:

        trans = connection.begin()  # Iniciar una transacción
        try:
            insert_query = orders.insert()
            connection.execute(insert_query)

            insert_query = products.insert().values(
                title = "Iphone",
                price = 800.00,
                order_id = 1
            )
            connection.execute(insert_query)

            insert_query = products.insert().values(
                title = "Galaxy",
                price = 730.00,
                order_id = 1
            )
            connection.execute(insert_query)

            insert_query = products.insert().values(
                title = "Motorola",
                price = 960.00,
                order_id = 1
            )
            connection.execute(insert_query)

#Inner join          
            
            select_query = select(
                [
                    products.c.title,
                    products.c.price
                ]
            ).select_from(
                products.join(orders, products.c.id == orders.c.product_id)
            ).where(
                orders.c.id == 1
            )

            result = connection.execute(select_query)

            for product in result.fetchall():
                print(product.title, product.price)

            trans.commit()  # Confirmar la transacción

        except Exception as e:
            trans.rollback()  # Revertir la transacción en caso de error
            print(f"Error: {e}")          