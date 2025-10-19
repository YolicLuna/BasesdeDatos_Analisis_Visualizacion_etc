import peewee
#Se importa la libreria peewee para la conexion a la base de datos

database = peewee.MySQLDatabase("python_db",
                                host = "127.0.0.1",
                                port = 3306, 
                                user = "root",
                                passwd = "aqui_tu_contraseña")

class Author(peewee.Model):
    name = peewee.CharField(max_length=50)

    class Meta:
        database = database
        db_table = "authors"
    
    def __str__(self):
        return self.name
        
class Book(peewee.Model):
    title = peewee.CharField(max_length=50)
    author = peewee.ForeignKeyField(Author, backref = "books")

    class Meta:
        database = database
        db_table = "books"
    
    def __str__(self):
        return self.title

if __name__ == "__main__":
    
    database.drop_tables([Author, Book])
    database.create_tables([Author, Book])

    author1 = Author.create(name = "Stephen King")

    book1 = Book.create(title = "It", author = author1)
    book2 = Book.create(title = "El resplandor", author = author1)
    book3 = Book.create(title = "Cujo", author = author1)

    for book in author1.books:
        print(book)
