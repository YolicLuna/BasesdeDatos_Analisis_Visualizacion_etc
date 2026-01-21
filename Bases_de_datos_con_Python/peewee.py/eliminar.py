# Se importa la libreria peewee para la conexion a la base de datos
import peewee
# Se importa la libreria datatime para el manejo de fechas.
from datetime import datetime

# Se crea la conexion a la base de datos con los datos de la base de datos
database = peewee.MySQLDatabase("python_db",
                                host = "127.0.0.1",
                                port = 3306, 
                                user = "root",
                                passwd = "aqui_tu_contraseña")

# Se crea la clase User que hereda de peewee.Model para definir la tabla de usuarios
class User(peewee.Model):
    username = peewee.CharField(max_length = 50, 
    unique = True, index = True)
    email = peewee.CharField(max_length = 60, null = False)
    active = peewee.BooleanField(default = False)
    created_at = peewee.DateTimeField(default = datetime.now)
    """Se crea la clase User que hereda de peewee.Model, se crean los campos de la tabla, se define el tipo de dato y las restricciones 
    de los campos."""

    # Se crea la clase Meta que hereda de peewee.Model, se define la base de datos y el nombre de la tabla."""
    class Meta:
        database = database
        db_table = "users"
    
    # Se crea el metodo __str__ que retorna el nombre de usuario
    def __str__(self):
        return self.username

# Se crea la condicion para que se ejecute el codigo si se ejecuta el archivo main.py
if __name__ == "__main__":
    # Se crea la condicion para que si la tabla existe se elim
    if User.table_exists():
        # Se elimina la tabla si existe
        User.drop_table()
    # Se crea la tabla si no existe
    User.create_table()

    # Se crea un objeto de la clase User y se le asignan valores a los campos, se guarda el objeto en la base de datos
    user1 = User(username = "user1", email = "user1@ejemplo.com", active = True)
    user1.save()
    
    # Se crea un objeto de la clase User y se le asignan valores a los campos, se guarda el objeto en la base de datos
    user2 = User()
    user2.username = "user2"
    user2.email = "user2@ejemplo.com"
    user2.save()
    values = {
        "username": "user3",
        "email": "user3@ejemplo.com"
    }

    # Se crea un objeto de la clase User con el diccionario de valores, se guarda el objeto en la base de datos
    user3 = User(**values)
    user3.save()

    # Se crea un objeto de la clase User con el metodo insert, se guarda el objeto en la base de datos
    user4 = User.create(username = "user4", email = "user4@ejemplo.com")
    query = User.insert(username = "user5", email = "user5@ejemplo.com")
    print(type(query))
    query.execute()
    
    # Se crea una lista de diccionarios con los valores de los campos de la tabla,
    users = [
        {"username" : "user6", "email" : "user6@ejemplo.com", "active" : True},
        {"username" : "user7", "email" : "user7@ejemplo.com"},
        {"username" : "user8", "email" : "user8@ejemplo.com", "active" : True},
        {"username" : "user9", "email" : "user9@ejemplo.com"},
        {"username" : "user10", "email" : "user10@ejemplo.com", "active" : True}
    ]

    # Se crea un objeto de la clase User con el metodo insert_many, se guarda el objeto en la base de datos
    query = User.insert_many(users)
    query.execute()

    # Se crea una consulta a la tabla User, se obtiene el objeto con el nombre de usuario user10 y se elimina el objeto de la base de datos
    user = User.select().where(User.username == "user10").get()
    user.delete_instance()

    # Se crea un objeto de la clase User con el metodo delete, se elimina el objeto de la base de datos
    query = User.delete().where(User.id == 9)
    query.execute()
